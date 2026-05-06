# Batch 9 UCI Dry Bean Deep Toolchain Study

Batch 9 is a deep external target study, not a continuity review. Sovryn used the UCI Dry Bean Dataset as one concrete public target and ran the existing Batch 7/8 toolchain on real data.

What actually ran:

- Loaded the UCI Dry Bean Dataset with `ucimlrepo`.
- Ran `schema_provenance_auditor` on the curated CSV.
- Ran `metric_stress_validator` on the same target in headerless form.
- Trained dummy, linear, and tree baselines on a stratified 70/30 split.
- Ran shuffled-label, seed-variation, and stratified/non-stratified metric stress checks.
- Tried a small class-weight extension and rejected it because macro-F1 did not improve on the primary split.
- Replayed the local data/toolchain in a `--network none` container.

Core findings:

- Dataset shape: 13611 rows, 16 features, 7 classes.
- Schema/provenance: 0 missing cells, 68 duplicate full rows, 68 duplicate feature rows, no checked sentinel values.
- LogisticRegression: accuracy=0.9219, macro-F1=0.9347.
- RandomForestClassifier: accuracy=0.9197, macro-F1=0.9322.
- Shuffled-label control: accuracy=0.2605, macro-F1=0.0623.
- Class-weight extension: reject_no_macro_f1_gain, macro-F1 delta=-0.0038.
- Container replay: network=none, tools replayed={'metric_stress_validator': True, 'schema_provenance_auditor': True}, logistic macro-F1=0.9338.

This is not an official benchmark reproduction. No official train/test split or exact paper protocol was reproduced. The value of this result is the deeper toolchain evidence: provenance checks, duplicate-risk visibility, metric stress controls, bounded extension testing, and replay.
