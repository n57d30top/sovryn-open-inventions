# scikit-learn Iris Example Reproduction Ladder

Sovryn provisioned scikit-learn 1.8.0, executed a bounded Iris classification smoke reproduction, compared a most-frequent dummy baseline with LogisticRegression and a shallow decision tree, and marked the result partial because the full upstream repository test suite was not run.

## What was executed

Loaded the Iris dataset through scikit-learn, ran five-fold stratified cross-validation, trained a heldout LogisticRegression pipeline, and compared against DummyClassifier and DecisionTreeClassifier.

## What Sovryn learned

The package install and example-scale classifier path are reproducible in this environment, but this is not a full repository reproduction because upstream tests were not run.

## Ladder status

Highest reproduction ladder level reached: **Level 8**.

## Public sources

| Source | URL | Role |
| --- | --- | --- |
| scikit-learn GitHub repository | https://github.com/scikit-learn/scikit-learn | BSD-3-Clause project repository with examples and tests. |
| Iris example documentation | https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html | Public example documentation for loading and inspecting the Iris dataset. |

## Status

- Result label: `partial_reproduction_smoke_only`
- Negative or partial result: `true`
- Publication safety: public, computational, non-sensitive data only

## Disclaimer

Sovryn produces autonomous open-research artifacts, defensive publications, and open-source research evidence. It is not a patent filing system and does not provide legal patentability, legal novelty, or freedom-to-operate opinions.
