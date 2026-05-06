# Method

The run fetched the public archive, extracted the CSV, parsed semicolon-delimited rows with decimal commas, converted -200 sentinels into missingness evidence, checked timestamp continuity, computed per-column summaries, and compared a schema-only missingness detector against a sentinel-aware detector.

## Rejected Overclaims

Rejected candidate: schema_only_missing_detector for sentinel-missingness detection. It remains useful only as a weak baseline, not as a final audit method.
