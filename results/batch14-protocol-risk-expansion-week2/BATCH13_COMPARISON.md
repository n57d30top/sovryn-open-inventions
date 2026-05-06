# Batch 13 Comparison

Batch 13 found random-over-source Logistic macro-F1 deltas from +0.0222 to +0.0293.

| Target | Batch 14 delta | Within Batch 13 range? | Larger than Batch 13 range? | Severity |
| --- | ---: | --- | --- | --- |
| UCI Human Activity Recognition Using Smartphones | 0.0288 | true | false | moderate |
| UCI Statlog Shuttle | 0.0702 | false | true | high |
| UCI Statlog Landsat Satellite | 0.0222 | true | false | high |
| UCI Letter Recognition | 0.0028 | false | false | low |

Batch 14 expanded the range. HAR remained in the Batch 13 range, Landsat was also in that range but scored high severity because of spatial/file-split and class-risk concerns, Shuttle was much larger at +0.0702, and Letter introduced protocol ambiguity despite a small measured delta.

Protocol-first validation remained justified because Batch 14 produced both larger split-risk and a new approximated-protocol case.
