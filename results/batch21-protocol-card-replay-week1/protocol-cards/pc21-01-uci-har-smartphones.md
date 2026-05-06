# pc21-01-uci-har-smartphones: UCI HAR Smartphones

Source URL: https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip

Dataset access method: public source archive or documented bundled loader.

Protocol status: clear

Split/protocol description: Archive provides train/test files and subject identifiers.

Metrics: accuracy, macro-F1, weighted-F1, per-class F1 summary.

Baselines: DummyClassifier, linear logistic SGD, RandomForest where feasible.

Random challenger: stratified random split with same test fraction when feasible.

Replay feasibility: ready for execution.

Known limitations: Low ambiguity in file split; subject grouping must remain explicit.

Claim boundaries: This card does not establish a benchmark win or full benchmark reproduction; it defines a replay plan and ambiguity boundary.
