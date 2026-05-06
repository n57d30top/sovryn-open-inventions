# Random Split Challenger

Each challenger combines the source train/test data and creates a same-size stratified random split with seed 42.

| Target | Seed | Train rows | Test rows | Logistic accuracy | Logistic macro-F1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| UCI Human Activity Recognition Using Smartphones | 42 | 7352 | 2947 | 0.9820 | 0.9832 |
| UCI Statlog Shuttle | 42 | 43500 | 14500 | 0.9255 | 0.4530 |
| UCI Statlog Landsat Satellite | 42 | 4435 | 2000 | 0.8610 | 0.8192 |
| UCI Letter Recognition | 42 | 16000 | 4000 | 0.7742 | 0.7728 |

Random splits are challengers only. They are not substitutes for source-described protocols.
