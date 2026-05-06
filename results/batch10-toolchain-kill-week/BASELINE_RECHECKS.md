# Baseline Rechecks

## Schema baseline

Simple baseline:

- pandas `shape`
- pandas `isna`
- pandas `duplicated`
- pandas `value_counts`

Recheck:

This baseline can reproduce the raw Dry Bean and Wine Quality findings: row count, missingness, duplicate rows, and class distribution. Therefore, the schema tool is not a discovery engine for ordinary single-table audits.

Surviving value:

It produces source-hash-bound, public-safe schema/provenance evidence and consistent gates.

## Metric baseline

Simple baseline:

- sklearn train/test split
- `DummyClassifier`
- `LogisticRegression`
- `RandomForestClassifier`
- classification report and confusion matrix

Recheck:

sklearn can produce the raw Batch 9 metrics. The custom metric tool adds value only when it forces negative controls and anti-hype flags into the public package.

## Repo-test baseline

Simple baseline:

- grep for `def test`
- pytest collection or target execution

Recheck:

Static AST and grep inventory can agree, but runtime cases can expand through parametrization. Runtime collection/execution must remain the decisive evidence.
