# Reproduce

1. Create an isolated Python environment.
2. Install pandas, numpy, and scikit-learn.
3. Download the public UCI archives listed in `TARGET_SELECTION.md`.
4. Load HAR, Shuttle, and Letter.
5. Apply source/protocol splits and same-size stratified random challenger splits.
6. Compute full-row and feature-vector hash overlap across train/test.
7. Check source group/subject/file identifiers only where present.
8. Train DummyClassifier, linear logistic SGD, and RandomForest sanity baselines.
9. Run shuffled-label and duplicate-aware negative controls.
10. Compare leakage-risk findings against prior split-risk findings.
