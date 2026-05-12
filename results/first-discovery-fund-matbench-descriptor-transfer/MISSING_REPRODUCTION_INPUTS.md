# Missing Reproduction Inputs

Exact independent recomputation of the Product-recorded Matbench descriptor-transfer residual is blocked by the following missing public inputs.

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

- Residual reproduced exactly: no.
- Baselines reproduced exactly: no.
- Public raw Matbench source loaded: yes.
- Public proxy checks produced: yes.
- Updated review readiness: external_review_ready_with_major_caveats; exact standalone scientific reproduction remains incomplete.
