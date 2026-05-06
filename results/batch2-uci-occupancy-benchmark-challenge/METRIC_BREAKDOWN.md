# Metric Breakdown

| Method | Precision | Recall | F1 | Balanced Accuracy | FP | FN | Rejected |
| --- | --- | --- | --- | --- | --- | --- | --- |
| light_threshold_train_selected | 0.974 | 0.994 | 0.984 | 0.994 | 55 | 12 | false |
| co2_threshold_train_selected | 0.312 | 0.798 | 0.448 | 0.665 | 3612 | 413 | false |
| temperature_threshold_train_selected | 0.618 | 0.911 | 0.736 | 0.881 | 1153 | 183 | false |
| humidity_threshold_train_selected | 0.21 | 1 | 0.347 | 0.5 | 7703 | 0 | false |
| two_of_four_sensor_vote_candidate | 0.341 | 1 | 0.508 | 0.743 | 3967 | 0 | true |
| three_of_four_sensor_vote_candidate | 0.711 | 0.992 | 0.828 | 0.942 | 828 | 16 | true |

## Concrete Metrics

| Metric | Value |
| --- | --- |
| train rows | 8143 |
| holdout rows | 9752 |
| train occupancy rate | 0.212 |
| holdout occupancy rate | 0.21 |
| best baseline | light_threshold_train_selected |
| best baseline F1 | 0.984 |
| candidate rejected | 2 |
| wins | 0 |
| losses | 2 |
| ties | 0 |
