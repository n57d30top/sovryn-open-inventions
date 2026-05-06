# Metric Risk Report

Metric risks checked:

- Shuffled-label control: macro-F1=0.0623.
- Majority baseline: macro-F1=0.0591.
- LogisticRegression: accuracy=0.9219, macro-F1=0.9347.
- RandomForestClassifier: accuracy=0.9197, macro-F1=0.9322.
- Simple baseline explains result: False.
- Accuracy could hide class failure according to tool flag: False.

Conclusion:

The score is not explained by dummy or shuffled-label controls. The stronger baselines remain ordinary sklearn baselines, so no benchmark-win or breakthrough claim is made.
