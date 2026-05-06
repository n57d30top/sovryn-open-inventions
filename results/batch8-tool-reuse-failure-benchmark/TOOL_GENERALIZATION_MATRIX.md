# Tool Generalization Matrix

| Tool | Target 1 | Target 2 | Decision |
| --- | --- | --- | --- |
| `schema_provenance_auditor` | Student Performance: reusable success | Bike Sharing: schema mismatch failure case | narrow_but_useful |
| `metric_stress_validator` | Sonar: reusable with high FP/FN rates | Spambase: reusable success | reusable |
| `pytest_repro_summary` | iniconfig: reusable success | pyproject-hooks: minimal-environment error case | narrow_but_useful |
