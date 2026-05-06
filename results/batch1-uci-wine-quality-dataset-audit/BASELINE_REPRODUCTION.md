# Baseline Reproduction

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| schema-only audit | missing=0, columns=12 | caught no missing values | missed class imbalance and duplicates |
| schema+distribution audit | duplicates=240, majorityShare=0.426 | caught duplicates and imbalance | does not validate sensory-label correctness |

Baseline reproduction is bounded to public-safe data or source-card evidence. Missing full-scale reproduction is recorded as a limitation, not hidden.
