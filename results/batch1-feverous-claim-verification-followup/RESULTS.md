# Results

| Metric | Value |
| --- | --- |
| required evaluation fields | 4 |
| README mentions evaluation command | 1 |
| baseline field recall | 0.75 |
| schema-aware field recall | 1 |
| reproduction score | 78 |

## Baseline Matrix

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| README-only protocol parser | label/predicted_label/evidence | 0.75 recall | missed predicted_evidence formatting note |
| schema-aware parser | label/predicted_label/evidence/predicted_evidence | 1.00 recall | still no full dataset baseline run |
