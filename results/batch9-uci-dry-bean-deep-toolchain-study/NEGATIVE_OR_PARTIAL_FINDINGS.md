# Negative Or Partial Findings

- No official benchmark protocol was reproduced; this is a controlled baseline study.
- The dataset was loaded as a single public table without an official split, so split sensitivity remains a limitation.
- `schema_provenance_auditor` needed Batch 9 wrapper context to identify the target column and class distribution.
- The class-weight balanced LogisticRegression extension decreased macro-F1 on the primary split and was rejected as an improvement claim.
- Duplicate rows were found, but this does not prove invalid data without row-level provenance.
