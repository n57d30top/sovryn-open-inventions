# Data And Class-Risk Audit

| Metric | Value |
| --- | --- |
| Rows | 58000 |
| Features | 9 |
| Classes | 7 |
| Train rows | 43500 |
| Test rows | 14500 |
| Missing cells | 0 |
| Duplicate feature rows | 0 |
| Train/test max class distribution delta | 0.0075 |

Class counts:

```json
{
  "1": 45586,
  "2": 50,
  "3": 171,
  "4": 8903,
  "5": 3267,
  "6": 10,
  "7": 13
}
```

The rare classes are the main stress point. Accuracy can remain high because the majority class dominates, while macro-F1 exposes rare-class weakness.
