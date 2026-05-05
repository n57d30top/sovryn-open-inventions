# Experiment Design

- Experiment: sci-exp-c5bec512d93a
- Baseline: unit-normalization-only conflict detector
- Worker profile: container-netoff

## Success criteria

- candidate false-positive rate is lower than unit-normalization-only baseline
- candidate recall does not drop compared with the baseline
- result remains stable across at least three deterministic seeds

## Failure criteria

- unit-normalization-only baseline has equal or lower false-positive rate with comparable recall
- candidate treats low-confidence equivalence-map matches as full canonicalization
- candidate relies on unsupported general cheminformatics claims
