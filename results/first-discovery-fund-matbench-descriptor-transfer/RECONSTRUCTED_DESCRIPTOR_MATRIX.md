# Reconstructed Descriptor Matrix

The public raw-data descriptor matrix is written to `RAW_DATA_FEATURE_MATRIX.json`.

It contains seven transparent formula descriptors for every parseable public Matbench row. It is reconstructed from public raw data by `reproduce_matbench_candidate.py`; it is not the original Product descriptor-transfer matrix.

- Source ref: `https://huggingface.co/datasets/smgjch/Matbench/resolve/main/matbench_expt_gap.json`
- Source SHA-256: `e982f9d9586ab9603c588782646870542fb2b39f915ccb0fdb513426e2ff9859`
- Rows: `921`
- Train rows: `727`
- Holdout rows: `194`

Features: `element_count`, `total_atoms`, `mean_atomic_number`, `atomic_number_range`, `transition_metal_fraction`, `max_atomic_number`, `min_atomic_number`
