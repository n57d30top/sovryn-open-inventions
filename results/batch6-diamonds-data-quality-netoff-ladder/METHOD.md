# Method

1. Select a public-safe target matching the Batch 6 target type: public data-quality target.
2. Check source access and safety boundaries.
3. Create an isolated Python execution environment.
4. Install or provision only the packages needed for this target: pandas 3.0.2.
5. Execute the smoke, baseline, challenger or data-quality checks described below.
6. Record the highest ladder level honestly and stop short of unsupported full-reproduction claims.

## Executed checks

Loaded 53940 CSV rows with pandas in a network-off sandbox and checked missing cells, duplicate rows, nonpositive numeric values, empty categorical values, positive carat with nonpositive dimensions, and upper-tail price count.

## Metrics summary

```json
{
  "dataset": {
    "columns": [
      "carat",
      "cut",
      "color",
      "clarity",
      "depth",
      "table",
      "price",
      "x",
      "y",
      "z"
    ],
    "download_sha256": "9574730b03aba241d899c4a97511c5061b19358fab89510774fb6c24168345c4",
    "rows": 53940
  },
  "execution": {
    "checks_executed": [
      "missing cells",
      "duplicate rows",
      "nonpositive numeric values",
      "empty categorical values",
      "positive carat with nonpositive dimensions",
      "upper-tail price count"
    ],
    "isolation": "sandbox-exec network denied",
    "parser": "pandas.read_csv"
  },
  "generated_at": "2026-05-06T08:31:27.698936+00:00",
  "highest_ladder_level": 9,
  "negative_or_partial": true,
  "quality_checks": {
    "duplicate_rows": 146,
    "empty_categorical_values": {
      "clarity": 0,
      "color": 0,
      "cut": 0
    },
    "missing_cells": 0,
    "nonpositive_numeric_values": {
      "carat": 0,
      "depth": 0,
      "price": 0,
      "table": 0,
      "x": 8,
      "y": 7,
      "z": 20
    },
    "positive_carat_nonpositive_dimension_rows": 20,
    "price_upper_tail_count_99_5pct": 270
  },
  "result_label": "data_quality_issues_confirmed_under_network_off_replay",
  "source_urls": [
    "https://github.com/mwaskom/seaborn-data",
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv"
  ],
  "target": "seaborn-data diamonds CSV data-quality network-off audit"
}
```
