# Counterexample Results Table

| Counterexample/control pressure | Product-recorded result | Evidence ref | Reviewer caveat |
| --- | --- | --- | --- |
| Runtime counterexample collapse flag | `counterexampleCollapsed: false` | `copied-product-evidence/runtime-evidence-output-01.json` | Product-recorded nonfatal status. |
| Insight closure counterexample gate | passed | `copied-product-evidence/insight-closure.json#counterexample_search` | Says counterexample/control pressure did not collapse the narrow hard-seed claim. |
| Product prediction negative/control examples | `bipartite_negative_control`, `odd_cycle_negative_control`, `trivial_invariant_null` marked unsupported/negative | `copied-product-evidence/frozen-prediction-ledger.json` | These are useful as control evidence but also reveal formal-object wording in a Matbench-labeled package. |
| Kill-week counterexample attack | nonfatal | `copied-product-evidence/kill-week-results.json` | Internal kill-week status, not external domain validation. |

