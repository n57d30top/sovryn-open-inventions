# Baseline Reproduction

| Baseline / Challenger | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| schema-only audit | missing values and column count | 0.25 | misses distribution skew and duplicates |
| distribution-aware audit | zero-area and duplicate checks | 0.75 | does not validate fire-report ground truth |

Baseline claims are limited to the concrete metrics shown here.
