# Batch 14 Protocol Risk Report

Batch 14 executed Week 2 of the Protocol-First Benchmark Validation and Split-Risk Program.

What ran:

- 4 public UCI targets selected.
- 3 new targets relative to Batch 13.
- 4 real public datasets loaded.
- 3 `protocol_reproduced` targets and 1 `protocol_approximated` target.
- 4 stratified-random challenger splits.
- 4 baseline comparison sets.
- 4 metric stress validations.
- 4 fresh-seed replays.
- 1 network-off container replay covering all four targets.

Main answer:

Yes. Batch 14 found protocol-first evaluation still changes conclusions across 4 targets; 2 targets reached high or severe split-risk severity, and 1 target introduced documentation-order protocol ambiguity. Highest risk came from class imbalance, documentation-only order splits, and source train/test files whose random challengers substantially changed macro-F1.
