# Dataset

- Study: chemistry-data-quality-does-explicit-low-confidence-identifier-equivalence-reduce-overconfident-
- Dataset kind: synthetic_chemistry_records
- Dataset count: 3
- Seeds: 1, 2, 3
- Privacy scope: Synthetic toy records only; no synthesis guidance, hazardous substance optimization, lab handling, or chemical design.

## Schema

- recordId
- name
- smiles
- property
- value
- unit
- source
- expectedIssue

## Required Patterns

- Celsius/Kelvin unit pairs
- limited toy identifier equivalence
- known inconsistent property values
- weak provenance records
- normal consistent duplicates

## Limitations

- Identifier equivalence is a limited toy map, not general SMILES canonicalization.
- No RDKit or OpenBabel claim is made.
- Future public-data studies must source-card concrete non-sensitive chemistry datasets.
