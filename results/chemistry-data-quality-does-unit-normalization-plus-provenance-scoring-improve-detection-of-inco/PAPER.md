# Scientific Report: Does unit-normalization plus provenance scoring improve detection of inconsistent chemistry-style molecular property records compared with unit normalization alone?

## Abstract

This bounded computational-science study tests a hypothesis with synthetic, public-safe data, generated instruments, baseline comparison, statistical analysis, replication, and falsification. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion.

## Research question

Does unit-normalization plus provenance scoring improve detection of inconsistent chemistry-style molecular property records compared with unit normalization alone?

## Hypotheses

- Unit normalization plus provenance scoring will reduce false positives when auditing inconsistent chemistry-style molecular-property records compared with unit normalization alone.
  - Null hypothesis: Unit normalization plus provenance scoring will not reduce false positives compared with unit normalization alone on the same synthetic chemistry-style records.
- Explicit low-confidence identifier-equivalence labels will improve audit interpretability compared with treating toy identifier variants as canonical matches.
  - Null hypothesis: Low-confidence identifier-equivalence labels will not improve interpretability compared with treating toy identifier variants as canonical matches.

## Methods

The study uses deterministic generated datasets, safe software instruments, Node Alpha execution evidence, and explicit gates. Claims remain bounded to the generated evidence.

## Dataset

Use three deterministic synthetic chemistry-style molecular-property datasets with Celsius/Kelvin pairs, limited toy identifier equivalence, weak provenance records, and known value conflicts.

## Instruments

- unit-normalization-baseline
- unit-provenance-chemistry-detector
- chemistry-experiment-runner

## Baselines

unit-normalization-only conflict detector

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
- Evidence summary: The unit-plus-provenance detector reduced false positives compared with the unit-normalization-only baseline on deterministic toy molecular-property records.

## Ablations

- remove provenance scoring
- remove limited identifier-equivalence confidence
- remove outlier residual threshold

## Sensitivity

- sweep inconsistency residual threshold
- sweep provenance penalty weight
- sweep equivalence confidence penalty

## Replication

Replication was stable across deterministic toy chemistry-style seeds.

## Falsification

Material failures: 0.

## Limitations

- This is a synthetic chemistry-style data-quality result, not a general cheminformatics claim.
- Identifier equivalence uses a limited toy map and must not be read as RDKit/OpenBabel canonicalization.
- No synthesis, drug-design, lab, or hazardous-material guidance is provided.
- Literature grounding uses deterministic fixture summaries in tests.
- Query links do not count as reviewed source cards.
- Future real-source mode must bind public source cards to specific claims and limitations.
- Synthetic fixture-backed evidence is not a substitute for independent real-source replication.

## Safety scope

- Domain: chemistry-data-quality
- Risk: low
- Blocked methods: wet-lab protocols, hazardous synthesis guidance, biological optimization, exploit development, medical treatment recommendations

## Reproducibility instructions

Run the study commands or the campaign command in a fresh Sovryn repo. Recompute hashes from the JSON artifacts and inspect Node Alpha execution evidence before interpreting the result.

## Next questions

- Does the provenance-aware detector reduce false positives on public non-sensitive aggregate energy datasets?
- How sensitive is the detector to noisy or missing provenance labels?
- Which safe counterexamples make the simple threshold baseline win over the provenance-aware method?
