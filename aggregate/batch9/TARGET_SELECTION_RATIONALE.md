# Target Selection Rationale

Selected: UCI Dry Bean Dataset.

Selection reasons:

- Public safe computational target.
- Real tabular classification data.
- Multiclass setting stresses macro-F1, per-class F1, confusion matrices, and class imbalance checks.
- Schema/provenance audit is meaningful because row counts, features, duplicates, target column, and provenance limitations can be inspected.
- Baselines are measurable with standard sklearn models.

Rejected alternatives:

- UCI Rice Cammeo/Osmancik: binary and less demanding for multiclass metric stress.
- UCI Breast Cancer Wisconsin Diagnostic: not selected because a safe agricultural target was available.
- UCI Optical Recognition of Handwritten Digits: useful but less aligned with the dataset/provenance direction selected in Batch 8.5.
