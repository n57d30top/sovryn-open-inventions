# Extension Attempts

| Target | Extension | Baseline | Baseline macro-F1 | Extension macro-F1 | Delta | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| UCI Rice Cammeo/Osmancik | class_weight_balanced_logistic_regression | logistic_regression | 0.9174 | 0.9223 | 0.0049 | accepted_measured_macro_f1_gain |
| UCI Rice Cammeo/Osmancik | class_weight_balanced_random_forest | random_forest | 0.9245 | 0.9190 | -0.0054 | rejected_macro_f1_decrease |
| UCI Optical Recognition of Handwritten Digits | class_weight_balanced_logistic_regression | logistic_regression | 0.9704 | 0.9704 | -0.0000 | downgraded_no_material_macro_f1_gain |
| UCI Optical Recognition of Handwritten Digits | class_weight_balanced_random_forest | random_forest | 0.9864 | 0.9864 | 0.0000 | downgraded_no_material_macro_f1_gain |
| UCI Iris | class_weight_balanced_logistic_regression | logistic_regression | 0.9107 | 0.9107 | 0.0000 | downgraded_no_material_macro_f1_gain |
| UCI Iris | class_weight_balanced_random_forest | random_forest | 0.8878 | 0.8878 | 0.0000 | downgraded_no_material_macro_f1_gain |
| UCI Wine Recognition | class_weight_balanced_logistic_regression | logistic_regression | 0.9829 | 0.9829 | 0.0000 | downgraded_no_material_macro_f1_gain |
| UCI Wine Recognition | class_weight_balanced_random_forest | random_forest | 1.0000 | 1.0000 | 0.0000 | downgraded_no_material_macro_f1_gain |

At least one extension was rejected or downgraded. No improvement claim is made unless the measured macro-F1 delta supports it.
