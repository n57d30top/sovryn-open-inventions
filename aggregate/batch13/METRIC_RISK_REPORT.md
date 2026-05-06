# Metric Risk Report

| Target | Shuffled-label macro-F1 | Weakest protocol class F1 | Weakest class | Active flags |
| --- | ---: | ---: | --- | --- |
| UCI Human Activity Recognition Using Smartphones | 0.1512 | 0.9186 | 4 | randomSplitMateriallyDifferent |
| UCI Optical Recognition of Handwritten Digits | 0.1305 | 0.9012 | 8 | randomSplitMateriallyDifferent |
| UCI Pen-Based Recognition of Handwritten Digits | 0.0687 | 0.8163 | 1 | randomSplitMateriallyDifferent |

Macro-F1 and accuracy were close on the completed protocol splits, but class-level reporting still mattered. For Pen Digits, class `1` had the weakest protocol F1 despite high aggregate accuracy.
