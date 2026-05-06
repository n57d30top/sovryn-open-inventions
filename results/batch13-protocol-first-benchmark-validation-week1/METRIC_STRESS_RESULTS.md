# Metric Stress Results

`metric_stress_validator` was used as anti-hype support, not as proof of benchmark validity.

| Target | Shuffled-label macro-F1 | Weakest protocol class F1 | Weakest class | Split-risk status | Active flags |
| --- | ---: | ---: | --- | --- | --- |
| UCI Human Activity Recognition Using Smartphones | 0.1512 | 0.9186 | 4 | material_protocol_difference | randomSplitMateriallyDifferent |
| UCI Optical Recognition of Handwritten Digits | 0.1305 | 0.9012 | 8 | material_protocol_difference | randomSplitMateriallyDifferent |
| UCI Pen-Based Recognition of Handwritten Digits | 0.0687 | 0.8163 | 1 | material_protocol_difference | randomSplitMateriallyDifferent |

Shuffled-label controls remained low on all completed targets. The useful stress finding was not a magic discovery; it was that random split performance differed materially from source train/test performance on all three targets.
