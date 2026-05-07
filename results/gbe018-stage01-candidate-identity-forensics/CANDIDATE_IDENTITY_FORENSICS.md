# Candidate Identity Forensics

Candidate: `GBE-CAND-018`.

Current promoted claim: Machine-checkable evidence-triad completeness appears to predict benchmark/protocol reproducibility risk better than headline benchmark popularity in bounded public metadata and replay probes.

Forensic decision: the current candidate identity is not clean enough for immediate deep validation. The same identifier is bound to at least two different mechanisms and appears in both rejected and surviving/promotion paths. That blocks any honest deep-validation run using the existing ID as-is.

| Evidence point | Observed artifact | Impact |
| --- | --- | --- |
| Initial candidate card | Stage 05 card says baseline leakage resistance | Does not match later evidence-triad claim |
| Death-gate file | Stage 06 rejected list marks GBE-CAND-018 as rival_theory_stronger | Promotion path conflicts with a rejection record |
| Survivor file | Stage 06 survivor list reuses GBE-CAND-018 for evidence triad alignment | Same ID carries a different mechanism |
| Promotion file | Stage 10 promotes evidence-triad completeness | Later evidence binds to a mutated claim |
| Decision file | Stage 17 calls it strongest promising_but_unvalidated seed | Downstream decision is weakened by upstream identity conflict |
