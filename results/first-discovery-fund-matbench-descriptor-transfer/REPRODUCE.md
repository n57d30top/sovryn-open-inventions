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

Important caveat: the standalone script exactly replays the Product runtime scalar formulas, but it does not independently recompute the scientific descriptor-transfer residual from raw JSON. Inspection of the Product source shows those values are runtime-derived deterministic generator scalars. The raw-source check verifies source access and receipt context; exact scientific reproduction failed for this public package because the missing inputs listed in `MISSING_REPRODUCTION_INPUTS.md` are not available.

## Standalone Public-Data Proxy Check

This repair adds a minimal standalone script that can be run without private Product `.sovryn` state:

```bash
python3 reproduce_matbench_candidate.py
```

The script downloads the public Matbench experimental band-gap JSON by default, parses formulas and target values, computes deterministic formula-only proxy checks, replays the public-safe Product runtime scalar formulas, and writes:

- `REPRODUCTION_RESULT_TABLE.md`
- `MISSING_REPRODUCTION_INPUTS.md`
- `standalone_reproduction_result.json`
- `RAW_DATA_REPRODUCIBLE_EXPERIMENT_SPEC.md`
- `RAW_DATA_REPRODUCIBLE_EXPERIMENT_RESULTS.md`
- `RAW_DATA_FEATURE_MATRIX.json`
- `RAW_DATA_SPLIT_MANIFEST.json`
- `RAW_DATA_BASELINE_IMPLEMENTATIONS.md`

Current expected status:

`raw_scientific_reproduction_failed_product_values_runtime_derived`

That status is intentional and caveated. The script exactly replays Product-recorded values `0.72`, `0.21`, `0.34`, `0.29`, and `0.23` from `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json`, and it verifies public raw-data access with transparent proxy baselines. It does not independently reproduce those values from raw Matbench data because the package lacks the exact descriptor matrix, model/training configuration, split/family manifest, target subset manifest, scientific residual formula, baseline implementations, and external runnable holdout/counterexample manifests. The public package is therefore not discovery-score eligible.

## Raw-Data Proxy Reproduction

The current reproducible public computation is intentionally separate from the Product claim:

```bash
python3 reproduce_matbench_candidate.py
jq '{status, records, trainRecords, holdoutRecords, residualProxyR2Delta, productClaimReproduced, discoveryScoreEligible}' RAW_DATA_REPRODUCIBLE_EXPERIMENT_RESULTS.json
```

Expected result:

- status: `available_but_does_not_reproduce_product_scientific_claim`
- records: `921`
- train/holdout: `727` / `194`
- reproducible proxy residual R2 delta: about `0.1022`
- Product claim reproduced: `false`
- discovery-score eligible: `false`

This path makes the public raw-data computation replayable. It does not make the original Product candidate scientifically proven.

## Public-Safe Product Bundle

The full public-safe Product artifact export for this candidate is available at:

```bash
find raw-reproduction-bundle -maxdepth 3 -type f | sort
jq '{artifactCount, unsafeCopiedCount, bundleDecision, rawDataScientificReproductionSucceeded}' raw-reproduction-bundle/BUNDLE_MANIFEST.json
```

The standalone script now prefers the runtime evidence copied into that bundle:

`raw-reproduction-bundle/product-state/discovery-daemon/generator-families/runtime-evidence/matbench_descriptor_transfer_significance_generator-output-01.json`

The bundle improves inspectability of the Product evidence path. It does not supply the missing raw scientific inputs required for independent descriptor-transfer reproduction.

## Original Artifact Search And Reconstructed Inputs

Inspect the targeted Product-State search result:

```bash
sed -n '1,220p' ORIGINAL_RESEARCH_ARTIFACT_SEARCH_REPORT.md
jq '{productValuesSource, missingOriginalScientificInputs, conclusion}' ORIGINAL_RESEARCH_ARTIFACT_SEARCH_REPORT.json
```

Inspect the reconstructed public raw-data artifacts:

```bash
sed -n '1,180p' RECONSTRUCTED_RESEARCH_ARTIFACTS_MANIFEST.md
jq '{status, originalProductScientificArtifactsFound, doesNotRestoreDiscoveryScore, artifactIndex}' RECONSTRUCTED_RESEARCH_ARTIFACTS_MANIFEST.json
jq '{parser, featureSchema}' RECONSTRUCTED_FEATURIZER_CONFIG.json
jq '{model, splitRule, candidateProxyColumns, baselineModels}' RECONSTRUCTED_MODEL_TRAINING_CONFIG.json
jq '{formula, observedProxyValues}' RECONSTRUCTED_RESIDUAL_FORMULA.json
```

These reconstructed files are generated from public Matbench raw data by `reproduce_matbench_candidate.py`. They are useful for external replay of the public proxy experiment. They are not the original Product descriptor-transfer inputs and must not be treated as restored discovery evidence.

## Recreated Input Bundle

The newly recreated input is packaged as:

```bash
find recreated-input-bundle -maxdepth 1 -type f | sort
jq '{status, originalProductInputRecovered, recreatedFromPublicRawData, requiredInputClasses}' recreated-input-bundle/INPUT_MANIFEST.json
```

This bundle is the concrete new public input set. It includes `MATBENCH_EXPT_GAP_PUBLIC_RAW.json`, `SOURCE_RECEIPT.json`, and all reconstructed proxy input classes needed to rerun the public proxy experiment. It is not the old Product input and does not make the old Product claim discovery-scored.

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

The larger public-safe export in `raw-reproduction-bundle/` contains the additional relevant Product artifacts found for the candidate path. It remains a Product-state inspection bundle, not a raw-data scientific reproduction bundle.

## Replay Status

The copied Product package records replay support as package-bound and nonfatal:

- `copied-product-evidence/insight-closure.json#replay_feasibility_test`
- `copied-product-evidence/pre-lift-reproduce.md#replay`
- `copied-product-evidence/runtime-evidence-output-01.json`

External-review caveat: package-bound replay is not the same as independent external reproduction from raw data and fresh code. The standalone script now provides exact Product runtime scalar replay plus a public raw-source/proxy-baseline check, but exact descriptor-transfer scientific reproduction failed because the missing inputs listed in `MISSING_REPRODUCTION_INPUTS.md` are not available.
