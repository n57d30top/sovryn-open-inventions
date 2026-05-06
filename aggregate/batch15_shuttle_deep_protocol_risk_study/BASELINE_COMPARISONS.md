# Baseline Comparisons

| Split | Model | Accuracy | Macro-F1 | Weighted-F1 | Worst classes |
| --- | --- | --- | --- | --- | --- |
| source | dummy_majority | 0.7916 | 0.1262 | 0.6995 | 2:0.000, 3:0.000, 4:0.000 |
| source | dummy_stratified | 0.6458 | 0.1411 | 0.6481 | 2:0.000, 3:0.000, 6:0.000 |
| source | extra_trees | 0.9994 | 0.9825 | 0.9994 | 3:0.919, 2:0.960, 5:0.999 |
| source | forest | 0.9996 | 0.9205 | 0.9996 | 7:0.667, 6:0.857, 2:0.960 |
| source | linear | 0.9335 | 0.3862 | 0.9278 | 2:0.000, 3:0.000, 6:0.000 |
| stratified_random | dummy_majority | 0.7859 | 0.1257 | 0.6917 | 2:0.000, 3:0.000, 4:0.000 |
| stratified_random | dummy_stratified | 0.6432 | 0.1407 | 0.6432 | 2:0.000, 3:0.000, 6:0.000 |
| stratified_random | extra_trees | 0.9992 | 0.8443 | 0.9991 | 6:0.000, 3:0.914, 5:0.998 |
| stratified_random | forest | 0.9993 | 0.7075 | 0.9991 | 6:0.000, 7:0.000, 3:0.956 |
| stratified_random | linear | 0.9246 | 0.4518 | 0.9169 | 2:0.000, 3:0.000, 6:0.000 |
| non_stratified_random | dummy_majority | 0.7870 | 0.1258 | 0.6931 | 2:0.000, 3:0.000, 4:0.000 |
| non_stratified_random | dummy_stratified | 0.6406 | 0.1371 | 0.6408 | 2:0.000, 3:0.000, 6:0.000 |
| non_stratified_random | extra_trees | 0.9993 | 0.7898 | 0.9992 | 6:0.000, 7:0.667, 2:0.929 |
| non_stratified_random | forest | 0.9996 | 0.8411 | 0.9995 | 6:0.000, 2:0.889, 4:0.999 |
| non_stratified_random | linear | 0.9278 | 0.3825 | 0.9202 | 2:0.000, 3:0.000, 6:0.000 |

No benchmark-win claim is made.
