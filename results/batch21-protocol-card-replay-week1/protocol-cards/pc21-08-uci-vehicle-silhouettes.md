# pc21-08-uci-vehicle-silhouettes: UCI Vehicle Silhouettes

Source URL: https://archive.ics.uci.edu/static/public/149/statlog+vehicle+silhouettes.zip

Dataset access method: public source archive or documented bundled loader.

Protocol status: ambiguous

Split/protocol description: Archive provides multiple xaa-xai data shards, but no single canonical train/test split is provided.

Metrics: accuracy, macro-F1, weighted-F1, per-class F1 summary.

Baselines: DummyClassifier, linear logistic SGD, RandomForest where feasible.

Random challenger: stratified random split with same test fraction when feasible.

Replay feasibility: ready for execution.

Known limitations: Multiple plausible file-shard and random interpretations exist.

Claim boundaries: This card does not establish a benchmark win or full benchmark reproduction; it defines a replay plan and ambiguity boundary.
