# Missing Reproduction Inputs

Product runtime scalar replay is now exact. Exact independent raw-data scientific recomputation of the Matbench descriptor-transfer residual remains blocked by the following missing public inputs.

## Resolved Product Runtime Inputs

| Input | Status | Artifact |
| --- | --- | --- |
| generator id / output id / ordinal rule | resolved | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |
| Product runtime formulas | resolved | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |
| public-safe Product artifact bundle | exported/searched | `raw-reproduction-bundle/BUNDLE_MANIFEST.json` |
| measured outcome `0.72` | reproduced | `REPRODUCTION_RESULT_TABLE.md` |
| residual magnitude `0.21` | reproduced | `REPRODUCTION_RESULT_TABLE.md` |
| baseline scalars `0.34`, `0.29`, `0.23` | reproduced | `REPRODUCTION_RESULT_TABLE.md` |
| public raw-data proxy experiment | reproducible but separate from Product claim | `RAW_DATA_REPRODUCIBLE_EXPERIMENT_RESULTS.md` |
| reconstructed public raw-data research artifacts | available but not original Product artifacts | `RECONSTRUCTED_RESEARCH_ARTIFACTS_MANIFEST.md` |

## Unresolved Raw-Data Scientific Inputs

The public-safe raw reproduction bundle was exported and searched. It contains Product runtime evidence, source receipts, generated evidence packages, candidate drafts, and review handoff artifacts. It does not contain the original scientific raw-data inputs below.

| Missing input | Why it is required |
| --- | --- |
| descriptor matrix / feature definition | The Product claim refers to a descriptor-transfer residual, but the public package does not expose the exact pymatgen/matminer/ASE feature matrix or featurizer configuration. |
| model and training configuration | The public package does not expose the model class, hyperparameters, preprocessing, target scaling, or random seed that map raw formulas to the Product measured outcome 0.72. |
| exact train/validation/holdout split and family labels | The Product evidence names composition/formula-size/target-family and holdout pressure, but the public package does not expose the exact split manifest or target-family labels. |
| residual formula and score normalization | The public package does not define the exact scalar transformation that produces residual magnitude 0.21 from model, baseline, holdout, and control outputs. |
| baseline implementation details | The Product values 0.34, 0.29, and 0.23 are recorded scalars, but their exact algorithms are not exposed as executable public code. |
| target subset manifest | The copied Product source-cache artifact records rawTargetCount 300, while the current public Matbench JSON contains more rows; the exact Product subset selection is not public. |
| external runnable holdout/counterexample manifests | The public package records holdout, replay, and counterexample status, but does not expose an independent runnable manifest for those checks. |

## Classification

- Product runtime residual reproduced exactly: yes.
- Product runtime baselines reproduced exactly: yes.
- Raw-data scientific residual reproduced exactly: no.
- Raw-data scientific baselines reproduced exactly: no.
- Public raw Matbench source loaded: yes.
- Public proxy checks produced: yes.
- Public raw-data proxy experiment fully specified: yes.
- Reconstructed public raw-data artifacts produced: yes.
- Reconstructed artifacts are original Product artifacts: no.
- Product values source classification: runtime_derived_deterministic_generator_scalars.
- Public-safe bundle decision: maximal_public_safe_export_completed_but_raw_scientific_inputs_not_found.
- Updated review readiness: not_external_review_ready_raw_scientific_reproduction_failed.
- Public discovery-score eligibility: false.
