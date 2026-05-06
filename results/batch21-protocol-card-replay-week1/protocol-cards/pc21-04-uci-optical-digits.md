# pc21-04-uci-optical-digits: UCI Optical Digits

Source URL: https://archive.ics.uci.edu/static/public/80/optical+recognition+of+handwritten+digits.zip

Dataset access method: public source archive or documented bundled loader.

Protocol status: clear

Split/protocol description: Archive provides optdigits.tra and optdigits.tes train/test files.

Metrics: accuracy, macro-F1, weighted-F1, per-class F1 summary.

Baselines: DummyClassifier, linear logistic SGD, RandomForest where feasible.

Random challenger: stratified random split with same test fraction when feasible.

Replay feasibility: ready for execution.

Known limitations: Writer/source grouping is partly described but not fully exposed in the compact files.

Claim boundaries: This card does not establish a benchmark win or full benchmark reproduction; it defines a replay plan and ambiguity boundary.
