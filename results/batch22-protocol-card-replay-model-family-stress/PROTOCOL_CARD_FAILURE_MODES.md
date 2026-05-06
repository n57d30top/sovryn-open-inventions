# Protocol Card Failure Modes

- Vehicle Silhouettes: Protocol Card cannot identify a canonical train/test split; shard holdout is only one interpretation.
- Letter Recognition: row-order split is source-described but not file-separated.
- Shuttle: source files are clear, but original time-order generation is not reconstructable.
- Landsat: source files are clear, but spatial grouping is not exposed.
- HAR: subject boundary is clear, but Protocol Card still needs explicit subject-overlap checks.
