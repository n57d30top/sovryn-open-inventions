# Random Split Challenger

Each challenger combined the source train and test files, then created a stratified random split with seed 42 and the same test fraction as the source test file.

| Target | Seed | Train rows | Test rows | Logistic accuracy | Logistic macro-F1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| UCI Human Activity Recognition Using Smartphones | 42 | 7352 | 2947 | 0.9820 | 0.9832 |
| UCI Optical Recognition of Handwritten Digits | 42 | 3823 | 1797 | 0.9722 | 0.9722 |
| UCI Pen-Based Recognition of Handwritten Digits | 42 | 7494 | 3498 | 0.9463 | 0.9458 |

The challenger is not treated as more official than the source files. It is a split-risk contrast.
