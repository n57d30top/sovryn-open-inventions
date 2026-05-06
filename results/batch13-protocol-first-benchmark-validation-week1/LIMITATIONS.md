# Limitations

- No official benchmark reproduction claim is made beyond following source-provided train/test files.
- The source pages and archives do not by themselves resolve every historical benchmark protocol detail.
- The random challenger uses one stratified random split family and seed/stress checks; it is not an exhaustive split search.
- LogisticRegression and RandomForest are practical baselines, not tuned state-of-the-art models.
- `schema_provenance_auditor` is packaging-only here because pandas exposes the same raw missingness and duplicate checks.
- `metric_stress_validator` cannot prove absence of leakage or protocol correctness.
- HAR required nested-archive extraction, but the actual source train/test files were loaded after that extraction.
