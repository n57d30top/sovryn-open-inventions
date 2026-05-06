# pc21-06-uci-letter-recognition: UCI Letter Recognition

Source URL: https://archive.ics.uci.edu/static/public/59/letter+recognition.zip

Dataset access method: public source archive or documented bundled loader.

Protocol status: approximated

Split/protocol description: Documentation describes first 16000 rows for training and remaining 4000 for testing, but no separate split files.

Metrics: accuracy, macro-F1, weighted-F1, per-class F1 summary.

Baselines: DummyClassifier, linear logistic SGD, RandomForest where feasible.

Random challenger: stratified random split with same test fraction when feasible.

Replay feasibility: ready for execution.

Known limitations: The order split is source-described but not file-separated.

Claim boundaries: This card does not establish a benchmark win or full benchmark reproduction; it defines a replay plan and ambiguity boundary.
