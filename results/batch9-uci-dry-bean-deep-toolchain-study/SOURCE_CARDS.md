# Source Cards

## UCI Dry Bean Dataset

- Kind: public dataset.
- URL: https://archive.ics.uci.edu/dataset/602/dry+bean+dataset
- DOI: https://doi.org/10.24432/C50S4B
- Role: primary external target.
- Use in this result: loaded real public data and executed schema, baseline, metric stress, extension, and replay checks.
- Limitation: no official split was reproduced in this run.

## Dataset documentation

- Kind: dataset metadata and variable documentation.
- URL: https://archive.ics.uci.edu/dataset/602/dry+bean+dataset
- Role: source for dataset shape, features, class target, and provenance context.

## ucimlrepo

- Kind: data access package.
- URL: https://github.com/uci-ml-repo/ucimlrepo
- Role: loaded the UCI dataset by ID 602.

## pandas

- Kind: data analysis package.
- URL: https://pandas.pydata.org/
- Role: dataframe loading, missingness, duplicates, and schema checks.

## scikit-learn

- Kind: machine-learning package.
- URL: https://scikit-learn.org/
- Role: DummyClassifier, LogisticRegression, RandomForestClassifier, train/test split, metrics.

## Batch 7 schema_provenance_auditor

- Kind: prior Sovryn custom research tool.
- Corpus slug: batch7-wine-quality-schema-provenance-tool
- Role: required schema/provenance audit instrument.

## Batch 7 metric_stress_validator

- Kind: prior Sovryn custom research tool.
- Corpus slug: batch7-banknote-metric-stress-validator
- Role: required metric stress validation instrument.

## Batch 8 tool decision context

- Kind: prior tool reuse benchmark.
- Corpus slug: batch8-tool-reuse-failure-benchmark
- Role: establishes that `metric_stress_validator` was reusable and `schema_provenance_auditor` was narrow_but_useful before this Batch 9 study.
