# Reproduce

1. Create an isolated Python environment.
2. Install pandas, numpy, and scikit-learn.
3. Download the public sources listed in `CANDIDATE_SELECTION.md`.
4. For the three executed targets, apply the Protocol Card split and the same-size stratified random challenger.
5. Train DummyClassifier, linear logistic SGD, and RandomForest baselines.
6. Record accuracy, macro-F1, weighted-F1, per-class F1, shuffled-label control, and replay divergence.
