# pc21-07-uci-image-segmentation: UCI Image Segmentation

Source URL: https://archive.ics.uci.edu/static/public/50/image+segmentation.zip

Dataset access method: public source archive or documented bundled loader.

Protocol status: clear

Split/protocol description: Archive provides segmentation.data and segmentation.test files with class label first.

Metrics: accuracy, macro-F1, weighted-F1, per-class F1 summary.

Baselines: DummyClassifier, linear logistic SGD, RandomForest where feasible.

Random challenger: stratified random split with same test fraction when feasible.

Replay feasibility: ready for execution.

Known limitations: File split is clear, but image-source grouping details are limited.

Claim boundaries: This card does not establish a benchmark win or full benchmark reproduction; it defines a replay plan and ambiguity boundary.
