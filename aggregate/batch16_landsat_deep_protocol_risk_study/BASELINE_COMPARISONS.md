# Baseline Comparisons

| Split | Model | Accuracy | Macro-F1 | Weighted-F1 |
| --- | --- | --- | --- | --- |
| source | dummy_majority | 0.2305 | 0.0624 | 0.0864 |
| source | dummy_stratified | 0.1735 | 0.1516 | 0.1722 |
| source | forest | 0.9095 | 0.8939 | 0.9074 |
| source | linear | 0.8395 | 0.7971 | 0.8296 |
| stratified_random | dummy_majority | 0.2380 | 0.0641 | 0.0915 |
| stratified_random | dummy_stratified | 0.1870 | 0.1637 | 0.1876 |
| stratified_random | forest | 0.9165 | 0.8969 | 0.9139 |
| stratified_random | linear | 0.8610 | 0.8192 | 0.8539 |
| non_stratified_random | dummy_majority | 0.2325 | 0.0629 | 0.0877 |
| non_stratified_random | dummy_stratified | 0.1815 | 0.1558 | 0.1822 |
| non_stratified_random | forest | 0.9070 | 0.8918 | 0.9055 |
| non_stratified_random | linear | 0.8475 | 0.8094 | 0.8402 |
