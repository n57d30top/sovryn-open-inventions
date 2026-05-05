# Sovryn Open Inventions

This repository is the public corpus for Sovryn Open Inventions, Defensive Publications, and Open Source Research Artifacts.

Sovryn produces autonomous open-research artifacts, defensive publications, and open-source research evidence. It is not a patent filing system and does not provide legal patentability, legal novelty, or freedom-to-operate opinions.

## Public Corpus

- Static corpus site: [public-corpus/index.html](public-corpus/index.html)
- Machine-readable corpus: [public-corpus/corpus.json](public-corpus/corpus.json)
- Search index: [public-corpus/search-index.json](public-corpus/search-index.json)
- Results API: [public-corpus/api/results.json](public-corpus/api/results.json)
- Showcase page: [public-corpus/showcase.html](public-corpus/showcase.html)
- Computational science studies: [public-corpus/science.html](public-corpus/science.html)
- Science studies API: [public-corpus/api/science-studies.json](public-corpus/api/science-studies.json)

## Public Beta Reading Path

Start with [public-corpus/showcase.html](public-corpus/showcase.html), then open
the result README, SHOWCASE.md, REPRODUCE.md, LIMITATIONS.md, EXAMPLES.md, and
FALSIFICATION.md. The corpus is intended for public beta review and reproducible
research inspection, not for legal patent conclusions or operational deployment
without human review.

## Showcase Results

- #1: [Molecular Record Auditor for Chemistry-Style Dataset Quality](results/chemistry-record-auditor-tool-v2-v3/) — chemistry-data-quality, showcase
- #2: [Energy Usage Anomaly Auditor](results/energy-usage-anomaly-auditor-v3/) — energy-data-quality, showcase
- #3: [Patch Risk Auditor](results/patch-risk-auditor-v3/) — software-supply-chain, showcase

Each showcase result includes SHOWCASE.md, METHOD.md, REPRODUCE.md,
LIMITATIONS.md, and EXAMPLES.md. These documents explain the problem, method,
custom tool, tests, reproduction path, source evidence summary, counter-evidence,
and safety scope in human-readable language.

## Results

- [Does unit-normalization plus provenance scoring improve detection of inconsistent chemistry-style molecular property records compared with unit normalization alone?](results/chemistry-data-quality-does-unit-normalization-plus-provenance-scoring-improve-detection-of-inco/) — science_study, autopublished, chemistry-data-quality-does-unit-normalization-plus-provenance-scoring-improve-detection-o, chemistry-data-quality
- [Molecular Record Auditor for Chemistry-Style Dataset Quality](results/chemistry-record-auditor-tool/) — good, superseded, chemistry-record-auditor-tool, chemistry-data-quality
- [Molecular Record Auditor for Chemistry-Style Dataset Quality](results/chemistry-record-auditor-tool-v2/) — good, superseded, chemistry-record-auditor-tool, chemistry-data-quality
- [Molecular Record Auditor for Chemistry-Style Dataset Quality](results/chemistry-record-auditor-tool-v2-v2/) — good, superseded, chemistry-record-auditor-tool, chemistry-data-quality
- [Molecular Record Auditor for Chemistry-Style Dataset Quality](results/chemistry-record-auditor-tool-v2-v3/) — good, showcase, chemistry-record-auditor-tool, chemistry-data-quality
- [Corpus Deduplication for Defensive Publications](results/corpus-deduplication/) — good, needs_revision, corpus-deduplication, open-invention-corpus
- [Do provenance-aware anomaly scoring methods reduce false positives in synthetic energy-usage datasets compared with simple threshold baselines?](results/energy-data-quality-do-provenance-aware-anomaly-scoring-methods-reduce-false-positives-in-synthe/) — science_study, autopublished, energy-data-quality-do-provenance-aware-anomaly-scoring-methods-reduce-false-positives-in-, energy-data-quality
- [Energy Usage Anomaly Auditor](results/energy-usage-anomaly-auditor/) — good, superseded, energy-usage-anomaly-auditor, energy-data-quality
- [Energy Usage Anomaly Auditor](results/energy-usage-anomaly-auditor-v2/) — good, superseded, energy-usage-anomaly-auditor, energy-data-quality
- [Energy Usage Anomaly Auditor](results/energy-usage-anomaly-auditor-v3/) — good, showcase, energy-usage-anomaly-auditor, energy-data-quality
- [Replayable Evidence Chain for Autonomous Research Agents](results/evidence-chain/) — good, superseded, evidence-chain, open-invention-corpus
- [Replayable Evidence Chain for Autonomous Research Agents](results/evidence-chain-v2/) — good, needs_revision, evidence-chain, open-invention-corpus
- [Patch Risk Auditor](results/patch-risk-auditor/) — good, superseded, patch-risk-auditor, software-supply-chain
- [Patch Risk Auditor](results/patch-risk-auditor-v2/) — good, superseded, patch-risk-auditor, software-supply-chain
- [Patch Risk Auditor](results/patch-risk-auditor-v3/) — good, showcase, patch-risk-auditor, software-supply-chain
- [Policy-Gated Toolchain Installation Protocol](results/toolchain-policy/) — good, needs_revision, toolchain-policy, node-toolchain-policy

## Corpus Lifecycle

Results can be marked demo_pilot, draft, dry_run_ready, autopublished, showcase,
needs_revision, superseded, or blocked. Old result folders are retained for
auditability; newer version-group entries supersede earlier iterations.

## Autopublish

Results in this corpus were published automatically only after automated quality, replay, safety, reliability, public-hygiene, and publication dry-run gates. Human interpretation is still required before operational use.
