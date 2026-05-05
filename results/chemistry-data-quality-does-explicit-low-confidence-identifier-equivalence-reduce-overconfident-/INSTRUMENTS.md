# Instruments

- Study: chemistry-data-quality-does-explicit-low-confidence-identifier-equivalence-reduce-overconfident-
- Instrument count: 3
- External packages: none recorded
- Toolchain policy passed: true
- Node Alpha execution present: true
- Worker profile used: container-netoff
- No silent fallback: true

## Instrument List

- unit-normalization-baseline: Normalize Celsius/Kelvin toy values and flag large conflicts without provenance context.
- unit-provenance-chemistry-detector: Combine unit normalization, limited toy identifier equivalence, provenance score, and outlier checks.
- chemistry-experiment-runner: Run the unit-normalization baseline and unit-plus-provenance detector over seeded toy molecular-property datasets.

## Provisioning Scope

No host sudo, shell pipe installers, secrets, environment dumps, or raw worker logs are included in this public report.
