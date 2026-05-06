# Next Deep Target Selection

Batch 15 should choose one deep target rather than another broad expansion.

Candidate ranking:

| Candidate | Reason |
| --- | --- |
| UCI Statlog Shuttle | Largest Batch 14 split-risk delta and severe class-risk symptoms; useful for rare-class and metric-risk controls. |
| UCI Statlog Landsat Satellite | High severity, explicit no-cross-validation warning, and spatial/file split risk. |
| UCI HAR Smartphones | Strong subject-holdout control and stable carry-forward comparison. |
| UCI Letter Recognition | Useful for protocol-card ambiguity, but low measured split delta makes it less urgent as the deep target. |

Recommended Batch 15 deep target: UCI Statlog Shuttle or UCI Statlog Landsat Satellite, with Shuttle preferred if the goal is rare-class metric risk and Landsat preferred if the goal is spatial/file split protocol risk.
