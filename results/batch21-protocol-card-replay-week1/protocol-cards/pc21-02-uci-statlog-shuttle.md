# pc21-02-uci-statlog-shuttle: UCI Statlog Shuttle

Source URL: https://archive.ics.uci.edu/static/public/148/statlog+shuttle.zip

Dataset access method: public source archive or documented bundled loader.

Protocol status: clear

Split/protocol description: Archive provides shuttle.trn and shuttle.tst; documentation notes time-order and majority-class context.

Metrics: accuracy, macro-F1, weighted-F1, per-class F1 summary.

Baselines: DummyClassifier, linear logistic SGD, RandomForest where feasible.

Random challenger: stratified random split with same test fraction when feasible.

Replay feasibility: ready for execution.

Known limitations: Source split is replayable, but original time-order generation is not fully reconstructable.

Claim boundaries: This card does not establish a benchmark win or full benchmark reproduction; it defines a replay plan and ambiguity boundary.
