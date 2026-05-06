# lrc25-02-uci-statlog-shuttle: UCI Statlog Shuttle

Source URL: https://archive.ics.uci.edu/static/public/148/statlog+shuttle.zip

Linked Protocol Card: pc21-02-uci-statlog-shuttle

Source/protocol split definition: source_train_test_files

Random/stratified challenger definition: same-size stratified random split where execution is feasible.

Duplicate risk fields: train/test full-row hash overlap, train/test feature-vector hash overlap, within-split duplicate feature rows.

Group/subject/file risk fields: source identifiers checked when present; not invented when absent.

Feature leakage risk fields: target-like feature screening, high-cardinality ID-like feature screening, univariate class-association screening.

Target leakage risk fields: exact target-like feature check and limitation note.

Class imbalance / rare-class risk: class_imbalance_mimics_leakage_risk

Ambiguity notes: Batches 14 and 15 found high split-risk symptoms and rare-class / metric-risk limits on the source split.

No-overclaim boundaries: This card does not claim confirmed leakage unless overlap or target-like evidence is directly found. Split deltas can remain ordinary protocol difficulty, class imbalance, or ambiguity.
