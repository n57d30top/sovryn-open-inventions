# Replay Results

## Fresh Seed Replay

| Target | Seed 42 random logistic macro-F1 | Seed 99 random logistic macro-F1 | Delta |
| --- | ---: | ---: | ---: |
| UCI Human Activity Recognition Using Smartphones | 0.9832 | 0.9823 | -0.0009 |
| UCI Statlog Shuttle | 0.4530 | 0.3827 | -0.0703 |
| UCI Statlog Landsat Satellite | 0.8192 | 0.8147 | -0.0045 |
| UCI Letter Recognition | 0.7728 | 0.7722 | -0.0005 |

## Container Network-Off Replay

| Target | Replay mode | Protocol status | Source/protocol logistic macro-F1 | Random challenger logistic macro-F1 | Severity |
| --- | --- | --- | ---: | ---: | --- |
| UCI Human Activity Recognition Using Smartphones | container --network none | protocol_reproduced | 0.9550 | 0.9832 | moderate |
| UCI Statlog Shuttle | container --network none | protocol_reproduced | 0.3828 | 0.4530 | high |
| UCI Statlog Landsat Satellite | container --network none | protocol_reproduced | 0.7971 | 0.8192 | high |
| UCI Letter Recognition | container --network none | protocol_approximated | 0.7699 | 0.7728 | low |

The container reported external network unreachable and still loaded all four targets from pre-provisioned public archives. That is the intended network-off behavior.
