# Preregistration

Research question: Can a simple skewness/entropy rule beat the best single-feature threshold baseline on a deterministic holdout split?

Metrics fixed before execution:
- precision
- recall
- F1
- accuracy
- balanced accuracy
- wins/losses/ties

Kill criteria:
- challenger F1 does not exceed best baseline F1
- holdout leakage detected
- losses hidden
