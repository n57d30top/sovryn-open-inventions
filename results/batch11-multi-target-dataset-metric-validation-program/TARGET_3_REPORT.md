# Target 3: UCI Iris


## Data Loaded

- Rows: 150
- Features: 4
- Classes: 3
- Target column: `class`
- Missing cells: 0
- Duplicate full rows: 3
- Duplicate feature rows: 3
- Class distribution: {"Iris-setosa": 50, "Iris-versicolor": 50, "Iris-virginica": 50}

## Schema And Provenance

`schema_provenance_auditor` ran successfully: true.

Compared with ordinary pandas checks, the schema tool did not create a unique raw discovery claim for this target. Its decision label was `packaging_only` because pandas `shape`, `isna`, `duplicated`, `describe`, and `value_counts` explained the base finding. The tool still added source-hash-bound packaging and a repeatable evidence card.

## Baselines

| Model | Accuracy | Macro-F1 | Weakest class | Weakest-class F1 |
| --- | --- | --- | --- | --- |
| Dummy most frequent | 0.3333 | 0.1667 | Iris-versicolor | 0.0000 |
| Dummy stratified | 0.3333 | 0.3229 | Iris-versicolor | 0.2400 |
| LogisticRegression | 0.9111 | 0.9107 | Iris-virginica | 0.8571 |
| RandomForest | 0.8889 | 0.8878 | Iris-virginica | 0.8148 |

Logistic top confusion summary: Iris-virginica->Iris-versicolor (3), Iris-versicolor->Iris-virginica (1).

## Metric Stress

- `metric_stress_validator` ran successfully: true.
- Logistic macro-F1 range across seeds: 0.9107 to 0.9778.
- Non-stratified minus stratified macro-F1 delta: 0.0893.
- Accuracy minus macro-F1: 0.0004.
- Simple baseline explains result: false.
- Metric tool decision label: `anti_hype_support_only`.

The metric tool added anti-hype controls and a standardized shuffled-label/dummy-control package. It did not replace normal sklearn metrics.

## Extension Attempts

| Extension | Baseline | Baseline macro-F1 | Extension macro-F1 | Delta | Decision |
| --- | --- | --- | --- | --- | --- |
| class_weight_balanced_logistic_regression | logistic_regression | 0.9107 | 0.9107 | 0.0000 | downgraded_no_material_macro_f1_gain |
| class_weight_balanced_random_forest | random_forest | 0.8878 | 0.8878 | 0.0000 | downgraded_no_material_macro_f1_gain |

## Hard Question Answer

For this target, the custom toolchain mostly revealed process-level value beyond pandas/sklearn: hash-bound schema evidence, explicit negative controls, split/seed stress, and public limitation wording. It did not reveal a strong unique raw finding that ordinary pandas/sklearn could not compute.
