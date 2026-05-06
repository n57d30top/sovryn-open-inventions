# Reproduce

1. Create an isolated Python environment.
2. Install `pandas`, `scikit-learn`, and `ucimlrepo`.
3. Fetch UCI IDs 545, 80, 149, 53, and 109 with `ucimlrepo`.
4. For each completed target, export a headered CSV and a headerless CSV.
5. Run `schema_provenance_auditor` on the headered CSV.
6. Run `metric_stress_validator` on the headerless CSV with the target column at the final index.
7. Run DummyClassifier, LogisticRegression, and RandomForest baselines on a 70/30 split with seed 42.
8. Run shuffled-label, seed/split, stratified/non-stratified, and per-class stress checks.
9. Run class-weight extension attempts and compare macro-F1 against the simple baseline.
10. Replay at least two targets with a fresh seed or split, and replay at least two target runs in a container with network mode `none`.

The public package includes structured evidence JSON but intentionally omits private execution paths and unstructured run output.
