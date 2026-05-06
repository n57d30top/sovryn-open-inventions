# lrc25-01-uci-har-smartphones: UCI HAR Smartphones

Source URL: https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip

Linked Protocol Card: pc21-01-uci-har-smartphones

Source/protocol split definition: source_train_test_files_with_subject_ids

Random/stratified challenger definition: same-size stratified random split where execution is feasible.

Duplicate risk fields: train/test full-row hash overlap, train/test feature-vector hash overlap, within-split duplicate feature rows.

Group/subject/file risk fields: source identifiers checked when present; not invented when absent.

Feature leakage risk fields: target-like feature screening, high-cardinality ID-like feature screening, univariate class-association screening.

Target leakage risk fields: exact target-like feature check and limitation note.

Class imbalance / rare-class risk: subject_overlap_or_subject_mixing_risk

Ambiguity notes: Batches 13, 14, 21, and 22 showed a source-vs-random macro-F1 delta around the moderate split-risk range; subject_train and subject_test are available.

No-overclaim boundaries: This card does not claim confirmed leakage unless overlap or target-like evidence is directly found. Split deltas can remain ordinary protocol difficulty, class imbalance, or ambiguity.
