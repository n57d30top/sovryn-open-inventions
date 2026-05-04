from __future__ import annotations

import json
import math
import sys
from collections import defaultdict
from pathlib import Path

try:
    import pint
except Exception:  # pragma: no cover - exercised when policy blocks provisioning
    pint = None

EQUIVALENCE_MAP = {
    "CCO": ("ethanol", "equivalence_map_low_confidence"),
    "OCC": ("ethanol", "equivalence_map_low_confidence"),
    "CC(=O)C": ("acetone", "equivalence_map_low_confidence"),
    "CC(C)=O": ("acetone", "equivalence_map_low_confidence"),
    "c1ccccc1": ("benzene", "equivalence_map_low_confidence"),
    "C1=CC=CC=C1": ("benzene", "equivalence_map_low_confidence"),
    "O": ("water", "exact_identifier"),
}

REQUIRED_FIELDS = ["name", "smiles", "property", "value", "unit", "source"]
ALLOWED_UNITS = {"C", "K"}
WEAK_SOURCES = {"toy_reference_unknown", "toy_reference_bad", ""}


class AuditError(ValueError):
    pass


def validate_record(record, index):
    missing = [field for field in REQUIRED_FIELDS if field not in record]
    if missing:
        raise AuditError(f"record {index} missing fields: {', '.join(missing)}")
    if not str(record["smiles"]).strip():
        raise AuditError(f"record {index} missing molecule identifier")
    if record["unit"] not in ALLOWED_UNITS:
        raise AuditError(f"record {index} invalid unit: {record['unit']}")
    if not isinstance(record["value"], (int, float)) or not math.isfinite(record["value"]):
        raise AuditError(f"record {index} invalid numeric value")


def canonicalize_identifier(smiles):
    if smiles in EQUIVALENCE_MAP:
        canonical, confidence = EQUIVALENCE_MAP[smiles]
        return canonical, confidence
    return smiles, "unmapped_identifier_low_confidence"


def normalize_temperature(value, unit, target="K"):
    pint_used = pint is not None
    if pint_used:
        ureg = pint.UnitRegistry(autoconvert_offset_to_baseunit=True)
        source_unit = ureg.degC if unit == "C" else ureg.kelvin
        target_unit = ureg.kelvin if target == "K" else ureg.degC
        normalized = ureg.Quantity(float(value), source_unit).to(target_unit).magnitude
    else:
        if unit == target:
            normalized = float(value)
        elif unit == "C" and target == "K":
            normalized = float(value) + 273.15
        elif unit == "K" and target == "C":
            normalized = float(value) - 273.15
        else:
            raise AuditError(f"unsupported conversion: {unit} to {target}")
    return round(float(normalized), 2), pint_used


def audit_records(records):
    groups = defaultdict(list)
    pint_used = False
    malformed = []
    for index, record in enumerate(records):
        try:
            validate_record(record, index)
        except AuditError as exc:
            malformed.append({"index": index, "reason": str(exc)})
            continue
        canonical, confidence = canonicalize_identifier(record["smiles"])
        value_k, used = normalize_temperature(record["value"], record["unit"], "K")
        value_c, used_c = normalize_temperature(record["value"], record["unit"], "C")
        pint_used = pint_used or used or used_c
        groups[(canonical, record["property"])].append(
            {
                "name": record["name"],
                "smiles": record["smiles"],
                "canonicalCompound": canonical,
                "canonicalizationConfidence": confidence,
                "property": record["property"],
                "valueOriginal": record["value"],
                "unitOriginal": record["unit"],
                "valueK": value_k,
                "valueC": value_c,
                "source": record["source"],
                "provenanceScore": 40 if record["source"] in WEAK_SOURCES else 90,
            }
        )
    compounds = []
    dataset_issues = []
    for (compound, prop), items in sorted(groups.items()):
        values_k = [item["valueK"] for item in items]
        spread = round(max(values_k) - min(values_k), 2) if len(values_k) > 1 else 0
        outliers = [item for item in items if item["valueC"] > 250 or item["valueC"] < -100]
        conflicts = spread > 2.0
        weak_provenance = [item for item in items if item["provenanceScore"] < 60]
        quality = 100
        if conflicts:
            quality -= 25
            dataset_issues.append({"compound": compound, "issueType": "conflicting_property_values", "spreadK": spread})
        if outliers:
            quality -= 25
            dataset_issues.append({"compound": compound, "issueType": "suspicious_property_outlier", "records": [item["name"] for item in outliers]})
        if weak_provenance:
            quality -= 15
            dataset_issues.append({"compound": compound, "issueType": "weak_provenance", "records": [item["name"] for item in weak_provenance]})
        if any(item["canonicalizationConfidence"].endswith("low_confidence") for item in items):
            quality -= 5
        compounds.append(
            {
                "compound": compound,
                "property": prop,
                "recordCount": len(items),
                "canonicalizationConfidence": sorted(set(item["canonicalizationConfidence"] for item in items)),
                "normalizedValuesK": values_k,
                "valueSpreadK": spread,
                "consistentAfterUnitNormalization": not conflicts,
                "outlierCount": len(outliers),
                "weakProvenanceCount": len(weak_provenance),
                "qualityScore": max(0, quality),
                "records": items,
            }
        )
    average_quality = round(sum(item["qualityScore"] for item in compounds) / max(1, len(compounds)), 2)
    reliability = max(0, min(100, round(average_quality - len(malformed) * 10, 2)))
    return {
        "tool": "mol-record-auditor",
        "scope": "safe chemistry-style data-quality audit",
        "externalToolEvidence": {
            "package": "pint",
            "usedForUnitNormalization": pint_used,
            "status": "used" if pint_used else "fallback_used",
            "version": getattr(pint, "__version__", "unavailable") if pint is not None else "unavailable",
        },
        "compounds": compounds,
        "malformedRecords": malformed,
        "datasetIssues": sorted(dataset_issues, key=lambda item: (item["compound"], item["issueType"])),
        "datasetReliabilityScore": reliability,
        "limitations": [
            "toy dataset only",
            "limited equivalence map, not general SMILES canonicalization",
            "not RDKit or OpenBabel",
            "data-quality audit only, not synthesis or lab guidance",
        ],
    }


def write_report(output, report_path="AUDIT_REPORT.md"):
    lines = [
        "# Molecular Record Audit Report",
        "",
        f"Dataset reliability score: {output['datasetReliabilityScore']}",
        "",
        "## Issues",
    ]
    for issue in output["datasetIssues"]:
        lines.append(f"- {issue['compound']}: {issue['issueType']}")
    lines.extend(
        [
            "",
            "## Safety Scope",
            "",
            "This is a safe data-quality audit for toy chemistry-style records. It is not chemical synthesis, wet-lab guidance, drug design, or hazardous-substance optimization.",
            "",
            "## Limitations",
            "",
            "- Lightweight toy-dataset auditor.",
            "- Not RDKit/OpenBabel.",
            "- Not a full cheminformatics toolkit.",
            "- Identifier equivalence is limited and low-confidence.",
        ]
    )
    Path(report_path).write_text("\n".join(lines) + "\n", encoding="utf8")


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    input_path = Path(argv[0] if argv else "sample-input.json")
    output_path = Path(argv[1] if len(argv) > 1 else "sample-output.json")
    records = json.loads(input_path.read_text(encoding="utf8"))
    output = audit_records(records)
    if output["malformedRecords"]:
        raise AuditError(output["malformedRecords"][0]["reason"])
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf8")
    write_report(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
