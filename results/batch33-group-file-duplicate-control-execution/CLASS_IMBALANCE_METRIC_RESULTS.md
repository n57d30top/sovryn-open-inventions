# Class Imbalance and Metric Results

| Target | Source accuracy | Source macro-F1 | Source weighted-F1 | Random macro-F1 | Shuffled-label macro-F1 |
| --- | --- | --- | --- | --- | --- |
| UCI Statlog Shuttle | 0.9234 | 0.3779 | 0.9142 | 0.5664 | 0.1266 |
| UCI HAR Smartphones | 0.962 | 0.9624 | 0.9619 | 0.9852 | 0.1664 |
| UCI Statlog Landsat Satellite | 0.818 | 0.7374 | 0.7856 | 0.7443 | 0.2033 |
| UCI Letter Recognition | 0.7145 | 0.7051 | 0.7071 | 0.6981 | 0.0324 |
| UCI Optical Digits | 0.9471 | 0.9472 | 0.9473 | 0.9682 | 0.1096 |
| scikit-learn digits control | 0.9704 | 0.9702 | 0.9703 | 0.9557 | 0.147 |

Shuttle was the strongest class/metric mechanism case: linear source macro-F1 was 0.3779 while random macro-F1 was 0.5664, and shuffled-label control remained low at 0.1266. This supports a rare-class/class-imbalance explanation more than a confirmed duplicate-transfer explanation.
