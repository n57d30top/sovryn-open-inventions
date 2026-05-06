# Method

1. Select a public-safe target matching the Batch 6 target type: public scientific or ML repository with tests/examples.
2. Check source access and safety boundaries.
3. Create an isolated Python execution environment.
4. Install or provision only the packages needed for this target: scikit-learn 1.8.0.
5. Execute the smoke, baseline, challenger or data-quality checks described below.
6. Record the highest ladder level honestly and stop short of unsupported full-reproduction claims.

## Executed checks

Loaded the Iris dataset through scikit-learn, ran five-fold stratified cross-validation, trained a heldout LogisticRegression pipeline, and compared against DummyClassifier and DecisionTreeClassifier.

## Metrics summary

```json
{
  "dataset": {
    "classes": 3,
    "features": 4,
    "name": "Iris plants dataset bundled with scikit-learn",
    "rows": 150
  },
  "execution": {
    "cv_folds": 5,
    "models_executed": [
      "DummyClassifier most_frequent",
      "StandardScaler + LogisticRegression",
      "DecisionTreeClassifier max_depth=3"
    ],
    "train_test_split_rows": {
      "test": 30,
      "train": 120
    }
  },
  "generated_at": "2026-05-06T08:29:29.078820+00:00",
  "highest_ladder_level": 8,
  "installed_packages": {
    "scikit-learn": "1.8.0"
  },
  "metrics": {
    "dummy_accuracy_mean": 0.3333333333333333,
    "dummy_accuracy_scores": [
      0.3333333333333333,
      0.3333333333333333,
      0.3333333333333333,
      0.3333333333333333,
      0.3333333333333333
    ],
    "heldout_logreg_accuracy": 0.9666666666666667,
    "logreg_accuracy_mean": 0.9666666666666668,
    "logreg_accuracy_scores": [
      0.9666666666666667,
      0.9,
      1,
      0.9666666666666667,
      1
    ],
    "tree_accuracy_mean": 0.9533333333333334,
    "tree_accuracy_scores": [
      0.9666666666666667,
      0.9333333333333333,
      0.9666666666666667,
      0.9,
      1
    ]
  },
  "negative_or_partial": true,
  "partial_reason": "The package installed and examples/smoke metrics executed, but the upstream repository test suite was not cloned and run in full.",
  "result_label": "partial_reproduction_smoke_only",
  "source_urls": [
    "https://github.com/scikit-learn/scikit-learn",
    "https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html"
  ],
  "target": "scikit-learn repository/package Iris example smoke reproduction"
}
```
