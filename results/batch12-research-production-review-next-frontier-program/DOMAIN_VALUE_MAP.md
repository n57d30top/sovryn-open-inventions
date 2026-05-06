# Domain Value Map

| Domain | Value | Exec | Repro | Baseline | Tool fit | External | Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dataset quality / provenance auditing | 78 | 88 | 82 | 64 | 72 | 82 | continue_with_constraints |
| benchmark metric validation | 88 | 92 | 84 | 92 | 88 | 86 | promote |
| repo/test reproduction | 82 | 78 | 70 | 58 | 62 | 88 | continue_with_constraints |
| source/evidence extraction | 55 | 38 | 54 | 42 | 48 | 66 | deprioritize |
| time-series anomaly benchmarks | 74 | 76 | 68 | 70 | 58 | 80 | narrow |
| claim verification / evidence datasets | 50 | 32 | 50 | 40 | 42 | 68 | deprioritize |
| package install/test reproduction | 76 | 80 | 70 | 50 | 60 | 86 | narrow |
| scientific dataset reliability | 86 | 90 | 84 | 86 | 84 | 88 | promote |

## dataset quality / provenance auditing

Recommended action: `continue_with_constraints`.

Reason: Repeated useful negative findings appeared in Air Quality, Diamonds, Wine Quality, Dry Bean, and Batch 11, but pandas often explains the raw finding.

## benchmark metric validation

Recommended action: `promote`.

Reason: Batch 7, 9, 10, and 11 show repeatable baselines, metric stress, negative controls, and clear anti-hype value.

## repo/test reproduction

Recommended action: `continue_with_constraints`.

Reason: itsdangerous and pluggy produced real execution, but dependency variance and static/runtime pytest mismatch remain unresolved.

## source/evidence extraction

Recommended action: `deprioritize`.

Reason: The recent program produced stronger value from executed datasets and repos than from source-only review.

## time-series anomaly benchmarks

Recommended action: `narrow`.

Reason: Air Quality showed sentinel-aware value, but the current custom tools are less mature for temporal protocols than for split and metric checks.

## claim verification / evidence datasets

Recommended action: `deprioritize`.

Reason: Potentially useful, but under-executed in Batches 5-11 compared with dataset and benchmark work.

## package install/test reproduction

Recommended action: `narrow`.

Reason: Install/test reproduction is externally useful, but it needs runtime evidence improvements before promotion.

## scientific dataset reliability

Recommended action: `promote`.

Reason: The strongest repeated pattern is public dataset execution plus schema, split, metric, baseline, negative-control, and replay discipline.
