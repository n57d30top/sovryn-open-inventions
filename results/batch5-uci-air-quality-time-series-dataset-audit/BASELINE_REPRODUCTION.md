# Baseline Reproduction

Baseline reproduction target: schema-only missingness detection over numeric fields. This baseline treats fields as present when a numeric cell exists, so -200 sentinel values are missed.

## Outcome

Container-netoff audit over 9357 rows and 15 columns. NMHC(GT) missing-sentinel rate 0.902; sentinel-aware detector F1 1 versus schema-only F1 0.
