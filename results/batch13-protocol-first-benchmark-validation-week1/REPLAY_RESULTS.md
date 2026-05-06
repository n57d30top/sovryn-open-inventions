# Replay Results

## Fresh Seed Replay

| Target | Seed 42 random logistic macro-F1 | Seed 99 random logistic macro-F1 | Delta |
| --- | ---: | ---: | ---: |
| UCI Human Activity Recognition Using Smartphones | 0.9832 | 0.9823 | -0.0009 |
| UCI Optical Recognition of Handwritten Digits | 0.9722 | 0.9701 | -0.0021 |
| UCI Pen-Based Recognition of Handwritten Digits | 0.9458 | 0.9533 | 0.0075 |

## Container Network-Off Replay

| Target | Replay mode | Source split logistic macro-F1 | Random challenger logistic macro-F1 | Split-risk status |
| --- | --- | ---: | ---: | --- |
| UCI Human Activity Recognition Using Smartphones | container --network none | 0.9550 | 0.9832 | material_protocol_difference |
| UCI Optical Recognition of Handwritten Digits | container --network none | 0.9500 | 0.9722 | material_protocol_difference |
| UCI Pen-Based Recognition of Handwritten Digits | container --network none | 0.9164 | 0.9458 | material_protocol_difference |

The container replay reported external network unreachable and still loaded all three targets from pre-provisioned public archives. That is the intended network-off behavior.
