# lrc25-05-uci-vehicle-silhouettes: UCI Vehicle Silhouettes

Source URL: https://archive.ics.uci.edu/static/public/149/statlog+vehicle+silhouettes.zip

Linked Protocol Card: pc21-08-uci-vehicle-silhouettes

Source/protocol split definition: protocol_ambiguous_source_shards

Random/stratified challenger definition: same-size stratified random split where execution is feasible.

Duplicate risk fields: train/test full-row hash overlap, train/test feature-vector hash overlap, within-split duplicate feature rows.

Group/subject/file risk fields: source identifiers checked when present; not invented when absent.

Feature leakage risk fields: target-like feature screening, high-cardinality ID-like feature screening, univariate class-association screening.

Target leakage risk fields: exact target-like feature check and limitation note.

Class imbalance / rare-class risk: file_shard_protocol_ambiguity_blocks_leakage_conclusion

Ambiguity notes: Batches 22 and 23 selected and downgraded Vehicle as an ambiguous shard-layout target with no source-declared canonical split.

No-overclaim boundaries: This card does not claim confirmed leakage unless overlap or target-like evidence is directly found. Split deltas can remain ordinary protocol difficulty, class imbalance, or ambiguity.
