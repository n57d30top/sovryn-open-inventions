# Independent Replay

Replay attempts:

1. Fresh seed and split replay.
2. Network-off container replay on preloaded public data.

Fresh seed replay:

- Primary seed: 42
- Replay seed: 2026
- Logistic macro-F1 delta replay minus primary: 0.0036
- RandomForest macro-F1 delta replay minus primary: 0.0039

Container replay:

- Replay type: container_netoff
- Network: none
- Seed: 909
- Logistic accuracy: 0.9221
- Logistic macro-F1: 0.9338
- schema_provenance_auditor replayed: True
- metric_stress_validator replayed: True

Replay supports local toolchain reproducibility for this dataset, not official benchmark reproduction.
