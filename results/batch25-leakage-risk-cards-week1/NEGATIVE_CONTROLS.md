# Negative Controls

| target | shuffled-label macro-F1 | duplicate-aware attempted | duplicate-aware result | control effect |
| --- | --- | --- | --- | --- |
| UCI HAR Smartphones | 0.131544 | False | No cross-split feature hash overlap was found in the source split. | weakens leakage claim unless direct overlap is found |
| UCI Statlog Shuttle | 0.127626 | False | No cross-split feature hash overlap was found in the source split. | weakens leakage claim unless direct overlap is found |
| UCI Letter Recognition | 0.016277 | True | -0.033754 | weakens leakage claim unless direct overlap is found |

Letter served as the low-risk near-control target. Controls weakened broad leakage claims because split deltas did not automatically map to confirmed duplicate, group, or target leakage.
