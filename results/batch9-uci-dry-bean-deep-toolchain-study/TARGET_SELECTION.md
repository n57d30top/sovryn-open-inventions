# Target Selection

Selected target: UCI Dry Bean Dataset.

Why this target was selected:

- It is public and safe for computational analysis.
- It is a tabular classification dataset with real data, 13,611 rows, 16 numeric features, and 7 classes.
- It fits the Batch 8.5 decision to promote dataset and metric validation as the next deep toolchain direction.
- It creates useful pressure for both required tools: schema/provenance auditing and metric stress validation.
- It has measurable baseline availability through standard sklearn classifiers without requiring private or operationally unsafe data.

Rejected alternatives:

- UCI Rice Cammeo/Osmancik: good fallback, but binary and less demanding for multiclass metric stress.
- UCI Breast Cancer Wisconsin Diagnostic: public and measurable, but not selected because a safe agricultural target was available.
- UCI Optical Recognition of Handwritten Digits: useful benchmark, but less aligned with the Batch 8.5 dataset/provenance direction than Dry Bean.

External usefulness:

The result is useful for evaluating whether Sovryn's dataset and metric tools can move from shallow reuse to deep target analysis. The target is not used for a benchmark-win claim.
