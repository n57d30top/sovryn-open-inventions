# Method

This document is the external-review method repair for the public Corpus package. It does not change the Product Fund Gate result, the FundClass, or the exact Product claim.

## Exact Product Claim

The measured public computational_materials_property_data target-outcome residual for HARD-GEN-MATBENCH-DESCRIPTOR-TRANSFER-SIGNIFICANCE-GENERATOR-OUTPUT-01 has scientific significance: public materials descriptor transfer residual survives composition formula size target family split leakage and shuffled target controls changes interpretation of the bounded measured target slice by surviving baseline, rival, holdout, replay, counterexample, recurrence, and mechanism pressure checks. The scope is limited to the cited public targets and the recorded evidence package.

## Bounded Reviewer Interpretation

For review, the package should be read more narrowly:

The public package records a Product-generated Matbench/materials hard-seed and claim-lift package in which `matbench_descriptor_transfer_significance_generator-output-01` has measured outcome `0.72` and residual magnitude `0.21`. The copied Product runtime evidence says three simple controls did not explain that residual: composition/formula-size/target-family baseline `0.34`, matched negative control `0.29`, and null/trivial-rule baseline `0.23`. The package is ready for external inspection with major caveats; it is not external validation.

## Data Source

Primary public sources:

- `https://matbench.materialsproject.org/`
- `https://huggingface.co/datasets/smgjch/Matbench/resolve/main/matbench_expt_gap.json`
- `https://materialsproject.org/`

Copied Product source receipt:

- `copied-product-evidence/matbench-source-cache.json`

The Product source-cache artifact records `rawTargetCount: 300`, measured variable `holdout experimental band-gap residual after composition-only, size, and source-family baselines`, target outcome `public Matbench experimental band-gap residual after composition, size, and simple family controls`, measured outcome `1.1487`, and residual magnitude `0.6376`. That source-cache artifact is supporting context; the public Fund claim itself is bound to `matbench_descriptor_transfer_significance_generator-output-01`, whose runtime evidence is copied at `copied-product-evidence/runtime-evidence-output-01.json`.

## Target Outcome

The public candidate target is:

- output id: `matbench_descriptor_transfer_significance_generator-output-01`
- target id: `matbench_descriptor_transfer_significance_generator-target-01`
- measured variable: `matbench_descriptor_transfer_property_residual`
- measured outcome: `0.72`
- residual magnitude: `0.21`
- domain: `computational_materials_property_data`

## Descriptors And Features

The Product runtime evidence names the descriptor mechanism at the level of mechanism family, not a fully specified feature matrix:

- candidate mechanism: materials descriptor-transfer residual survives composition formula-size target-family split-leakage and shuffled-target controls
- recorded tool families: `pymatgen`, `matminer`, `ase`, `scikit-learn`, `numpy`
- rival mechanism: composition, formula size, element prevalence, target-family identity, split leakage, or shuffled-target controls explain the apparent property residual

Major caveat: the public package still does not expose a full reviewer-ready descriptor matrix, training script, split file, or model configuration. The copied Product artifacts expose the recorded runtime/gate state, not a complete independent Materials-ML experiment implementation.

## Split And Holdout Definition

The Product runtime evidence records holdout/replay availability as true. The copied source-cache artifact records a predeclared holdout path:

`predeclared Matbench family holdout: withhold formula-family groups after claim freeze and recompute composition-only residual direction on held-out families`

The copied insight-closure artifact records that holdout and replay paths were bound before InsightCandidate birth. For external review, this should be treated as holdout feasibility and package-bound support, not independent external replication.

## Baselines

The runtime evidence records three simple controls:

| Baseline | Recorded result | Explains signal |
| --- | ---: | --- |
| composition_formula_size_target_family_baseline | 0.34 | false |
| matched_negative_control | 0.29 | false |
| null_or_trivial_rule | 0.23 | false |

These are copied into `BASELINE_RESULTS_TABLE.md` and `copied-product-evidence/runtime-evidence-output-01.json`.

## Rival Explanations

The strongest recorded rival is that composition, formula size, element prevalence, target-family identity, split leakage, or shuffled-target controls explain the residual. The Product runtime evidence records `rivalWeakened: true`, and the insight closure says at least one rival mechanism remained weakened or scope-limited after second-stage pressure.

External-review caveat: weakened or scope-limited is not the same as eliminated globally. A reviewer should attempt to reproduce the residual with explicit feature matrices and independent split definitions.

## Residual Calculation And Metrics

The package exposes Product-recorded scalar outputs rather than a full statistical analysis:

- measured outcome: `0.72`
- residual magnitude: `0.21`
- second-stage residual floor noted in the birth gate: `0.1`
- baseline comparator values: `0.34`, `0.29`, `0.23`

No public p-value, confidence interval, variance estimate, or model-level error distribution is claimed by this repair pass.

## Controls

The Product package records:

- baseline controls: composition/formula-size/target-family, matched negative control, null/trivial-rule
- counterexample status: `counterexampleCollapsed: false`
- cross-source or cross-slice support: `true`
- holdout/replay path available: `true`
- nontrivial residual: `true`

Reviewer-facing tables are provided in:

- `BASELINE_RESULTS_TABLE.md`
- `RIVAL_THEORY_RESULTS_TABLE.md`
- `HOLDOUT_RESULTS_TABLE.md`
- `COUNTEREXAMPLE_RESULTS_TABLE.md`
- `REPLAY_RESULTS_TABLE.md`
- `EFFECT_SIZE_AND_RESIDUAL_TABLE.md`

## Failure Modes

The package should be downgraded or rejected if any of these occur:

- the residual is reproduced as a feature-definition or source-family artifact
- explicit composition/formula-size/target-family controls absorb the residual
- a shuffled-target or matched negative control produces the same effect
- the holdout path cannot be made independent of the claim-forming slice
- replay cannot reconstruct the recorded scalar values from public inputs
- the formal-object wording in Product limitations or prediction ledgers is found to contaminate the Matbench claim path
- external materials-domain review finds the signal already known or ordinary

## Scope

This method repair makes the public package more inspectable. It does not assert external validation, external adoption, Nobel-level status, Einstein-level status, breakthrough status, or broader materials-science truth.
