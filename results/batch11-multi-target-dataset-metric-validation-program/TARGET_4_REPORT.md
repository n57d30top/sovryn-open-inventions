# Target 4: UCI Wine Recognition


## Data Loaded

- Rows: 178
- Features: 13
- Classes: 3
- Target column: `class`
- Missing cells: 0
- Duplicate full rows: 0
- Duplicate feature rows: 0
- Class distribution: {"1": 59, "2": 71, "3": 48}

## Schema And Provenance

`schema_provenance_auditor` ran successfully: true.

Compared with ordinary pandas checks, the schema tool did not create a unique raw discovery claim for this target. Its decision label was `dominated_by_simple_baseline` because pandas `shape`, `isna`, `duplicated`, `describe`, and `value_counts` explained the base finding. The tool still added source-hash-bound packaging and a repeatable evidence card.

## Baselines

| Model | Accuracy | Macro-F1 | Weakest class | Weakest-class F1 |
| --- | --- | --- | --- | --- |
| Dummy most frequent | 0.3889 | 0.1867 | 1 | 0.0000 |
| Dummy stratified | 0.3704 | 0.3480 | 3 | 0.2308 |
| LogisticRegression | 0.9815 | 0.9829 | 1 | 0.9730 |
| RandomForest | 1.0000 | 1.0000 | 1 | 1.0000 |

Logistic top confusion summary: 2->1 (1).

## Metric Stress

- `metric_stress_validator` ran successfully: true.
- Logistic macro-F1 range across seeds: 0.9619 to 1.0000.
- Non-stratified minus stratified macro-F1 delta: -0.0025.
- Accuracy minus macro-F1: -0.0014.
- Simple baseline explains result: false.
- Metric tool decision label: `anti_hype_support_only`.

The metric tool added anti-hype controls and a standardized shuffled-label/dummy-control package. It did not replace normal sklearn metrics.

## Extension Attempts

| Extension | Baseline | Baseline macro-F1 | Extension macro-F1 | Delta | Decision |
| --- | --- | --- | --- | --- | --- |
| class_weight_balanced_logistic_regression | logistic_regression | 0.9829 | 0.9829 | 0.0000 | downgraded_no_material_macro_f1_gain |
| class_weight_balanced_random_forest | random_forest | 1.0000 | 1.0000 | 0.0000 | downgraded_no_material_macro_f1_gain |

## Hard Question Answer

For this target, the custom toolchain mostly revealed process-level value beyond pandas/sklearn: hash-bound schema evidence, explicit negative controls, split/seed stress, and public limitation wording. It did not reveal a strong unique raw finding that ordinary pandas/sklearn could not compute.
