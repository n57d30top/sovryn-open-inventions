# Targets

| Target | Rows | Features | Classes | Missing | Dup rows | Dup features | Fallback for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UCI Rice Cammeo/Osmancik | 3810 | 7 | 2 | 0 | 0 | 0 |  |
| UCI Optical Recognition of Handwritten Digits | 5620 | 64 | 10 | 0 | 0 | 0 |  |
| UCI Iris | 150 | 4 | 3 | 0 | 3 | 3 |  |
| UCI Wine Recognition | 178 | 13 | 3 | 0 | 0 | 0 |  |

Vehicle Silhouettes was attempted first and replaced by Iris after the target column exposed a one-row class value that blocked stratified modeling.
