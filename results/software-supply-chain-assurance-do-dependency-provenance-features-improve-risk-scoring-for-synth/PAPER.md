# Scientific Report: Do dependency-provenance features improve risk scoring for synthetic AI-generated pull requests compared with diff-pattern-only baselines?

## Abstract

This bounded computational-science study tests a hypothesis with synthetic, public-safe data, generated instruments, baseline comparison, statistical analysis, replication, and falsification. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion.

## Research question

Do dependency-provenance features improve risk scoring for synthetic AI-generated pull requests compared with diff-pattern-only baselines?

## Hypotheses

- A provenance-aware anomaly scoring method will reduce false positives on weather-related normal high-usage records compared with a simple threshold baseline.
  - Null hypothesis: A provenance-aware anomaly scoring method will not reduce the false-positive rate compared with a simple threshold baseline on the same synthetic energy-usage records.
- Combining provenance scoring with missing-interval and duplicate-record checks will improve dataset-quality triage compared with anomaly scoring alone.
  - Null hypothesis: Adding provenance, missing-interval, and duplicate-record checks will not improve dataset-quality triage compared with anomaly scoring alone.

## Methods

The study uses deterministic generated datasets, safe software instruments, Node Alpha execution evidence, and explicit gates. Claims remain bounded to the generated evidence.

## Dataset

Use three deterministic synthetic energy-usage datasets with labeled normal cases, weather-related high usage, missing intervals, duplicates, weak provenance records, and true anomaly spikes.

## Instruments

- threshold-baseline-detector
- provenance-aware-energy-detector
- experiment-runner

## Baselines

simple threshold baseline over energy usage residuals

## Metrics

- true positives
- false positives
- true negatives
- false negatives
- precision
- recall
- false positive rate
- false negative rate

## Results

- Result label: partially_supported
- Evidence summary: The candidate detector reduced false positives on seeded synthetic energy datasets while preserving recall in this bounded alpha runtime.

## Ablations

- remove provenance score
- remove weather-normalization feature
- remove missing-interval feature

## Sensitivity

- sweep anomaly threshold from 1.5 to 3.0 standard deviations
- sweep provenance penalty weight from 0.0 to 1.0
- sweep weather-normalization weight from 0.0 to 1.0

## Replication

Replication was stable across deterministic seeds in this bounded alpha study.

## Falsification

Material failures: 0.

## Limitations

- This is a synthetic-data result, not a real-world energy claim.
- Alpha.3 analysis does not yet include independent replication or falsification.
- The result label is evidence-bound and must not be read as a causal or production-readiness conclusion.
- Literature grounding uses deterministic fixture summaries in tests.
- Query links do not count as reviewed source cards.
- Future real-source mode must bind public source cards to specific claims and limitations.
- Synthetic fixture-backed evidence is not a substitute for independent real-source replication.

## Safety scope

- Domain: software-supply-chain-assurance
- Risk: low
- Blocked methods: wet-lab protocols, hazardous synthesis guidance, biological optimization, exploit development, medical treatment recommendations

## Reproducibility instructions

Run the study commands or the campaign command in a fresh Sovryn repo. Recompute hashes from the JSON artifacts and inspect Node Alpha execution evidence before interpreting the result.

## Next questions

- Does the provenance-aware detector reduce false positives on public non-sensitive aggregate energy datasets?
- How sensitive is the detector to noisy or missing provenance labels?
- Which safe counterexamples make the simple threshold baseline win over the provenance-aware method?
