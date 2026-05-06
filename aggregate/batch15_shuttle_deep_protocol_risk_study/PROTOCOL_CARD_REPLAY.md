# Protocol-Card Replay

Replay card:

- Source files: `shuttle.trn` and `shuttle.tst`.
- Source protocol: train on source train file, evaluate on source test file.
- Random challenger: same combined data, same test size, stratified by class.
- Models: dummy, simple linear, RandomForest, ExtraTrees.
- Seeds: 1, 7, 13, 42, 99.
- Package versions: pandas 3.0.2, numpy 2.4.4, scikit-learn 1.8.0.
