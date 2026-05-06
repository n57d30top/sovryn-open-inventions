# Results

| Metric | Value |
| --- | --- |
| rows audited | 1599 |
| columns audited | 12 |
| missing cells | 0 |
| duplicate rows | 240 |
| duplicate rate | 0.15 |
| majority quality share | 0.426 |
| rare extreme-quality rows | 81 |
| schema-only issue recall | 0.4 |
| schema+distribution issue recall | 0.8 |

## Baseline Matrix

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| schema-only audit | missing=0, columns=12 | caught no missing values | missed class imbalance and duplicates |
| schema+distribution audit | duplicates=240, majorityShare=0.426 | caught duplicates and imbalance | does not validate sensory-label correctness |
