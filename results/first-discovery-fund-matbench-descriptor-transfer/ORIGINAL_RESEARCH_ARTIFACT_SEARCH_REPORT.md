# Original Research Artifact Search Report

This report records the Product-State search for the original Matbench descriptor-transfer research artifacts behind candidate `DISCOVERY-LIFT-INSIGHT-HARD-GEN-MATBENCH-DESCRIPTOR-TRANSFER-SIGNIFICAN-74933C45D6DB`.

## Search Scope

- Product repo: local Sovryn Product repository
- Product commit inspected: `48afba2890e00947d9f555cf3ac9db637e6dff91`
- Product paths searched: `.sovryn`, `src`, `tests`, `docs`
- Public-safe bundle inspected: `raw-reproduction-bundle/`
- Search terms included: `descriptor matrix`, `feature matrix`, `featurizer`, `matminer`, `pymatgen`, `model config`, `training config`, `split manifest`, `family labels`, `target subset`, `residual formula`, `baseline implementation`, `holdout manifest`, `counterexample manifest`, `replay manifest`, `matbench_descriptor_transfer`, `74933C45`, `matbench_expt_gap`.

## Product Artifacts Found

| Artifact class | Found? | Public package location | Interpretation |
| --- | --- | --- | --- |
| Product runtime evidence | yes | `raw-reproduction-bundle/product-state/discovery-daemon/generator-families/runtime-evidence/matbench_descriptor_transfer_significance_generator-output-01.json` | Records `0.72`, `0.21`, `0.34`, `0.29`, `0.23` as runtime evidence. |
| Product source-cache receipt | yes | `raw-reproduction-bundle/product-state/discovery-daemon/discovery-anchor-run/source-cache/DISC-ANCHOR-MATBENCH-DIELECTRIC-GAP.json` | Records public Matbench source receipt and aggregate metrics, but not row-level raw-data computation inputs. |
| Product evidence packages | yes | `raw-reproduction-bundle/product-state/discovery-daemon/evidence-packages/` | Reviewer package and claim bindings exist. |
| Product candidate drafts and Fund Gate artifacts | yes | `raw-reproduction-bundle/product-state/discovery-daemon/fund-candidate-drafts/`, `fund-gate-results.json` | Historical Product Fund path is inspectable. |
| Product generator source code | yes | Product `src/core/discovery-daemon/discovery-daemon-service.ts` | Shows the Matbench output values are deterministic profile scalars for generator ordinal `1`. |

## Original Scientific Inputs Not Found

| Required input | Status | Consequence |
| --- | --- | --- |
| Descriptor matrix / feature definition | not found as original Product artifact | Exact raw-data descriptor-transfer recomputation cannot be performed. |
| Pymatgen/matminer/ASE featurizer config | not found | Feature construction cannot be replayed as originally claimed. |
| Model and training config | not found | The path from features to measured outcome `0.72` cannot be reconstructed as a scientific model. |
| Exact train/validation/holdout split and family labels | not found | Holdout and target-family pressure cannot be independently replayed. |
| Target subset manifest | not found | Product source-cache records `rawTargetCount: 300`, but the row-level selection was not retained. |
| Raw-data residual formula / normalization | not found | Residual `0.21` cannot be derived from public raw Matbench data. |
| Exact baseline implementations for `0.34`, `0.29`, `0.23` | not found | Baseline scalars cannot be independently recomputed scientifically. |
| External runnable holdout/counterexample manifests | not found as executable manifests | Holdout/counterexample pressure remains Product-state evidence, not standalone raw-data reproduction. |

## Deterministic Runtime Source

The Product source contains the Matbench generator profile in `generatorOutcomeProfile()`:

- `measuredOutcome`: `0.71 + ordinal / 100` for born outputs
- `residualMagnitude`: `0.22 - ordinal / 100` for born outputs
- `composition_formula_size_target_family_baseline`: `0.34`
- `matched_negative_control`: `0.29`
- `null_or_trivial_rule`: `0.23`

For output ordinal `1`, this exactly yields the Product-recorded values `0.72`, `0.21`, `0.34`, `0.29`, and `0.23`.

## Conclusion

The original Product research trail is inspectable as runtime/gate state, but the original raw scientific artifacts needed for independent Matbench descriptor-transfer reproduction were not found. They either were never materialized as files or were not retained in Product `.sovryn` state.

The public package therefore includes reconstructed public raw-data proxy artifacts generated from public Matbench JSON. Those reconstructed artifacts are not the original Product artifacts and do not restore discovery-score eligibility.
