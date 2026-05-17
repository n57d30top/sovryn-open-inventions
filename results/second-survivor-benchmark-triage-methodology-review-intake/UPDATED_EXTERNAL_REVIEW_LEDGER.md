# Updated External Review Ledger

No score-effective external review has been ingested.

Latest public review-history record:

| Intake ID           | Source                                     | Public URL                                                                           | Decision                  | Reproduction status                                  | Independent | Score-effective | Reason                                                                                             |
| ------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------- | ---------------------------------------------------- | ----------- | --------------- | -------------------------------------------------------------------------------------------------- |
| `REVIEW-INTAKE-006` | public accept re-review comment            | https://github.com/n57d30top/sovryn-open-inventions/issues/1#issuecomment-4470388033 | accept                    | reported V2 100-claim reproducer passed              | no          | no              | Public receipt exists, but GitHub marks author as OWNER                                            |
| `REVIEW-INTAKE-007` | public fresh-checkout reproduction context | https://github.com/n57d30top/sovryn-open-inventions/issues/1#issuecomment-4470417022 | reproduction_context_only | public fresh-checkout V2 100-claim reproducer passed | no          | no              | Public receipt includes OS, Node, commit, command, output file, and SHA-256, but is owner-authored |

The public accept re-review and fresh-checkout reproduction receipts close the
previous `public_receipt_missing` condition and improve reproducibility
evidence. They are not score-effective because the independence requirement is
still unmet.

Current package status:

- `pipeline_fund_candidate_public_fresh_checkout_reproduction_independence_missing`
- discovery-scored: no
- notification allowed: no
- `FUND_FOUND`: no
