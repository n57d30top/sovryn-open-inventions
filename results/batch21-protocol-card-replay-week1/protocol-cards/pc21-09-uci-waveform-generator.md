# pc21-09-uci-waveform-generator: UCI Waveform Database Generator

Source URL: https://archive.ics.uci.edu/static/public/107/waveform+database+generator+version+1.zip

Dataset access method: public source archive or documented bundled loader.

Protocol status: ambiguous

Split/protocol description: Archive provides generator code and compressed generated data; fixed benchmark split is weakly specified.

Metrics: accuracy, macro-F1, weighted-F1, per-class F1 summary.

Baselines: DummyClassifier, linear logistic SGD, RandomForest where feasible.

Random challenger: stratified random split with same test fraction when feasible.

Replay feasibility: defer until loader/protocol clarification.

Known limitations: Generated data can be replayed in multiple ways; fixed split semantics are weak.

Claim boundaries: This card does not establish a benchmark win or full benchmark reproduction; it defines a replay plan and ambiguity boundary.
