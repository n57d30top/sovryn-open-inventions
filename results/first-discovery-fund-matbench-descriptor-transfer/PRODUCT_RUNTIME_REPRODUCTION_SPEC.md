# Product Runtime Reproduction Spec

This file documents the public-safe Product runtime scalar replay for the Matbench candidate. It does not strengthen the scientific claim and does not claim external validation. The raw scientific reproduction repair classifies these values as runtime-derived deterministic generator scalars, not raw-data-derived scientific outputs.

## Scope

The spec can exactly reproduce the Product-recorded runtime scalars for:

- output id: `matbench_descriptor_transfer_significance_generator-output-01`
- measured outcome: `0.72`
- residual magnitude: `0.21`
- composition/formula-size/target-family baseline: `0.34`
- matched negative control: `0.29`
- null/trivial-rule baseline: `0.23`

It cannot independently reproduce the scientific descriptor-transfer residual from raw Matbench data.

## Source

- Source Product commit: `48afba2890e00947d9f555cf3ac9db637e6dff91`
- Product code branch: `src/core/discovery-daemon/discovery-daemon-service.ts#matbench_descriptor_transfer_significance_generator`
- Public spec: `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json`

## Runtime Formula

For `matbench_descriptor_transfer_significance_generator-output-01`, the final numeric suffix gives `ordinal = 1`.

The Product branch defines `born = ordinal <= 2`.

For born outputs:

| Quantity | Formula | Output-01 value |
| --- | --- | ---: |
| measured outcome | `0.71 + ordinal / 100` | `0.72` |
| residual magnitude | `0.22 - ordinal / 100` | `0.21` |
| composition/formula-size/target-family baseline | `0.34` | `0.34` |
| matched negative control | `0.29` | `0.29` |
| null/trivial-rule baseline | `0.23` | `0.23` |

## Interpretation

This resolves the Product-runtime scalar reproduction gap: a reviewer can replay how the copied Product package produced the scalar values.

It does not resolve the raw scientific reproduction gap. The Product artifacts and public package still do not contain the descriptor matrix, featurizer config, model config, exact split manifest, target subset manifest, raw-data residual formula, baseline implementations, or external runnable holdout/counterexample manifests needed to reproduce the scientific claim from the Matbench JSON alone.

## Public Review Status Impact

Because exact raw-data scientific reproduction failed, the public package status is downgraded to:

`not_external_review_ready_raw_scientific_reproduction_failed`

The public FundClass is `not_discovery_scored_raw_reproduction_failed`, and public Einstein/Nobel discovery-score eligibility is `false`.
