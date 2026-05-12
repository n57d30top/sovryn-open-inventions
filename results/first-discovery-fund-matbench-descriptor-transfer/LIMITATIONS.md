# Limitations

## Public Review Status

This public package is `external_review_ready_with_major_caveats`.

The Product FundClass is preserved as `externally_review_ready_discovery_candidate`, but this Corpus repair explicitly records that the public package still needs external scientific review and stronger standalone reproducibility before it should be treated as an externally convincing materials-science result.

## Preserved Product Limitation

The Product package included this limitation:

> The evidence is bounded to generated formal object families and replayed Product artifacts.

That sentence is preserved as source evidence. It is also a caveat: the wording is not cleanly aligned with a Matbench/materials descriptor-transfer claim and should be reviewed as a possible package-generation artifact.

## Matbench Scope Limitation

For this Corpus result, the public claim remains bounded to:

- the cited Matbench/public-materials target refs;
- `matbench_descriptor_transfer_significance_generator-output-01`;
- the copied Product runtime evidence;
- the copied Product insight-closure, prediction-ledger, kill-week, and fund-draft artifacts;
- the recorded scalar outcome and residual values.

It does not claim a general law of materials descriptors, a broad benchmark improvement, or a domain-wide Matbench result.

## Reproducibility Limitation

The package now supports public inspection of the Product evidence without private local `.sovryn` paths and includes `reproduce_matbench_candidate.py`, a standalone public raw-data proxy check. The script loads the public Matbench experimental band-gap JSON and computes deterministic formula-only proxy checks.

The script does not exactly recompute the Product residual, all baselines, holdout, and counterexamples from raw public Matbench data. Exact reproduction remains blocked by the missing inputs listed in `MISSING_REPRODUCTION_INPUTS.md`.

## Evidence Limitation

The public package exposes copied Product artifacts and public source URLs. It does not provide:

- a full descriptor matrix;
- a complete model configuration;
- a train/test split file;
- the exact residual formula and score normalization;
- executable baseline implementations for Product scalars `0.34`, `0.29`, and `0.23`;
- a statistical uncertainty interval;
- a p-value or confidence interval;
- an independently authored reviewer report.

## Gate Limitation

The Product package records:

- Domain scientific significance pressure failed gate: `no_anti_discovery_claim_text`.
- The pre-lift insight artifact explicitly said it was not Fund evidence before claim-lift.
- The final Product Fund Gate passed after a stable claim-lift path, but external reviewers should inspect this transition carefully.

## No Overclaim

- No Nobel claim.
- No Einstein-level claim.
- No breakthrough claim.
- No external validation claim.
- No external adoption claim.
- No legal, medical, wet-lab, or unsafe capability claim.
- No stronger interpretation beyond the bounded package evidence is made.

## Required Future Repair

Before the candidate should be treated as scientifically convincing outside Sovryn, a reviewer or future package should:

- independently recompute the residual from public Matbench data;
- supply or reconstruct the exact descriptor-transfer feature matrix, split manifest, residual formula, and baseline implementations;
- publish exact feature construction and split definitions;
- publish model configuration or computation code;
- quantify uncertainty and effect size stability;
- show that controls do not absorb the residual under reviewer-selected splits;
- clarify or remove the formal-object/package-generation wording if it is not part of the Matbench evidence path.
