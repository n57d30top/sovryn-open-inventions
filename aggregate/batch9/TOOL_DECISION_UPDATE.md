# Tool Decision Update

- `schema_provenance_auditor`: promoted from `narrow_but_useful` to `reusable_for_single_table_tabular_benchmark_screening`, with target-context limitations preserved.
- `metric_stress_validator`: kept as `reusable` for tabular classification metric stress.
- `pytest_repro_summary`: unchanged as `narrow_but_useful`; not used because this target did not involve repository tests.

The update is evidence-based: Batch 9 required the schema tool to handle one full single-table tabular benchmark and required the metric tool to expose controls beyond normal sklearn score reporting.
