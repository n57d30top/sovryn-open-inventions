# Exact Reproduction Inputs Status

This audit separates two different meanings of "exact reproduction":

1. Product runtime scalar replay: whether the public package can reproduce the Product-recorded scalar values.
2. Raw-data scientific reproduction: whether the public package can recompute those values from public Matbench data, descriptors, models, splits, baselines, holdouts, and counterexamples.

## Product Runtime Scalar Inputs

| Input | Status | Public artifact |
| --- | --- | --- |
| generator id | resolved | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |
| output id | resolved | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |
| ordinal rule | resolved | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |
| born rule | resolved | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |
| measured-outcome formula | resolved | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |
| residual formula | resolved for Product runtime scalar replay | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |
| baseline scalar formulas | resolved for Product runtime scalar replay | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |
| runtime gate flags | resolved | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |

Result: Product runtime scalars are exactly reproducible.

## Raw-Data Scientific Inputs

| Missing input | Status | Consequence |
| --- | --- | --- |
| descriptor matrix / featurizer config | unresolved | Raw Matbench data cannot be transformed into the Product descriptor-transfer feature space. |
| model and training config | unresolved | Raw formulas cannot be mapped to the Product measured outcome `0.72`. |
| exact train/validation/holdout split and family labels | unresolved | Holdout and target-family pressure cannot be independently replayed. |
| target subset manifest | unresolved | Product source-cache count and current public JSON row count cannot be reconciled as an exact target slice. |
| raw-data residual formula and score normalization | unresolved | Product residual magnitude `0.21` cannot be recomputed from public measurements alone. |
| exact baseline implementations | unresolved | Product baseline scalars `0.34`, `0.29`, and `0.23` cannot be recomputed from public measurements alone. |
| external runnable holdout/counterexample manifests | unresolved | Holdout and counterexample pressure remains package-bound rather than independently runnable. |

Result: raw-data scientific reproduction remains incomplete.

## Status Decision

The public package should be classified as:

`package_repair_required_before_external_review`

This is a package-readiness downgrade only. It does not change the Product claim, Product FundClass, or Product Fund Gate result.
