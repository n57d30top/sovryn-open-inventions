# Baseline Reproduction

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| schema-only audit | 398 rows, 9 columns | 0.5 | does not treat question mark horsepower as missing |
| type-aware audit | 6 missing horsepower rows | 1 | does not validate real-world car measurement correctness |

Baseline reproduction is bounded to public-safe source or dataset evidence. Missing full-scale reproduction is recorded as a limitation, not hidden.
