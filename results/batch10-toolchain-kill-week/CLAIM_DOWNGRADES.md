# Claim Downgrades

## Downgrade 1

Original claim:

`schema_provenance_auditor` moved from `narrow_but_useful` to reusable for single-table tabular benchmark screening after Batch 9.

Downgraded wording:

`schema_provenance_auditor` is narrow but useful for public evidence packaging and comparable schema cards. For single-table tabular datasets, ordinary pandas checks dominate the raw discovery task.

## Downgrade 2

Original claim:

Existing tools were not enough for the Wine Quality duplicate/schema finding.

Downgraded wording:

Existing pandas tools were enough for the raw duplicate and missingness findings. The custom tool was useful because it packaged source hashes, schema comparison, and duplicate/missingness gates into one public artifact.

## Downgrade 3

Original claim:

`metric_stress_validator` is broadly reusable as the strongest Batch 7 tool.

Downgraded wording:

`metric_stress_validator` is the strongest of the three Batch 7 tools for anti-hype metric review, but it remains a support tool. It does not prove absence of leakage and does not replace official benchmark protocols.

## Downgrade 4

Original claim:

`pytest_repro_summary` can summarize repository reproduction reliably.

Downgraded wording:

`pytest_repro_summary` can summarize public-safe static and runtime evidence, but static inventory is not runtime reproduction and dependency failures must remain first-class outcomes.
