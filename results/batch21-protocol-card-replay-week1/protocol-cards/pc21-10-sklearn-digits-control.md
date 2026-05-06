# pc21-10-sklearn-digits-control: scikit-learn bundled digits control

Source URL: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

Dataset access method: public source archive or documented bundled loader.

Protocol status: absent

Split/protocol description: Bundled low-risk toy dataset with no source-described benchmark split.

Metrics: accuracy, macro-F1, weighted-F1, per-class F1 summary.

Baselines: DummyClassifier, linear logistic SGD, RandomForest where feasible.

Random challenger: stratified random split with same test fraction when feasible.

Replay feasibility: ready for execution.

Known limitations: Useful only as a low-risk control; no source protocol should be invented.

Claim boundaries: This card does not establish a benchmark win or full benchmark reproduction; it defines a replay plan and ambiguity boundary.
