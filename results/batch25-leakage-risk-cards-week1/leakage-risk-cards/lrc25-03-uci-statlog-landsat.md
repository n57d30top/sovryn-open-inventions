# lrc25-03-uci-statlog-landsat: UCI Statlog Landsat Satellite

Source URL: https://archive.ics.uci.edu/static/public/146/statlog+landsat+satellite.zip

Linked Protocol Card: pc21-03-uci-statlog-landsat

Source/protocol split definition: source_train_test_files

Random/stratified challenger definition: same-size stratified random split where execution is feasible.

Duplicate risk fields: train/test full-row hash overlap, train/test feature-vector hash overlap, within-split duplicate feature rows.

Group/subject/file risk fields: source identifiers checked when present; not invented when absent.

Feature leakage risk fields: target-like feature screening, high-cardinality ID-like feature screening, univariate class-association screening.

Target leakage risk fields: exact target-like feature check and limitation note.

Class imbalance / rare-class risk: spatial_file_overlap_not_directly_testable

Ambiguity notes: Batches 14, 16, and 20 preserved Landsat as spatial/file/protocol-risk evidence with missing spatial-coordinate limitations.

No-overclaim boundaries: This card does not claim confirmed leakage unless overlap or target-like evidence is directly found. Split deltas can remain ordinary protocol difficulty, class imbalance, or ambiguity.
