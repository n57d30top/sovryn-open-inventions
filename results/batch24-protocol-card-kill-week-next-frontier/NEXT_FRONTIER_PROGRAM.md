# Next Frontier Program

Selected program: Benchmark Leakage-Risk Detection under Protocol Cards.

Domain: protocol-first benchmark reliability.

Core research question: Can Sovryn detect duplicate, group, subject, file, or feature leakage risks after a Protocol Card defines the source split and challenger splits?

Why selected: Batches 21-24 show that Protocol Cards are useful, but the next bottleneck is whether split-risk is caused by leakage-like structure, group overlap, duplicate transfer, or merely expected protocol difficulty.

Rejected alternatives:

- Protocol-Card Replay at Larger Scale: rejected for now because ambiguous cards need stronger leakage/group checks first.
- Repo/Test Reproduction with Runtime Evidence: useful but less directly connected to the current evidence chain.
- Time-Series Anomaly Negative-Control Benchmarks: deferred because protocol-card infrastructure is stronger in classification benchmarks right now.
- Claim/Evidence Execution-Backed Validation: deprioritized because prior evidence showed less execution depth.
- Method Candidate Search under Protocol-First Benchmarks: premature until leakage-risk controls are stronger.

Four weekly batch goals:

1. Build leakage-risk cards for five protocol-bearing benchmarks and execute duplicate/group-overlap checks.
2. Stress three leakage-risk hypotheses across source, random, and group/file-aware splits.
3. Deep study one target where leakage-risk or group overlap changes conclusions.
4. Kill Week: attack leakage-risk claims, retire weak helpers, and choose the next program.

Required tools: Protocol Cards, metric_stress_validator, schema/provenance packaging, container-netoff replay, small target-local leakage helpers if unavoidable.

Baseline plan: DummyClassifier, linear logistic SGD, RandomForest, duplicate-aware and group-aware negative controls.

Replay plan: fresh seed, fresh split, and container-netoff-equivalent replay after data provisioning.

Stop criteria: stop or narrow if leakage-risk helpers add no value beyond pandas/sklearn/groupby checks on at least three targets.

Publication criteria: every result must include source cards, protocol cards, leakage-risk evidence, baselines, negative controls, limitations, and no benchmark-win claim.
