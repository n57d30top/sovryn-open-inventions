# Baseline Comparisons

Metrics are `accuracy / macro-F1`.

| Target | Split | Dummy most-frequent | Logistic/linear baseline | RandomForest/simple tree |
| --- | --- | ---: | ---: | ---: |
| UCI Human Activity Recognition Using Smartphones | source-described | 0.1822 / 0.0514 | 0.9545 / 0.9544 | 0.9250 / 0.9233 |
| UCI Human Activity Recognition Using Smartphones | stratified-random challenger | 0.1887 / 0.0529 | 0.9820 / 0.9832 | 0.9766 / 0.9769 |
| UCI Statlog Shuttle | source-described | 0.7916 / 0.1262 | 0.9287 / 0.3828 | 0.9997 / 0.8257 |
| UCI Statlog Shuttle | stratified-random challenger | 0.7859 / 0.1257 | 0.9255 / 0.4530 | 0.9994 / 0.8045 |
| UCI Statlog Landsat Satellite | source-described | 0.2305 / 0.0624 | 0.8395 / 0.7971 | 0.9115 / 0.8960 |
| UCI Statlog Landsat Satellite | stratified-random challenger | 0.2380 / 0.0641 | 0.8610 / 0.8192 | 0.9145 / 0.8950 |
| UCI Letter Recognition | source-described | 0.0360 / 0.0027 | 0.7720 / 0.7699 | 0.9603 / 0.9602 |
| UCI Letter Recognition | stratified-random challenger | 0.0408 / 0.0030 | 0.7742 / 0.7728 | 0.9680 / 0.9678 |

The result does not claim any benchmark win. For Shuttle, aggregate accuracy is misleading because several rare classes have zero or weak F1 under the linear baseline.
