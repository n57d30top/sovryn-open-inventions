# Custom Toolchain Usage

## schema_provenance_auditor

Status before Batch 9: `narrow_but_useful`.

What it found:

- No missing cells.
- 68 duplicate full rows and 68 duplicate feature rows.
- Stable single-table schema with 16 feature columns plus target column.
- No checked sentinel values among -1, 0, 999, and 9999.

What it missed:

- It needed Batch 9 context to identify `Class` as the target.
- It cannot infer official split or leakage risk from a single public table.

Decision: promote for single-table tabular benchmark screening, but keep the target-context limitation.

## metric_stress_validator

Status before Batch 9: `reusable`.

What it found:

- LogisticRegression and RandomForest beat dummy and shuffled-label controls by a large margin.
- Seed/split variation stayed small within the tested split family.
- Accuracy did not inflate the result relative to macro-F1 for the stronger baselines.
- The class-weight extension did not improve macro-F1 on the primary split.

Decision: keep reusable for tabular classification metric stress.

## pytest_repro_summary

Not used. The target is a dataset, not a repository test target.

Hard question answer:

Yes, Sovryn used its self-built schema/provenance and metric-stress tools on one external scientific target. The tools revealed 68 duplicate full/feature rows, no missing/sentinel values, low shuffled-label control performance, stable but not official split-family replay, and that a class-weight extension did not improve macro-F1 on the primary split.
