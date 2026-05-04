# mol-record-auditor

`mol-record-auditor` audits a toy chemistry-style molecular property dataset
for duplicate records, Celsius/Kelvin inconsistencies, suspicious outliers,
weak provenance, malformed fields, and reproducible quality scores.

It uses `pint` for unit normalization when provisioned under Sovryn policy.
The identifier map is fixed to the toy dataset and marked low-confidence. This
is not RDKit, OpenBabel, or a general SMILES canonicalization tool.
