# Preregistration

Research question: Can simple multi-sensor vote challengers beat the best train-selected single-sensor baseline on held-out occupancy detection?

Metrics fixed before evaluation:
- precision
- recall
- F1
- balanced accuracy
- wins/losses/ties against best baseline

Kill criteria:
- candidate does not beat best baseline F1
- candidate improves only by sacrificing balanced accuracy
- holdout leakage detected

Publication criteria: publish only if the result includes external target binding, concrete metrics, failures/losses, limitations, reproducibility instructions, and public hygiene pass.
