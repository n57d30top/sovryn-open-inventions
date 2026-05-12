# Reconstructed Model Training Config

This is the public proxy model configuration used by the standalone reproduction script. It is not the original Product model/training config.

- Model: `ordinary least squares with intercept, train-only standardization, and ridge 1e-8`
- Split rule: `sha256(formula)[0:8] modulo 5 equals 0 for holdout; all other buckets train`
- Candidate columns: `element_count`, `total_atoms`, `mean_atomic_number`, `atomic_number_range`, `transition_metal_fraction`, `max_atomic_number`, `min_atomic_number`
- Machine-readable config: `RECONSTRUCTED_MODEL_TRAINING_CONFIG.json`
