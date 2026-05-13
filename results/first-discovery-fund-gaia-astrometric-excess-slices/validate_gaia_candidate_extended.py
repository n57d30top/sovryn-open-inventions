#!/usr/bin/env python3
"""Additional public validation pressure for the Gaia candidate.

This script is intentionally stricter than the exact replay script. It keeps
the original bounded claim unchanged, then adds fresh public Gaia TAP panels
that reviewers can inspect:

- the original equatorial panel used for exact replay,
- north and south declination holdout panels,
- a brighter-magnitude control panel,
- additional rival proxies (RUWE and visibility periods).

The output is a review supplement, not external validation and not a stronger
scientific claim.
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

CANDIDATE_ID = "DISCOVERY-LIFT-INSIGHT-HARD-GEN-GAIA-ASTROMETRIC-EXCESS-SIGNIFICANCE-GE-0F9E75E885B6"

EXPECTED_PRIMARY = {
    "measuredOutcome": 0.4256,
    "residualMagnitude": 0.1343,
    "baselines": {
        "phot_g_mean_magnitude_correlation": 0.1372,
        "bp_rp_color_correlation": 0.1126,
        "single_sky_slice_dominance_control": 0.5075,
    },
}

RA_SLICES = [
    ("ra_000_090", 0, 90),
    ("ra_090_180", 90, 180),
    ("ra_180_270", 180, 270),
    ("ra_270_360", 270, 360),
]

PANELS = [
    {
        "panelId": "primary_equatorial_replay",
        "purpose": "exact replay panel",
        "decMin": -30,
        "decMax": 30,
        "gMin": 14,
        "gMax": 20,
        "limit": 40,
    },
    {
        "panelId": "north_declination_holdout",
        "purpose": "independent declination holdout",
        "decMin": 30,
        "decMax": 60,
        "gMin": 14,
        "gMax": 20,
        "limit": 20,
    },
    {
        "panelId": "south_declination_holdout",
        "purpose": "independent declination holdout",
        "decMin": -60,
        "decMax": -30,
        "gMin": 14,
        "gMax": 20,
        "limit": 20,
    },
    {
        "panelId": "bright_magnitude_control",
        "purpose": "negative/control magnitude slice",
        "decMin": -30,
        "decMax": 30,
        "gMin": 12,
        "gMax": 14,
        "limit": 20,
    },
]


def tap_url(panel, min_ra, max_ra):
    limit = panel.get("limit", 20)
    query = " ".join(
        [
            f"select top {limit} source_id,ra,dec,phot_g_mean_mag,bp_rp,",
            "astrometric_excess_noise,ruwe,visibility_periods_used",
            "from gaiaedr3.gaia_source",
            f"where ra >= {min_ra} and ra < {max_ra}",
            f"and dec > {panel['decMin']} and dec < {panel['decMax']}",
            f"and phot_g_mean_mag between {panel['gMin']} and {panel['gMax']}",
            "and bp_rp is not null",
            "and astrometric_excess_noise is not null",
            "order by source_id",
        ]
    )
    encoded = urllib.parse.quote(query)
    return (
        "https://gea.esac.esa.int/tap-server/tap/sync?"
        f"REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY={encoded}"
    )


def fetch_text(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "sovryn-open-inventions-gaia-review/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        payload = response.read()
        text = payload.decode("utf-8")
        return text, {
            "status": response.status,
            "contentLength": len(text),
            "sourceHash": hashlib.sha256(payload).hexdigest(),
        }


def source_row_snapshot_path(panel_id, slice_id):
    return (
        Path("raw-reproduction-bundle")
        / "extended-source-rows"
        / panel_id
        / f"{slice_id}.csv"
    )


def load_or_fetch_text(panel_id, slice_id, url):
    snapshot = source_row_snapshot_path(panel_id, slice_id)
    if snapshot.exists():
        payload = snapshot.read_bytes()
        return payload.decode("utf-8"), {
            "status": "local_snapshot",
            "contentLength": len(payload),
            "sourceHash": hashlib.sha256(payload).hexdigest(),
            "snapshotPath": str(snapshot),
            "replaySource": "public_corpus_extended_source_row_snapshot",
        }
    text, receipt = fetch_text(url)
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    snapshot.write_text(text, encoding="utf8")
    receipt["snapshotPath"] = str(snapshot)
    receipt["replaySource"] = "live_public_gaia_tap_then_public_snapshot"
    return text, receipt


def parse_rows(text, panel_id, slice_id):
    rows = []

    def optional_float(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return None

    for rec in csv.DictReader(io.StringIO(text)):
        try:
            rows.append(
                {
                    "sourceId": rec["source_id"],
                    "ra": float(rec["ra"]),
                    "dec": float(rec["dec"]),
                    "g": float(rec["phot_g_mean_mag"]),
                    "color": float(rec["bp_rp"]),
                    "excess": float(rec["astrometric_excess_noise"]),
                    "ruwe": optional_float(rec.get("ruwe")),
                    "visibilityPeriods": optional_float(rec.get("visibility_periods_used")),
                    "panelId": panel_id,
                    "sliceId": slice_id,
                }
            )
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


def pearson_optional(rows, left_name, right_name):
    pairs = [
        (row[left_name], row[right_name])
        for row in rows
        if row.get(left_name) is not None and row.get(right_name) is not None
    ]
    if len(pairs) < 2:
        return 0.0, len(pairs)
    left = [pair[0] for pair in pairs]
    right = [pair[1] for pair in pairs]
    return pearson(left, right), len(pairs)


def round_metric(value):
    return round(value * 10000) / 10000


def solve_linear_system(matrix, vector):
    n = len(vector)
    augmented = [list(matrix[i]) + [vector[i]] for i in range(n)]
    for column in range(n):
        pivot = max(range(column, n), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-12:
            return None
        if pivot != column:
            augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [value / divisor for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                value - factor * augmented[column][index]
                for index, value in enumerate(augmented[row])
            ]
    return [augmented[row][-1] for row in range(n)]


def linear_residual_control(rows, feature_names):
    usable = [
        row
        for row in rows
        if all(row.get(name) is not None for name in feature_names)
        and row.get("excess") is not None
    ]
    feature_count = len(feature_names) + 1
    if len(usable) <= feature_count:
        return {
            "featureNames": feature_names,
            "rowCount": len(usable),
            "fitSucceeded": False,
            "residualMagnitude": None,
            "crossSliceSupport": False,
            "counterexampleCollapsed": True,
            "sliceMeans": [],
        }
    normal = [[0.0 for _ in range(feature_count)] for _ in range(feature_count)]
    target = [0.0 for _ in range(feature_count)]
    for row in usable:
        features = [1.0] + [float(row[name]) for name in feature_names]
        y = float(row["excess"])
        for i in range(feature_count):
            target[i] += features[i] * y
            for j in range(feature_count):
                normal[i][j] += features[i] * features[j]
    coefficients = solve_linear_system(normal, target)
    if coefficients is None:
        return {
            "featureNames": feature_names,
            "rowCount": len(usable),
            "fitSucceeded": False,
            "residualMagnitude": None,
            "crossSliceSupport": False,
            "counterexampleCollapsed": True,
            "sliceMeans": [],
        }
    residuals = []
    for row in usable:
        features = [1.0] + [float(row[name]) for name in feature_names]
        predicted = sum(coefficient * feature for coefficient, feature in zip(coefficients, features))
        residuals.append({**row, "adjustedResidual": row["excess"] - predicted})
    slice_means = []
    for slice_id, _, _ in RA_SLICES:
        values = [
            row["adjustedResidual"]
            for row in residuals
            if row["sliceId"] == slice_id
        ]
        slice_means.append(
            {
                "sliceId": slice_id,
                "adjustedResidualMean": mean(values),
                "rowCount": len(values),
            }
        )
    residual_magnitude = round_metric(
        mean([abs(row["adjustedResidualMean"]) for row in slice_means])
    )
    positive_slices = sum(
        1 for row in slice_means if row["adjustedResidualMean"] > 0.05
    )
    negative_slices = sum(
        1 for row in slice_means if row["adjustedResidualMean"] < -0.05
    )
    cross_slice_support = max(positive_slices, negative_slices) >= 2
    return {
        "featureNames": feature_names,
        "rowCount": len(usable),
        "fitSucceeded": True,
        "coefficients": [round_metric(value) for value in coefficients],
        "residualMagnitude": residual_magnitude,
        "crossSliceSupport": cross_slice_support,
        "counterexampleCollapsed": not cross_slice_support or residual_magnitude < 0.05,
        "sliceMeans": slice_means,
    }


def expected_excess(row):
    return 0.08 + max(0, row["g"] - 16) * 0.1 + abs(row["color"] - 1.2) * 0.08


def score_panel(rows):
    residuals = [{**row, "residual": row["excess"] - expected_excess(row)} for row in rows]
    slice_means = []
    for slice_id, _, _ in RA_SLICES:
        values = [row["residual"] for row in residuals if row["sliceId"] == slice_id]
        slice_means.append({"sliceId": slice_id, "residualMean": mean(values), "rowCount": len(values)})

    residual_abs_sum = sum(abs(row["residualMean"]) for row in slice_means)
    single_slice_dominance = 1.0 if residual_abs_sum == 0 else max(
        abs(row["residualMean"]) for row in slice_means
    ) / residual_abs_sum
    positive_slices = sum(1 for row in slice_means if row["residualMean"] > 0.05)
    negative_slices = sum(1 for row in slice_means if row["residualMean"] < -0.05)

    ruwe_correlation, ruwe_pair_count = pearson_optional(rows, "ruwe", "excess")
    visibility_correlation, visibility_pair_count = pearson_optional(rows, "visibilityPeriods", "excess")
    baselines = {
        "phot_g_mean_magnitude_correlation": round_metric(abs(pearson([row["g"] for row in rows], [row["excess"] for row in rows]))),
        "bp_rp_color_correlation": round_metric(abs(pearson([row["color"] for row in rows], [row["excess"] for row in rows]))),
        "ruwe_correlation_rival": round_metric(abs(ruwe_correlation)),
        "visibility_periods_correlation_rival": round_metric(abs(visibility_correlation)),
        "single_sky_slice_dominance_control": round_metric(single_slice_dominance),
    }
    strongest_rival = max(
        ["phot_g_mean_magnitude_correlation", "bp_rp_color_correlation", "ruwe_correlation_rival", "visibility_periods_correlation_rival"],
        key=lambda name: baselines[name],
    )
    adjusted_controls = {
        "g_color": linear_residual_control(rows, ["g", "color"]),
        "g_color_ruwe": linear_residual_control(rows, ["g", "color", "ruwe"]),
        "g_color_ruwe_visibility": linear_residual_control(
            rows,
            ["g", "color", "ruwe", "visibilityPeriods"],
        ),
    }
    return {
        "rowCount": len(rows),
        "measuredOutcome": round_metric(mean([row["excess"] for row in rows])),
        "residualMagnitude": round_metric(mean([abs(row["residualMean"]) for row in slice_means])),
        "baselines": baselines,
        "rivalPairCounts": {
            "ruwe": ruwe_pair_count,
            "visibilityPeriods": visibility_pair_count,
        },
        "strongestRival": strongest_rival,
        "strongestRivalScore": baselines[strongest_rival],
        "sliceMeans": slice_means,
        "adjustedControls": adjusted_controls,
        "crossSliceSupport": max(positive_slices, negative_slices) >= 2,
        "counterexampleCollapsed": not (max(positive_slices, negative_slices) >= 2) or single_slice_dominance > 0.85,
    }


def primary_reproduced(metrics):
    return (
        metrics["measuredOutcome"] == EXPECTED_PRIMARY["measuredOutcome"]
        and metrics["residualMagnitude"] == EXPECTED_PRIMARY["residualMagnitude"]
        and metrics["baselines"]["phot_g_mean_magnitude_correlation"]
        == EXPECTED_PRIMARY["baselines"]["phot_g_mean_magnitude_correlation"]
        and metrics["baselines"]["bp_rp_color_correlation"]
        == EXPECTED_PRIMARY["baselines"]["bp_rp_color_correlation"]
        and metrics["baselines"]["single_sky_slice_dominance_control"]
        == EXPECTED_PRIMARY["baselines"]["single_sky_slice_dominance_control"]
    )


def classify(panel_results):
    primary = panel_results["primary_equatorial_replay"]["metrics"]
    holdouts = [
        panel_results["north_declination_holdout"]["metrics"],
        panel_results["south_declination_holdout"]["metrics"],
    ]
    exact = primary_reproduced(primary)
    holdout_support_count = sum(
        1
        for metrics in holdouts
        if metrics["residualMagnitude"] >= 0.05
        and metrics["crossSliceSupport"]
        and not metrics["counterexampleCollapsed"]
    )
    ruwe_rival_strong = any(
        result["metrics"]["baselines"]["ruwe_correlation_rival"] >= 0.5
        for result in panel_results.values()
    )
    primary_ruwe_adjusted = primary["adjustedControls"]["g_color_ruwe"]
    ruwe_rival_explains_primary_signal = (
        primary_ruwe_adjusted["fitSucceeded"]
        and (
            primary_ruwe_adjusted["residualMagnitude"] < 0.05
            or not primary_ruwe_adjusted["crossSliceSupport"]
        )
    )
    holdout_supported = holdout_support_count >= 1
    if not exact:
        status = "primary_replay_failed"
    elif ruwe_rival_explains_primary_signal:
        status = "extended_validation_rival_explained_signal"
    elif ruwe_rival_strong and not holdout_supported:
        status = "extended_validation_major_rival_and_holdout_caveats"
    elif ruwe_rival_strong:
        status = "extended_validation_major_rival_caveat"
    elif not holdout_supported:
        status = "extended_validation_holdout_weak"
    else:
        status = "extended_validation_supportive_with_caveats"
    return {
        "status": status,
        "primaryExactReplaySucceeded": exact,
        "holdoutSupportedPanelCount": holdout_support_count,
        "ruweRivalStrong": ruwe_rival_strong,
        "ruweRivalExplainsPrimarySignal": ruwe_rival_explains_primary_signal,
        "primaryRuweAdjustedResidualMagnitude": primary_ruwe_adjusted[
            "residualMagnitude"
        ],
        "primaryRuweAdjustedCrossSliceSupport": primary_ruwe_adjusted[
            "crossSliceSupport"
        ],
        "noExternalValidationClaimed": True,
        "claimStrengthened": False,
    }


def write_markdown(result):
    lines = [
        "# Extended Gaia Validation Supplement",
        "",
        "This supplement adds fresh public Gaia TAP panels and stronger rival controls. It does not strengthen the bounded claim and does not claim external validation.",
        "",
        f"Overall status: `{result['decision']['status']}`.",
        "",
        "| Panel | Purpose | Rows | Measured outcome | Residual magnitude | Strongest rival | Strongest rival score | Cross-slice support | Counterexample collapsed |",
        "| --- | --- | ---: | ---: | ---: | --- | ---: | --- | --- |",
    ]
    for panel in PANELS:
        panel_result = result["panels"][panel["panelId"]]
        metrics = panel_result["metrics"]
        lines.append(
            "| "
            + " | ".join(
                [
                    panel["panelId"],
                    panel["purpose"],
                    str(metrics["rowCount"]),
                    str(metrics["measuredOutcome"]),
                    str(metrics["residualMagnitude"]),
                    metrics["strongestRival"],
                    str(metrics["strongestRivalScore"]),
                    str(metrics["crossSliceSupport"]).lower(),
                    str(metrics["counterexampleCollapsed"]).lower(),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- The original exact replay remains the authoritative bounded package claim.",
            "- RUWE is treated as a strong catalog-quality rival proxy, not as support for a new astrophysical mechanism.",
            f"- On the primary panel, residual magnitude after a linear G/color/RUWE control is `{result['decision']['primaryRuweAdjustedResidualMagnitude']}` and cross-slice support is `{str(result['decision']['primaryRuweAdjustedCrossSliceSupport']).lower()}`.",
            "- If the RUWE-adjusted residual loses cross-slice support or falls below the nontrivial threshold, this public package no longer counts as a discovery-scored candidate.",
            "- Holdout panels are independent public declination slices, but they are still Gaia-internal and do not equal outside expert validation.",
            "- Any strong RUWE/catalo-quality rival should downgrade scientific interpretation unless an external reviewer accepts the narrower residual claim.",
        ]
    )
    Path("EXTENDED_VALIDATION_TABLE.md").write_text("\n".join(lines) + "\n", encoding="utf8")
    rival_lines = [
        "# RUWE Rival Closure Results",
        "",
        "This file reports the strongest public catalog-quality rival pressure added after raw scientific replay. It does not create a new candidate or strengthen the original claim.",
        "",
        f"- Overall status: `{result['decision']['status']}`",
        f"- RUWE rival explains primary signal: `{str(result['decision']['ruweRivalExplainsPrimarySignal']).lower()}`",
        f"- Primary G/color/RUWE adjusted residual magnitude: `{result['decision']['primaryRuweAdjustedResidualMagnitude']}`",
        f"- Primary G/color/RUWE adjusted cross-slice support: `{str(result['decision']['primaryRuweAdjustedCrossSliceSupport']).lower()}`",
        "",
        "## Primary Adjusted Controls",
        "",
        "| Control | Rows | Residual magnitude | Cross-slice support | Counterexample collapsed |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    primary_controls = result["panels"]["primary_equatorial_replay"]["metrics"][
        "adjustedControls"
    ]
    for control_name, control in primary_controls.items():
        rival_lines.append(
            f"| {control_name} | {control['rowCount']} | {control['residualMagnitude']} | {str(control['crossSliceSupport']).lower()} | {str(control['counterexampleCollapsed']).lower()} |"
        )
    rival_lines.extend(
        [
            "",
            "## Decision",
            "",
            "The public raw replay remains reproducible, but the RUWE-adjusted control collapses the cross-slice residual support. The package should therefore be treated as not discovery-scored until a new candidate or narrowed claim survives this catalog-quality rival.",
        ]
    )
    Path("RUWE_RIVAL_CLOSURE_RESULTS.md").write_text(
        "\n".join(rival_lines) + "\n",
        encoding="utf8",
    )
    Path("ruwe_rival_closure_result.json").write_text(
        json.dumps(
            {
                "kind": "gaia_ruwe_rival_closure_result",
                "candidateId": CANDIDATE_ID,
                "status": result["decision"]["status"],
                "ruweRivalExplainsPrimarySignal": result["decision"][
                    "ruweRivalExplainsPrimarySignal"
                ],
                "primaryAdjustedControls": primary_controls,
                "noExternalValidationClaimed": True,
                "claimStrengthened": False,
            },
            indent=2,
        )
        + "\n",
        encoding="utf8",
    )


def main():
    all_results = {}
    all_receipts = []
    for panel in PANELS:
        rows = []
        panel_receipts = []
        for slice_id, min_ra, max_ra in RA_SLICES:
            url = tap_url(panel, min_ra, max_ra)
            print(f"loading {panel['panelId']} {slice_id}", flush=True)
            text, receipt = load_or_fetch_text(panel["panelId"], slice_id, url)
            receipt.update(
                {
                    "panelId": panel["panelId"],
                    "sliceId": slice_id,
                    "sourceUrl": url,
                }
            )
            panel_receipts.append(receipt)
            all_receipts.append(receipt)
            rows.extend(parse_rows(text, panel["panelId"], slice_id))
        all_results[panel["panelId"]] = {
            "purpose": panel["purpose"],
            "panel": panel,
            "receipts": panel_receipts,
            "metrics": score_panel(rows),
        }

    result = {
        "kind": "gaia_extended_validation_result",
        "candidateId": CANDIDATE_ID,
        "panels": all_results,
        "receipts": all_receipts,
        "expectedPrimary": EXPECTED_PRIMARY,
        "decision": classify(all_results),
        "scope": "public Gaia EDR3 TAP panels only; no external validation or broad astrophysical law is claimed",
    }
    Path("extended_validation_result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf8")
    write_markdown(result)
    print(json.dumps(result["decision"], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
