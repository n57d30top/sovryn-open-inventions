# Replay Results Table

| Replay item | Product-recorded status | Evidence ref | Reviewer caveat |
| --- | --- | --- | --- |
| Runtime holdout/replay availability | true | `copied-product-evidence/runtime-evidence-output-01.json` | Indicates a Product replay path exists. |
| Insight closure replay gate | passed | `copied-product-evidence/insight-closure.json#replay_feasibility_test` | Package-bound replay gate, not independent external replay. |
| Pre-lift replay ref | present | `copied-product-evidence/pre-lift-reproduce.md#replay` | Copied Product replay text. |
| Public source replay path | download Matbench public JSON, parse formulas, replay Product runtime scalars, and rerun formula-only proxy checks | `reproduce_matbench_candidate.py`<br>`PRODUCT_RUNTIME_REPRODUCTION_SPEC.json`<br>`copied-product-evidence/matbench-source-cache.json` | The public script executes this path, but the raw-data descriptor-transfer scientific residual remains unreproduced without the missing scientific inputs. |
| Public inspection replay | `jq` over copied evidence files | `REPRODUCE.md` | Lets reviewers inspect Product-recorded values without private `.sovryn` state. |
