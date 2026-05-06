# Metric Stress Results

`metric_stress_validator` was used as support evidence.

| Target | Shuffled-label macro-F1 | Weakest protocol class | Weakest protocol class F1 | Active flags |
| --- | ---: | --- | ---: | --- |
| UCI Human Activity Recognition Using Smartphones | 0.1512 | 4 | 0.9186 | randomSplitMateriallyDifferent |
| UCI Statlog Shuttle | 0.1276 | 2 | 0.0000 | accuracyCouldHideClassFailure, randomSplitMateriallyDifferent |
| UCI Statlog Landsat Satellite | 0.1068 | 4 | 0.3798 | accuracyCouldHideClassFailure, randomSplitMateriallyDifferent |
| UCI Letter Recognition | 0.0326 | H | 0.5314 | none |

The strongest metric-risk findings were Shuttle and Landsat: accuracy and macro-F1 diverged enough that aggregate accuracy alone would hide class-level weakness.
