# Review Score Contract

Candidate: `DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001`

Current class: `pipeline_fund_candidate`

Current score effect: none for discovery-scored readiness.

## Invariants

- `fundFound` must remain false until a discovery-scored Fund Gate authorizes
  notification.
- `notificationAllowed` must remain false for this package as currently
  classified.
- `countsForDiscoveryScore` must remain false unless a future Product run
  creates a separate, valid discovery-scored state from external evidence.
- Public replay is inspectability evidence, not external validation.

## Score-Impacting Evidence Requirements

A review or reproduction can affect readiness only if all conditions hold:

1. The record is public or source-verifiable.
2. The record has a source receipt.
3. The reviewer/reproducer is independent of the Product run.
4. The reproduction loads public data and does not rely on Product `.sovryn`
   state.
5. The decision is supportive enough for the bounded methodology claim.
6. The record does not introduce overclaiming.

## Decision Mapping

| External decision                                         | Score impact                                                     |
| --------------------------------------------------------- | ---------------------------------------------------------------- |
| `accept` with independent reproduction and source receipt | eligible for Product intake review                               |
| `minor_revision` with source receipt                      | eligible for limited readiness evidence, not automatic promotion |
| `major_revision`                                          | no positive readiness increase                                   |
| `reject`                                                  | no positive readiness increase; may downgrade                    |
| private/unreceipted/local review                          | no score impact                                                  |

Any future promotion still requires unchanged Product gates. This contract does
not weaken Fund Gate logic.
