# Reproduce

Reproduction outline:

1. Create a fresh Python environment.
2. Install `pandas`, `scikit-learn`, and `ucimlrepo`.
3. Fetch UCI dataset ID 602 with `ucimlrepo.fetch_ucirepo(id=602)`.
4. Concatenate feature and target tables and write two local forms: one CSV with headers and one headerless CSV for the existing metric tool interface.
5. Run the existing Batch 7 `schema_provenance_auditor` on the headered CSV.
6. Run the existing Batch 7 `metric_stress_validator` on the headerless CSV with target column index `-1`.
7. Run DummyClassifier most-frequent, DummyClassifier stratified, LogisticRegression, and RandomForestClassifier on a stratified 70/30 split with seed 42.
8. Run shuffled-label, seed-variation, stratified/non-stratified, and per-class metric stress checks.
9. Attempt class-weight balanced LogisticRegression and compare it against the plain LogisticRegression baseline.
10. Replay with a fresh seed and run a container replay with networking disabled on preloaded public data.

The public result intentionally excludes raw logs and local absolute paths. The evidence JSON files in `evidence/` contain the curated values needed to inspect the run.
