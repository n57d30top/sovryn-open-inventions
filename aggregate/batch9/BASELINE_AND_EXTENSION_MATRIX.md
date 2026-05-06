# Baseline And Extension Matrix

| Model or extension | Accuracy | Macro-F1 | Decision |
| --- | ---: | ---: | --- |
| DummyClassifier most_frequent | 0.2605 | 0.0591 | weak simple baseline |
| DummyClassifier stratified | 0.1697 | 0.1403 | weak stochastic baseline |
| LogisticRegression | 0.9219 | 0.9347 | strong ordinary baseline |
| RandomForestClassifier | 0.9197 | 0.9322 | strong ordinary baseline |
| class_weight balanced LogisticRegression | 0.9160 | 0.9309 | reject_no_macro_f1_gain |
