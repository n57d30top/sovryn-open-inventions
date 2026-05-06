# Baseline Reproduction

| Baseline / Challenger | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| schema-only audit | shape and duplicate checks | 0.167 | misses most field-level missingness |
| type-aware audit | missing-by-column checks | 0.833 | does not validate biological measurement correctness |

Baseline claims are limited to the concrete metrics shown here.
