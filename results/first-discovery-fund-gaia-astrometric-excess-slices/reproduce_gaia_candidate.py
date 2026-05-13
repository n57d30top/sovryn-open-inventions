#!/usr/bin/env python3
"""Standalone public replay for the Gaia astrometric-excess candidate.

This script fetches the same public Gaia EDR3 TAP slices recorded in the public
package and recomputes the bounded metrics. It does not claim external
validation and does not generalize beyond the four recorded RA slices.
"""
import csv
import hashlib
import io
import json
import math
import sys
import urllib.parse
import urllib.request
from pathlib import Path

EXPECTED = {
    "measuredOutcome": 0.4256,
    "residualMagnitude": 0.1343,
    "baselines": {
        "phot_g_mean_magnitude_correlation": 0.1372,
        "bp_rp_color_correlation": 0.1126,
        "single_sky_slice_dominance_control": 0.5075,
    },
}
SLICES = [
    ("ra_000_090", 0, 90),
    ("ra_090_180", 90, 180),
    ("ra_180_270", 180, 270),
    ("ra_270_360", 270, 360),
]

def tap_url(min_ra, max_ra):
    query = " ".join([
        "select top 40 source_id,ra,dec,phot_g_mean_mag,bp_rp,astrometric_excess_noise",
        "from gaiaedr3.gaia_source",
        f"where ra >= {min_ra} and ra < {max_ra}",
        "and dec > -30 and dec < 30",
        "and phot_g_mean_mag between 14 and 20",
        "and bp_rp is not null",
        "and astrometric_excess_noise is not null",
        "order by source_id",
    ])
    return "https://gea.esac.esa.int/tap-server/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=" + urllib.parse.quote(query)

def fetch_text(url):
    with urllib.request.urlopen(url, timeout=60) as response:
        payload = response.read()
        text = payload.decode("utf-8")
        return text, {
            "status": response.status,
            "contentLength": len(text),
            "sourceHash": hashlib.sha256(payload).hexdigest(),
        }

def parse_rows(text, slice_id):
    rows = []
    for rec in csv.DictReader(io.StringIO(text)):
        try:
            rows.append({
                "sourceId": rec["source_id"],
                "ra": float(rec["ra"]),
                "dec": float(rec["dec"]),
                "g": float(rec["phot_g_mean_mag"]),
                "color": float(rec["bp_rp"]),
                "excess": float(rec["astrometric_excess_noise"]),
                "sliceId": slice_id,
            })
        except (KeyError, ValueError):
            pass
    return rows

def mean(values):
    return sum(values) / len(values) if values else 0.0

def pearson(left, right):
    if len(left) != len(right) or len(left) < 2:
        return 0.0
    left_mean = mean(left)
    right_mean = mean(right)
    numerator = sum((x - left_mean) * (y - right_mean) for x, y in zip(left, right))
    left_squares = sum((x - left_mean) ** 2 for x in left)
    right_squares = sum((y - right_mean) ** 2 for y in right)
    denominator = math.sqrt(left_squares * right_squares)
    return 0.0 if denominator == 0 else numerator / denominator

def round_metric(value):
    return round(value * 10000) / 10000

def score(rows):
    residuals = []
    for row in rows:
        expected = 0.08 + max(0, row["g"] - 16) * 0.1 + abs(row["color"] - 1.2) * 0.08
        residuals.append({**row, "residual": row["excess"] - expected})
    slice_means = []
    for slice_id, _, _ in SLICES:
        values = [row["residual"] for row in residuals if row["sliceId"] == slice_id]
        slice_means.append({"sliceId": slice_id, "residualMean": mean(values)})
    measured = round_metric(mean([row["excess"] for row in rows]))
    residual_magnitude = round_metric(mean([abs(row["residualMean"]) for row in slice_means]))
    magnitude_correlation = round_metric(abs(pearson([row["g"] for row in rows], [row["excess"] for row in rows])))
    color_correlation = round_metric(abs(pearson([row["color"] for row in rows], [row["excess"] for row in rows])))
    residual_abs_sum = sum(abs(row["residualMean"]) for row in slice_means)
    single_slice_dominance = round_metric(1.0 if residual_abs_sum == 0 else max(abs(row["residualMean"]) for row in slice_means) / residual_abs_sum)
    positive_slices = sum(1 for row in slice_means if row["residualMean"] > 0.05)
    negative_slices = sum(1 for row in slice_means if row["residualMean"] < -0.05)
    baselines = {
        "phot_g_mean_magnitude_correlation": magnitude_correlation,
        "bp_rp_color_correlation": color_correlation,
        "single_sky_slice_dominance_control": single_slice_dominance,
    }
    return {
        "measuredOutcome": measured,
        "residualMagnitude": residual_magnitude,
        "baselines": baselines,
        "sliceMeans": slice_means,
        "crossSliceSupport": max(positive_slices, negative_slices) >= 2,
        "counterexampleCollapsed": not (max(positive_slices, negative_slices) >= 2) or single_slice_dominance > 0.85,
    }

def main():
    rows = []
    receipts = []
    for slice_id, min_ra, max_ra in SLICES:
        url = tap_url(min_ra, max_ra)
        text, receipt = fetch_text(url)
        receipt.update({"sliceId": slice_id, "sourceUrl": url})
        receipts.append(receipt)
        rows.extend(parse_rows(text, slice_id))
    metrics = score(rows)
    reproduced = (
        len(rows) == 160 and
        metrics["measuredOutcome"] == EXPECTED["measuredOutcome"] and
        metrics["residualMagnitude"] == EXPECTED["residualMagnitude"] and
        metrics["baselines"] == EXPECTED["baselines"]
    )
    result = {
        "kind": "gaia_raw_scientific_reproduction_result",
        "candidateId": "DISCOVERY-LIFT-INSIGHT-HARD-GEN-GAIA-ASTROMETRIC-EXCESS-SIGNIFICANCE-GE-0F9E75E885B6",
        "publicReviewStatus": "external_review_ready_raw_scientific_reproduction_succeeded_caveated_no_external_validation" if reproduced else "raw_scientific_reproduction_failed",
        "rowsLoaded": len(rows),
        "receipts": receipts,
        "expected": EXPECTED,
        "observed": metrics,
        "exactRawScientificReproductionSucceeded": reproduced,
        "noExternalValidationClaimed": True,
        "scope": "four public Gaia EDR3 RA slices, dec -30..30, G 14..20, ordered by source_id, top 40 rows per slice",
    }
    out = Path("standalone_reproduction_result.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf8")
    table = [
        "# Reproduction Result Table",
        "",
        f"Exact raw scientific reproduction succeeded: `{str(reproduced).lower()}`.",
        "",
        "| Metric | Expected | Observed | Match |",
        "| --- | ---: | ---: | --- |",
        f"| measuredOutcome | {EXPECTED['measuredOutcome']} | {metrics['measuredOutcome']} | {str(EXPECTED['measuredOutcome'] == metrics['measuredOutcome']).lower()} |",
        f"| residualMagnitude | {EXPECTED['residualMagnitude']} | {metrics['residualMagnitude']} | {str(EXPECTED['residualMagnitude'] == metrics['residualMagnitude']).lower()} |",
    ]
    for name, expected in EXPECTED["baselines"].items():
        observed = metrics["baselines"][name]
        table.append(f"| {name} | {expected} | {observed} | {str(expected == observed).lower()} |")
    table.append("")
    table.append("No external validation or broad astrophysical interpretation is claimed by this replay.")
    Path("REPRODUCTION_RESULT_TABLE.md").write_text("\n".join(table) + "\n", encoding="utf8")
    print(json.dumps(result, indent=2))
    return 0 if reproduced else 1

if __name__ == "__main__":
    sys.exit(main())
