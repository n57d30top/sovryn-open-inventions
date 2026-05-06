# Claim Attacks and Downgrades

Batch 8 attacked the Batch 7 tool claims.

- Claim: `schema_provenance_auditor` is a reusable candidate. Result: narrowed. Bike day/hour files showed that related files can have intentionally different schemas.
- Claim: `metric_stress_validator` is only narrow but useful. Result: promoted. Sonar and Spambase confirmed the value of dummy and shuffled-label controls.
- Claim: `pytest_repro_summary` is useful but limited. Result: preserved and narrowed. iniconfig passed, while pyproject-hooks failed in the minimal runtime environment.

The program therefore did not defend prior claims by default. It converted new evidence into promotion, narrowing, and failure cases.
