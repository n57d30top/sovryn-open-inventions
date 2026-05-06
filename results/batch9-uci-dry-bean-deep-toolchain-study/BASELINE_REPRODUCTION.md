# Baseline Reproduction

This is a controlled baseline execution, not a full benchmark reproduction. No official train/test split or exact published protocol was reproduced.

Split:

- Test size: 0.30
- Seed: 42
- Stratified: true
- Target: `Class`

| Baseline | Accuracy | Macro-F1 |
| --- | ---: | ---: |
| dummy_most_frequent | 0.2605 | 0.0591 |
| dummy_stratified | 0.1697 | 0.1403 |
| logistic_regression | 0.9219 | 0.9347 |
| random_forest | 0.9197 | 0.9322 |

Per-class F1 for LogisticRegression:

{
  "BARBUNYA": 0.926261319534282,
  "BOMBAY": 1.0,
  "CALI": 0.9408163265306122,
  "DERMASON": 0.9140142517814727,
  "HOROZ": 0.9593777009507347,
  "SEKER": 0.9382113821138212,
  "SIRA": 0.8638906152889994
}

The majority baseline does not explain the linear/tree result. The strongest simple baselines are ordinary sklearn models, not new Sovryn methods.
