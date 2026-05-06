# lrc25-04-uci-letter-recognition: UCI Letter Recognition

Source URL: https://archive.ics.uci.edu/static/public/59/letter+recognition.zip

Linked Protocol Card: pc21-06-uci-letter-recognition

Source/protocol split definition: approximated_row_order_protocol

Random/stratified challenger definition: same-size stratified random split where execution is feasible.

Duplicate risk fields: train/test full-row hash overlap, train/test feature-vector hash overlap, within-split duplicate feature rows.

Group/subject/file risk fields: source identifiers checked when present; not invented when absent.

Feature leakage risk fields: target-like feature screening, high-cardinality ID-like feature screening, univariate class-association screening.

Target leakage risk fields: exact target-like feature check and limitation note.

Class imbalance / rare-class risk: low_leakage_control_and_protocol_ambiguity_check

Ambiguity notes: Batches 14, 21, and 22 treated Letter as an approximated row-order protocol and a near-control with low source-vs-random delta.

No-overclaim boundaries: This card does not claim confirmed leakage unless overlap or target-like evidence is directly found. Split deltas can remain ordinary protocol difficulty, class imbalance, or ambiguity.
