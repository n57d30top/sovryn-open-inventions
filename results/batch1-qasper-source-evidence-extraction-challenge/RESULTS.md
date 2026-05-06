# Results

| Metric | Value |
| --- | --- |
| expected source-card fields | 6 |
| README length chars inspected | 9639 |
| expected fields present in source | 6 |
| keyword baseline field recall | 0.667 |
| source-card parser field recall | 1 |
| official baseline Token F1 found | 1 |

## Baseline Matrix

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| title/abstract keyword baseline | homepage/license/leaderboards/evidence | 0.667 recall | missed official baseline metric and structured metadata link |
| source-card parser | homepage, license, leaderboards, official baseline, token f1, evidence | 1.000 recall | does not evaluate QA model answers |
