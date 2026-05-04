from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

REQUIRED = ["timestamp", "kwh", "outdoorTemperatureC", "season", "householdId", "source"]


def parse_time(value):
    if not isinstance(value, str) or not value:
        raise ValueError("timestamp must be a non-empty string")
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def validate(records):
    for idx, record in enumerate(records):
        for field in REQUIRED:
            if field not in record or record[field] in ("", None):
                raise ValueError(f"record {idx} missing required field {field}")
        parse_time(record["timestamp"])
        if not isinstance(record["kwh"], (int, float)):
            raise ValueError(f"record {idx} kwh must be numeric")


def audit(records):
    frame = pd.DataFrame(records)
    validate(records)
    enriched = []
    seen = {}
    issues = []
    for record in records:
        parsed = parse_time(record["timestamp"])
        item = dict(record)
        item["_parsed"] = parsed
        item["_day"] = parsed.date().isoformat()
        enriched.append(item)
        key = (record["householdId"], record["timestamp"])
        seen.setdefault(key, []).append(record)
    for key, values in sorted(seen.items()):
        if len(values) > 1:
            issues.append({
                "issueType": "duplicate_timestamp",
                "householdId": key[0],
                "timestamp": key[1],
                "description": "Duplicate timestamp for anonymized toy household.",
                "severity": "medium",
            })
    by_household = {}
    for item in enriched:
        by_household.setdefault(item["householdId"], []).append(item)
    for household, values in sorted(by_household.items()):
        values.sort(key=lambda item: item["_parsed"])
        for left, right in zip(values, values[1:]):
            gap_days = (right["_parsed"] - left["_parsed"]).days
            if gap_days > 1 and left["season"] == right["season"]:
                issues.append({
                    "issueType": "missing_interval",
                    "householdId": household,
                    "timestamp": right["timestamp"],
                    "description": f"Missing {gap_days - 1} daily interval(s) before {right['timestamp']}.",
                    "severity": "medium",
                })
    baselines = {}
    for item in enriched:
        key = (item["householdId"], item["season"])
        baselines.setdefault(key, []).append(float(item["kwh"]))
    baseline_summary = {
        f"{household}:{season}": round(sum(values) / len(values), 3)
        for (household, season), values in sorted(baselines.items())
    }
    for item in enriched:
        baseline = baseline_summary[f"{item['householdId']}:{item['season']}"]
        expected = baseline + max(0.0, (18 - float(item["outdoorTemperatureC"])) * 0.15)
        ratio = float(item["kwh"]) / max(expected, 0.1)
        if ratio >= 1.8 or float(item["kwh"]) >= 30:
            issues.append({
                "issueType": "high_usage_spike",
                "householdId": item["householdId"],
                "timestamp": item["timestamp"],
                "description": "Usage is high relative to seasonal/weather-normalized expectation.",
                "severity": "high",
                "score": round(ratio, 3),
            })
        if item["season"] == "summer" and float(item["outdoorTemperatureC"]) >= 20 and float(item["kwh"]) >= 20:
            issues.append({
                "issueType": "weather_normalized_anomaly",
                "householdId": item["householdId"],
                "timestamp": item["timestamp"],
                "description": "Warm-weather record has unusually high usage for the toy baseline.",
                "severity": "medium",
            })
        if "unknown" in str(item["source"]) or "weak" in str(item["source"]):
            issues.append({
                "issueType": "weak_provenance",
                "householdId": item["householdId"],
                "timestamp": item["timestamp"],
                "description": "Record source is weak or unknown.",
                "severity": "medium",
            })
    reliability = max(0, 100 - len(issues) * 7)
    return {
        "kind": "energy_record_auditor_output",
        "recordCount": len(records),
        "externalToolEvidence": {
            "package": "pandas",
            "version": getattr(pd, "__version__", "unknown"),
            "usedForTabularValidation": hasattr(frame, "records") or frame is not None,
        },
        "baselineSummary": baseline_summary,
        "datasetIssues": sorted(issues, key=lambda item: (item["issueType"], item.get("timestamp", ""))),
        "datasetReliabilityScore": reliability,
        "safetyScope": "synthetic anonymized toy records only; no private smart-meter data",
    }


def main(argv):
    if len(argv) != 3:
        raise SystemExit("usage: energy_record_auditor <input> <output>")
    data = json.loads(Path(argv[1]).read_text())
    records = data.get("records")
    if not isinstance(records, list):
        raise ValueError("input must contain records list")
    output = audit(records)
    Path(argv[2]).write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    Path("ENERGY_AUDIT_REPORT.md").write_text(render_report(output), encoding="utf8")
    Path("TOOL_LIMITATIONS.md").write_text(render_limitations(), encoding="utf8")


def render_report(output):
    lines = ["# Energy Audit Report", "", f"Dataset reliability score: {output['datasetReliabilityScore']}", ""]
    for issue in output["datasetIssues"]:
        lines.append(f"- {issue['issueType']}: {issue['description']}")
    return "\n".join(lines) + "\n"


def render_limitations():
    return """# Tool Limitations

This is a lightweight toy-dataset auditor. It is not a surveillance system,
not a private smart-meter analytics product, not an energy-market trading tool,
and not a legal patentability or freedom-to-operate opinion.
"""


if __name__ == "__main__":
    main(sys.argv)
