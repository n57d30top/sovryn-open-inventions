# Baseline Comparisons

Metrics are `accuracy / macro-F1`.

| Target | Split | Dummy most-frequent | LogisticRegression | RandomForest |
| --- | --- | ---: | ---: | ---: |
| UCI Human Activity Recognition Using Smartphones | source train/test | 0.1822 / 0.0514 | 0.9545 / 0.9544 | 0.9233 / 0.9216 |
| UCI Human Activity Recognition Using Smartphones | stratified random challenger | 0.1887 / 0.0529 | 0.9820 / 0.9832 | 0.9773 / 0.9776 |
| UCI Optical Recognition of Handwritten Digits | source train/test | 0.1013 / 0.0184 | 0.9499 / 0.9500 | 0.9683 / 0.9682 |
| UCI Optical Recognition of Handwritten Digits | stratified random challenger | 0.1018 / 0.0185 | 0.9722 / 0.9722 | 0.9855 / 0.9855 |
| UCI Pen-Based Recognition of Handwritten Digits | source train/test | 0.1038 / 0.0188 | 0.9160 / 0.9164 | 0.9640 / 0.9645 |
| UCI Pen-Based Recognition of Handwritten Digits | stratified random challenger | 0.1041 / 0.0188 | 0.9463 / 0.9458 | 0.9877 / 0.9879 |

The linear and tree baselines both stayed far above dummy baselines. The result is not a benchmark win; it is a protocol-vs-random split comparison.
