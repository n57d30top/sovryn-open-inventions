# Next Research Direction

The next research program should keep using the toolchain, but only under stricter anti-hype rules:

1. Every tool run must include a simple-baseline dominance check.
2. Schema/provenance tools must declare whether pandas can reproduce the raw finding.
3. Metric tools must declare whether sklearn can reproduce the base metrics.
4. Repo-test tools must distinguish static inventory, pytest collection, and runtime execution.
5. Deep targets should prefer official splits or source-provided protocols.
6. Tool usefulness claims should separate discovery value from packaging/reproducibility value.

Recommended Batch 11 direction:

Run a multi-target dataset-and-metric-validation program in one domain, but require each target to answer:

What did the custom tool reveal beyond the declared simple baseline?
