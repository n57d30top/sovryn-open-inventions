# Limitations

- This is not a full official benchmark reproduction or paper reproduction.
- Source-described train/test files were followed where available, but historical benchmark context may include details not encoded in the archive.
- Letter Recognition uses a documentation-order split; that is approximated rather than file-reproduced.
- Shuttle required pre-provisioning an uncompressed train sidecar for network-off container replay.
- RandomForest on Shuttle was fit on a stratified 20,000-row training subset to keep execution bounded; Logistic/linear source-vs-random comparisons were the primary split-risk signal.
- `metric_stress_validator` is support evidence, not proof of leakage absence.
- `schema_provenance_auditor` is packaging-only here.
