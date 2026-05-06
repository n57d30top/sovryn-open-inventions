# pc21-03-uci-statlog-landsat: UCI Statlog Landsat Satellite

Source URL: https://archive.ics.uci.edu/static/public/146/statlog+landsat+satellite.zip

Dataset access method: public source archive or documented bundled loader.

Protocol status: clear

Split/protocol description: Archive provides sat.trn and sat.tst and documentation warns against cross-validation.

Metrics: accuracy, macro-F1, weighted-F1, per-class F1 summary.

Baselines: DummyClassifier, linear logistic SGD, RandomForest where feasible.

Random challenger: stratified random split with same test fraction when feasible.

Replay feasibility: ready for execution.

Known limitations: Spatial/file context is described but exact geographic grouping is absent.

Claim boundaries: This card does not establish a benchmark win or full benchmark reproduction; it defines a replay plan and ambiguity boundary.
