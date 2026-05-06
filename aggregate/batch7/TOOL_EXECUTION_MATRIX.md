# Tool Execution Matrix

| Tool | Target | Executed | External packages/tools | Isolation | Decision |
| --- | --- | --- | --- | --- | --- |
| `schema_provenance_auditor` | UCI Wine Quality red and white CSV datasets | yes | pandas 3.0.2 | network-off sandbox | `keep_as_reusable_candidate` |
| `metric_stress_validator` | UCI Banknote Authentication classification dataset | yes | pandas 3.0.2, scikit-learn 1.8.0 | local isolated environment | `downgraded_to_narrow_but_useful` |
| `pytest_repro_summary` | pytest-dev/pluggy repository test suite | yes | pytest 9.0.1, pluggy editable checkout a469596df2c9f7f9d5219b85c764c644b81896f7 | local isolated environment | `keep_but_mark_dynamic_parametrization_limit` |
