# Raw-Data Reproducible Experiment Spec

This is a new public raw-data proxy experiment for inspectability. It does not reproduce or strengthen the Product descriptor-transfer claim.

## Source

- Source ref: `https://huggingface.co/datasets/smgjch/Matbench/resolve/main/matbench_expt_gap.json`
- Source SHA-256: `e982f9d9586ab9603c588782646870542fb2b39f915ccb0fdb513426e2ff9859`
- Records: `921`

## Feature Schema

| Feature | Definition |
| --- | --- |
| `element_count` | Number of distinct elements parsed from the composition formula. |
| `total_atoms` | Sum of stoichiometric counts parsed from the composition formula. |
| `mean_atomic_number` | Stoichiometry-weighted mean atomic number. |
| `atomic_number_range` | Maximum atomic number minus minimum atomic number in the formula. |
| `transition_metal_fraction` | Fraction of parsed stoichiometric count belonging to transition metals. |
| `max_atomic_number` | Maximum atomic number in the formula. |
| `min_atomic_number` | Minimum atomic number in the formula. |

## Split, Model, And Baselines

- Split rule: `sha256(formula)[0:8] modulo 5 equals 0 for holdout; all other buckets train`
- Model: `ordinary least squares with intercept, train-only standardization, and ridge 1e-8`
- Candidate proxy: OLS using all seven formula descriptors.
- Null baseline: train-target mean on deterministic holdout.
- Formula-size baseline: OLS using `element_count` and `total_atoms`.
- Matched negative control: all-feature OLS after deterministic train-target shuffle with seed `1729`.
- Residual definition: `candidate_proxy_holdout_r2 - max(null_r2, formula_size_r2, shuffled_target_r2)`

## Scope

This is a public raw-data formula-descriptor proxy experiment. It is not the original Product descriptor-transfer computation and must not be used to restore discovery-scored status.
