# Execution Details

- Execution profile: container-netoff
- Worker assurance: container-netoff
- Actual execution included: true
- Public artifact policy: aggregate metrics only

## Procedure

The run fetched the public archive, extracted the CSV, parsed semicolon-delimited rows with decimal commas, converted -200 sentinels into missingness evidence, checked timestamp continuity, computed per-column summaries, and compared a schema-only missingness detector against a sentinel-aware detector.

## Evidence

Container-netoff audit over 9357 rows and 15 columns. NMHC(GT) missing-sentinel rate 0.902; sentinel-aware detector F1 1 versus schema-only F1 0.
