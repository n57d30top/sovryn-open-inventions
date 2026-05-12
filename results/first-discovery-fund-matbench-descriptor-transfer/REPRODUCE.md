# Reproduce

This package supports two review modes:

1. public artifact inspection from the Corpus result, with no private local `.sovryn` state required;
2. full Product replay, if the reviewer also has the Product repository and wants to re-run the internal closure commands.

No step below creates a new Fund state or changes the Product Fund Gate.

## Public Artifact Inspection

From a fresh clone of the Corpus repository:

```bash
git clone https://github.com/n57d30top/sovryn-open-inventions.git
cd sovryn-open-inventions/results/first-discovery-fund-matbench-descriptor-transfer
```

Inspect the classification and copied evidence:

```bash
jq '{totalRefs, counts, internalNotCopied: (.internalProductRefsNotCopied | length), unresolved: (.unresolvedOrWeakRefs | length)}' EVIDENCE_REF_CLASSIFICATION.json
jq '{outputId: .output.outputId, measuredVariable: .output.measuredVariable, measuredOutcome: .output.measuredOutcome, residualMagnitude: .output.residualMagnitude, baselineResults: .output.baselineResults}' copied-product-evidence/runtime-evidence-output-01.json
jq '[.executions[] | {testType, passed, observation, caveats}]' copied-product-evidence/insight-closure.json
jq '{predictionCount: (.predictions | length), supported: ([.predictions[] | select(.supportedCandidateMechanism == true)] | length), unsupportedOrNegative: ([.predictions[] | select(.supportedCandidateMechanism == false)] | length), nonObvious: ([.predictions[] | select(.nonObvious == true)] | length)}' copied-product-evidence/frozen-prediction-ledger.json
```

Expected public-inspection values:

- total refs classified: `62`
- internal Product refs not copied: `0`
- unresolved or weak refs: `0`
- runtime evidence output id: `matbench_descriptor_transfer_significance_generator-output-01`
- measured outcome: `0.72`
- residual magnitude: `0.21`
- prediction count: `12`
- supported candidate mechanism predictions: `9`
- unsupported or negative/control predictions: `3`
- non-obvious predictions: `4`

## Public Raw Source Check

The public Matbench source named by the package can be fetched independently:

```bash
curl -L -o matbench_expt_gap.review.json https://huggingface.co/datasets/smgjch/Matbench/resolve/main/matbench_expt_gap.json
shasum -a 256 matbench_expt_gap.review.json
```

Compare the source availability and receipt context against:

```bash
jq '{sourceRef, sourceReceipt, rawTargetCount, measuredVariable, targetOutcome, measuredOutcome, residualMagnitude, baselineResults, holdoutPath, replayPath}' copied-product-evidence/matbench-source-cache.json
```

Important caveat: this public package does not yet include a standalone script that recomputes the Product residual from the downloaded raw JSON. The raw-source check verifies source access and receipt context; it does not by itself independently validate the scientific claim.

## Reviewer Tables

Inspect the reviewer-facing tables:

```bash
sed -n '1,220p' DATASET_AND_TARGET_TABLE.md
sed -n '1,220p' BASELINE_RESULTS_TABLE.md
sed -n '1,220p' RIVAL_THEORY_RESULTS_TABLE.md
sed -n '1,220p' HOLDOUT_RESULTS_TABLE.md
sed -n '1,220p' COUNTEREXAMPLE_RESULTS_TABLE.md
sed -n '1,220p' REPLAY_RESULTS_TABLE.md
sed -n '1,220p' EFFECT_SIZE_AND_RESIDUAL_TABLE.md
```

## Product Replay Path

If a reviewer also has the Product repository, the original internal replay path was:

```bash
npm run build
npm test
node dist/cli.js discover-daemon generator-fund-closure --json
node dist/cli.js discover-daemon generator-claim-lift-propose --json
node dist/cli.js discover-daemon generator-claim-lift --json
```

That path relies on Product `.sovryn` state. This Corpus repair copies the specific state needed for public inspection into `copied-product-evidence/`, so a reviewer can inspect the package without those local paths.

## Replay Status

The copied Product package records replay support as package-bound and nonfatal:

- `copied-product-evidence/insight-closure.json#replay_feasibility_test`
- `copied-product-evidence/pre-lift-reproduce.md#replay`
- `copied-product-evidence/runtime-evidence-output-01.json`

External-review caveat: package-bound replay is not the same as independent external reproduction from raw data and fresh code. A stronger future package should add a minimal script that recomputes the residual, baselines, and holdout from the public Matbench JSON.
