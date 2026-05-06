# Target 1: UCI Rice Cammeo/Osmancik


## Data Loaded

- Rows: 3810
- Features: 7
- Classes: 2
- Target column: `Class`
- Missing cells: 0
- Duplicate full rows: 0
- Duplicate feature rows: 0
- Class distribution: {"Cammeo": 1630, "Osmancik": 2180}

## Schema And Provenance

`schema_provenance_auditor` ran successfully: true.

Compared with ordinary pandas checks, the schema tool did not create a unique raw discovery claim for this target. Its decision label was `dominated_by_simple_baseline` because pandas `shape`, `isna`, `duplicated`, `describe`, and `value_counts` explained the base finding. The tool still added source-hash-bound packaging and a repeatable evidence card.

## Baselines

| Model | Accuracy | Macro-F1 | Weakest class | Weakest-class F1 |
| --- | --- | --- | --- | --- |
| Dummy most frequent | 0.5722 | 0.3639 | Cammeo | 0.0000 |
| Dummy stratified | 0.4908 | 0.4800 | Cammeo | 0.4049 |
| LogisticRegression | 0.9195 | 0.9174 | Cammeo | 0.9042 |
| RandomForest | 0.9265 | 0.9245 | Cammeo | 0.9121 |

Logistic top confusion summary: Cammeo->Osmancik (55), Osmancik->Cammeo (37).

## Metric Stress

- `metric_stress_validator` ran successfully: true.
- Logistic macro-F1 range across seeds: 0.9174 to 0.9364.
- Non-stratified minus stratified macro-F1 delta: 0.0118.
- Accuracy minus macro-F1: 0.0021.
- Simple baseline explains result: false.
- Metric tool decision label: `anti_hype_support_only`.

The metric tool added anti-hype controls and a standardized shuffled-label/dummy-control package. It did not replace normal sklearn metrics.

## Extension Attempts

| Extension | Baseline | Baseline macro-F1 | Extension macro-F1 | Delta | Decision |
| --- | --- | --- | --- | --- | --- |
| class_weight_balanced_logistic_regression | logistic_regression | 0.9174 | 0.9223 | 0.0049 | accepted_measured_macro_f1_gain |
| class_weight_balanced_random_forest | random_forest | 0.9245 | 0.9190 | -0.0054 | rejected_macro_f1_decrease |

## Hard Question Answer

For this target, the custom toolchain mostly revealed process-level value beyond pandas/sklearn: hash-bound schema evidence, explicit negative controls, split/seed stress, and public limitation wording. It did not reveal a strong unique raw finding that ordinary pandas/sklearn could not compute.
