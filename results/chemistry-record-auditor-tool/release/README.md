# Molecular Record Auditor for Chemistry-Style Dataset Quality

A safe open-source data-quality method for auditing chemistry-style molecular property records.

## What The Tool Does

`mol-record-auditor` audits a toy molecular-property dataset for duplicate compound
records, Celsius/Kelvin inconsistencies, suspicious outliers, conflicting
property values, weak provenance, malformed fields, and dataset-level
reliability.

External supporting package: `pint`, provisioned under Sovryn policy for unit
normalization.

Node Alpha executed the prototype through an explicit sandbox-local validation
profile after checking the stronger container-netoff profile. No silent fallback
is claimed.

## Issues Detected In The Toy Dataset

```json
[
  {
    "compound": "acetone",
    "issueType": "conflicting_property_values",
    "spreadK": 942.95
  },
  {
    "compound": "acetone",
    "issueType": "suspicious_property_outlier",
    "records": [
      "propanone"
    ]
  },
  {
    "compound": "acetone",
    "issueType": "weak_provenance",
    "records": [
      "propanone"
    ]
  }
]
```

## Safety Scope

This is not chemical synthesis, not wet-lab guidance, not chemical discovery,
not drug design, and not hazardous-substance optimization.

## Disclaimer

This is an autonomous open-research artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion. It was published automatically after automated policy gates and still requires human interpretation before use.
