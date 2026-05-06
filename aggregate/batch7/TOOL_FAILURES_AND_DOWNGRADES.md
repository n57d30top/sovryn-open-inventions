# Tool Failures and Downgrades

- `schema_provenance_auditor`: kept as reusable candidate, but duplicate findings are review signals rather than proof of invalid records.
- `metric_stress_validator`: downgraded to `narrow_but_useful` because one deterministic split cannot certify official benchmark validity or absence of leakage.
- `pytest_repro_summary`: kept with a dynamic-parametrization limitation because static definitions and runtime cases can diverge.
