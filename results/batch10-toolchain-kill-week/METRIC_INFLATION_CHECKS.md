# Metric Inflation Checks

Batch 9 Dry Bean metrics:

- Dummy most-frequent accuracy: 0.2605
- Dummy most-frequent macro-F1: 0.0591
- LogisticRegression accuracy: 0.9219
- LogisticRegression macro-F1: 0.9347
- RandomForest accuracy: 0.9197
- RandomForest macro-F1: 0.9322
- Shuffled-label control accuracy: 0.2605
- Shuffled-label control macro-F1: 0.0623

Attack findings:

- Accuracy did not hide a major macro-F1 collapse for LogisticRegression or RandomForest on the primary split.
- Class imbalance exists, but macro-F1 and per-class F1 reporting reduce headline-accuracy inflation risk.
- The `SIRA` class remained the weakest reported LogisticRegression per-class F1 in Batch 9, so per-class reporting was useful.
- Shuffled-label control is useful, but not sufficient to prove absence of leakage.
- LogisticRegression dominance makes the toolchain insight less novel: ordinary linear baseline performance was already strong.

Decision:

Preserve Batch 9 metrics as executed split-family evidence. Do not treat them as official benchmark reproduction, leaderboard-style superiority, or proof that the toolchain discovered a new method.
