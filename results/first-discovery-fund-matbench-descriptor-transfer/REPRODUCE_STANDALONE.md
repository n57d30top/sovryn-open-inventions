# Standalone Public Reproduction

This file describes the minimal public-data reproduction path added after external review. It does not change the Product claim, FundClass, or Fund Gate result.

## What This Script Does

`reproduce_matbench_candidate.py`:

- loads the public Matbench experimental band-gap JSON;
- parses formula/target rows from the raw public source;
- computes deterministic formula-only proxy checks with no private Product state;
- replays the public-safe Product runtime scalar formulas from `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json`;
- compares those public proxy values against the Product-recorded scalars:
  - measured outcome `0.72`;
  - residual magnitude `0.21`;
  - composition/formula-size/target-family baseline `0.34`;
  - matched negative control `0.29`;
  - null/trivial-rule baseline `0.23`;
- writes `REPRODUCTION_RESULT_TABLE.md`, `MISSING_REPRODUCTION_INPUTS.md`, and `standalone_reproduction_result.json`.

## Run

From this result directory:

```bash
python3 reproduce_matbench_candidate.py
```

Optional local raw-data mode:

```bash
curl -L -o matbench_expt_gap.review.json https://huggingface.co/datasets/smgjch/Matbench/resolve/main/matbench_expt_gap.json
python3 reproduce_matbench_candidate.py --data-file matbench_expt_gap.review.json
```

## Expected Classification

The expected current classification is:

`raw_scientific_reproduction_failed_product_values_runtime_derived`

That status means:

- the public raw Matbench JSON can be fetched and parsed;
- simple public proxy baselines can be recomputed;
- the exact Product runtime scalars are replayed from the public-safe Product runtime spec;
- the Product values are classified as runtime-derived deterministic generator scalars;
- the exact Product descriptor-transfer residual is not independently reproduced from raw Matbench scientific inputs in this public package;
- public Einstein/Nobel discovery-score eligibility is false.

## Why Exact Reproduction Is Not Yet Possible

The public package does not expose the full descriptor matrix, descriptor-transfer model/training configuration, exact split/family manifest, target subset manifest, scientific residual formula, baseline implementations, or external runnable holdout/counterexample manifests that would independently reproduce the Product-recorded values from raw data. Those gaps are listed in `MISSING_REPRODUCTION_INPUTS.md`.

## No Overclaim

This script is a reproducibility repair and downgrade record. It is not external validation, not external adoption, not a stronger scientific claim, and not a new Fund result.
