# Benchmark Repair Standard v0

This is a limited public standard for safer benchmark-claim framing. It is not a mature external standard.

| Rule | Name | Definition |
| --- | --- | --- |
| R1 | Protocol-card completeness gate | Require source, access method, split definition, metric, ambiguity notes, and replay plan before strong protocol-first claims. |
| R2 | Group/file/subject overlap check | When identifiers or source files exist, avoid random-only evaluation and report overlap/testability. |
| R3 | Duplicate-aware check | Compute exact feature overlap before claiming duplicate-transfer repair; do not infer leakage without overlap evidence. |
| R4 | Ambiguity gate | Block or caveat claims when multiple plausible protocol interpretations exist. |
| R5 | Rare-class metric reporting | Report accuracy, macro-F1, weighted-F1, and lowest per-class F1 when class imbalance is present. |
| R6 | Replay requirement | Bind repair evidence to replayable artifacts and document replay failure or divergence. |
