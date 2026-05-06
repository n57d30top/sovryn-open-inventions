# Toolchain Execution Matrix

| Tool or phase | Used | Evidence | Decision |
| --- | --- | --- | --- |
| schema_provenance_auditor | yes | 13611 rows, 68 duplicate full rows, 0 missing cells | promote for single-table tabular benchmark screening |
| metric_stress_validator | yes | shuffled macro-F1=0.0623; logistic macro-F1=0.9347 | keep reusable |
| pytest_repro_summary | no | no repo/test target | not applicable |
| container-netoff replay | yes | network=none; tools replayed={'metric_stress_validator': True, 'schema_provenance_auditor': True} | passed |
