# Target 2: UCI Optical Recognition of Handwritten Digits


## Data Loaded

- Rows: 5620
- Features: 64
- Classes: 10
- Target column: `class`
- Missing cells: 0
- Duplicate full rows: 0
- Duplicate feature rows: 0
- Class distribution: {"0": 554, "1": 571, "2": 557, "3": 572, "4": 568, "5": 558, "6": 558, "7": 566, "8": 554, "9": 562}

## Schema And Provenance

`schema_provenance_auditor` ran successfully: true.

Compared with ordinary pandas checks, the schema tool did not create a unique raw discovery claim for this target. Its decision label was `dominated_by_simple_baseline` because pandas `shape`, `isna`, `duplicated`, `describe`, and `value_counts` explained the base finding. The tool still added source-hash-bound packaging and a repeatable evidence card.

## Baselines

| Model | Accuracy | Macro-F1 | Weakest class | Weakest-class F1 |
| --- | --- | --- | --- | --- |
| Dummy most frequent | 0.1014 | 0.0184 | 0 | 0.0000 |
| Dummy stratified | 0.0991 | 0.0985 | 5 | 0.0743 |
| LogisticRegression | 0.9703 | 0.9704 | 8 | 0.9373 |
| RandomForest | 0.9864 | 0.9864 | 9 | 0.9612 |

Logistic top confusion summary: 8->1 (6), 1->8 (3), 4->8 (3).

## Metric Stress

- `metric_stress_validator` ran successfully: true.
- Logistic macro-F1 range across seeds: 0.9675 to 0.9704.
- Non-stratified minus stratified macro-F1 delta: -0.0094.
- Accuracy minus macro-F1: -0.0000.
- Simple baseline explains result: false.
- Metric tool decision label: `anti_hype_support_only`.

The metric tool added anti-hype controls and a standardized shuffled-label/dummy-control package. It did not replace normal sklearn metrics.

## Extension Attempts

| Extension | Baseline | Baseline macro-F1 | Extension macro-F1 | Delta | Decision |
| --- | --- | --- | --- | --- | --- |
| class_weight_balanced_logistic_regression | logistic_regression | 0.9704 | 0.9704 | -0.0000 | downgraded_no_material_macro_f1_gain |
| class_weight_balanced_random_forest | random_forest | 0.9864 | 0.9864 | 0.0000 | downgraded_no_material_macro_f1_gain |

## Hard Question Answer

For this target, the custom toolchain mostly revealed process-level value beyond pandas/sklearn: hash-bound schema evidence, explicit negative controls, split/seed stress, and public limitation wording. It did not reveal a strong unique raw finding that ordinary pandas/sklearn could not compute.
