# Replay Results Table

| Replay item | Product-recorded status | Evidence ref | Reviewer caveat |
| --- | --- | --- | --- |
| Runtime holdout/replay availability | true | `copied-product-evidence/runtime-evidence-output-01.json` | Indicates a Product replay path exists. |
| Insight closure replay gate | passed | `copied-product-evidence/insight-closure.json#replay_feasibility_test` | Package-bound replay gate, not independent external replay. |
| Pre-lift replay ref | present | `copied-product-evidence/pre-lift-reproduce.md#replay` | Copied Product replay text. |
| Public source replay path | download Matbench public JSON, parse formulas, rerun composition baselines and residual scoring | `copied-product-evidence/matbench-source-cache.json` | This package does not yet include the standalone script to execute that path. |
| Public inspection replay | `jq` over copied evidence files | `REPRODUCE.md` | Lets reviewers inspect Product-recorded values without private `.sovryn` state. |

