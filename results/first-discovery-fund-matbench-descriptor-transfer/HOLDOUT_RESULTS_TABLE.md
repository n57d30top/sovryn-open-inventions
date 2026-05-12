# Holdout Results Table

| Holdout item | Product-recorded value | Evidence ref | Reviewer caveat |
| --- | --- | --- | --- |
| Holdout/replay availability | `true` | `copied-product-evidence/runtime-evidence-output-01.json` | Availability is not the same as an independent reviewer-executed holdout. |
| Insight closure holdout gate | passed | `copied-product-evidence/insight-closure.json#holdout_feasibility_test` | Closure says holdout and replay paths were bound before InsightCandidate birth. |
| Predeclared source-cache holdout path | withhold formula-family groups after claim freeze and recompute composition-only residual direction on held-out families | `copied-product-evidence/matbench-source-cache.json` | This is a path description; reviewer should execute or request the split file. |
| Product frozen prediction holdout-like families | `density_matched_chorded_cycle`, `disjoint_holdout_family_a`, `disjoint_holdout_family_b`, `solver_replay_family` | `copied-product-evidence/frozen-prediction-ledger.json` | These names expose an inconsistency: some Product prediction wording is formal-object-like and must not be overread as Matbench raw-data holdout proof. |

