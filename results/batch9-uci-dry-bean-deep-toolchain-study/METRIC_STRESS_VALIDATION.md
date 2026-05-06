# Metric Stress Validation

Tool used: `metric_stress_validator`.

Required checks performed:

- Shuffled-label control.
- Random-seed variation.
- Stratified vs non-stratified split comparison.
- Macro-F1 vs accuracy comparison.
- Per-class error analysis.
- Simple-baseline explanation check.

Shuffled-label control:

- Accuracy: 0.2605
- Macro-F1: 0.0623

Seed variation:

| Seed | Logistic accuracy | Logistic macro-F1 | Random forest accuracy | Random forest macro-F1 |
| --- | ---: | ---: | ---: | ---: |
| 7 | 0.9241 | 0.9362 | 0.9234 | 0.9343 |
| 42 | 0.9219 | 0.9347 | 0.9197 | 0.9322 |
| 99 | 0.9238 | 0.9373 | 0.9256 | 0.9370 |
| 123 | 0.9224 | 0.9346 | 0.9192 | 0.9306 |
| 2026 | 0.9285 | 0.9382 | 0.9261 | 0.9361 |

Metric-risk interpretation:

- Majority baseline does not explain the result.
- The shuffled-label control stays near the weak majority/control band.
- Accuracy and macro-F1 are close for LogisticRegression and RandomForest, so headline accuracy is not hiding a major macro-F1 collapse.
- `SIRA` has the weakest LogisticRegression per-class F1 among the stronger classes in the primary split, so per-class reporting remains useful.

This supports `metric_stress_validator` as reusable for tabular classification metric stress, while still not proving official benchmark reproduction.
