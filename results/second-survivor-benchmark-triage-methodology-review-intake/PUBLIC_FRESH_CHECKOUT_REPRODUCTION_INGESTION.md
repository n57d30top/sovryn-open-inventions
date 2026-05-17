# Public Fresh-Checkout Reproduction Ingestion

Candidate: `DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001`

Public receipt:

- https://github.com/n57d30top/sovryn-open-inventions/issues/1#issuecomment-4470417022

## Classification

`fresh-checkout owner-authored reproduction context / public reproducibility receipt`

This is stronger than an unreceipted local run because it records public
environment details, commit, command, output file, and output hash. It is still
not an independent external review or external validation.

## Environment

- OS: Microsoft Windows 11 Pro 10.0.26200
- Node: v24.13.0
- Corpus commit: `c4f4827f9c216a189a1bc2644791c418b20fe18b`
- Checkout mode: fresh detached worktree of the public corpus repository
- Product `.sovryn` state used: no
- Command: `node reproduce_v2_100_claim_challenge.js`
- Output file: `v2_100_claim_reproducer_result.json`
- Output SHA-256:
  `90ADA17AA3D552D38012200F93E084DAE8F21277D2109EE160F848B01710DECB`

## Reported Result

- 100 claims
- 42 independent tasks/datasets
- V2: 17/17 survivors, yield `1.000`
- baseline-only: 17/25 survivors, yield `0.680`
- V2 filters 8 baseline-only false advances
- `fundFound=false`
- `discoveryScored=false`
- `notificationAllowed=false`

## Gate Impact

Public reproducibility evidence: improved.

Score-effective independent external review: no.

Reason: the GitHub receipt is owner-authored (`author_association=OWNER`) and
explicitly says it is not independent external validation.

The candidate remains `pipeline_fund_candidate`.
