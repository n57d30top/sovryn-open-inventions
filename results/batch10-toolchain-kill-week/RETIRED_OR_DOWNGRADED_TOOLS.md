# Retired Or Downgraded Tools

No tool is fully retired in Batch 10.

Downgraded or narrowed tools:

| Tool | Before attack | After attack | Reason |
| --- | --- | --- | --- |
| `schema_provenance_auditor` | `reusable_for_single_table_tabular_benchmark_screening` after Batch 9 | `narrow_but_useful` | pandas dominates raw single-table discovery; tool value is packaging, hashes, and gates. |
| `metric_stress_validator` | `reusable` after Batch 8 | `reusable_support_tool` | useful for anti-hype controls, but not leakage proof or official protocol reproduction. |
| `pytest_repro_summary` | `narrow_but_useful` | `narrow_but_useful_support_only` | static inventory is not runtime reproduction; dependency failures dominate some targets. |

Retirement watchlist:

- Retire `schema_provenance_auditor` if future runs only duplicate pandas checks without adding public evidence value.
- Retire `pytest_repro_summary` if future runs do not include runtime collection or execution evidence.
