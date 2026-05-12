# Rival Theory Results Table

| Rival theory | Product-recorded pressure result | Evidence ref | Status for external review |
| --- | --- | --- | --- |
| Composition, formula size, element prevalence, target-family identity, split leakage, or shuffled-target controls explain the residual. | `rivalWeakened: true` in runtime evidence. | `copied-product-evidence/runtime-evidence-output-01.json` | Weakened or scoped internally; not eliminated globally. |
| Source-family documented behavior explains the residual. | `sourceFamilyDocumentedSignal: false` in runtime evidence. | `copied-product-evidence/runtime-evidence-output-01.json` | Needs domain reviewer check against Matbench/Materials-ML literature. |
| Known/trivial signal explains the residual. | `knownTrivialSignal: false` in runtime evidence. | `copied-product-evidence/runtime-evidence-output-01.json` | Needs independent novelty review. |
| Pre-lift anti-discovery wording prevents domain significance. | Domain significance assessment failed `no_anti_discovery_claim_text` before claim-lift. | `copied-product-evidence/pre-lift-claim-evidence-bindings.json` | Major caveat; reviewer should inspect the claim-lift transition. |

