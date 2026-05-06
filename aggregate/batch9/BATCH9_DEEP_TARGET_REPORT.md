# Batch 9 Deep Target Report

Result slug: `batch9-uci-dry-bean-deep-toolchain-study`.

Target: UCI Dry Bean Dataset.

Result kind: `deep_external_toolchain_reproduction_study`.

Batch 9 executed the Batch 8.5 dataset/metric-validation direction on one concrete target. The run loaded real public data, reused `schema_provenance_auditor` and `metric_stress_validator`, trained baseline models, performed metric stress tests, attempted a small extension, and replayed a meaningful phase in a network-off container.

Primary answer:

Yes, Sovryn used its self-built schema/provenance and metric-stress tools on one external scientific target. The tools revealed 68 duplicate full/feature rows, no missing/sentinel values, low shuffled-label control performance, stable but not official split-family replay, and that a class-weight extension did not improve macro-F1 on the primary split.
