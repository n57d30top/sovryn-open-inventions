# First External Review Request

This is a request for independent review or reproduction of a bounded benchmark-triage methodology candidate.

## Candidate

Candidate ID: `DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001`

Fund class: `pipeline_fund_candidate`

Current public status: `external_review_intake_ready_with_major_caveats`

The bounded claim is that a receipt-first benchmark triage method can identify OpenML benchmark claims whose random-split performance survives public raw replay as a bounded protocol-fragility signal across OpenML-32 and at least one independent task, with nonfatal baseline, holdout, rival, and negative-control checks.

## What Is Not Claimed

- No external validation is claimed.
- No external adoption is claimed.
- No discovery-scored Fund is claimed.
- No Nobel, Einstein-level, breakthrough, legal, medical, wet-lab, unsafe, or universal-truth claim is made.
- Reproducing the script output is inspectability evidence, not a discovery claim by itself.

## Public Reproducer

Repository result path:

`results/second-survivor-benchmark-triage-methodology-review-intake/`

Primary reproducer:

`node reproduce_second_survivor_benchmark.js`

Quickcheck:

`node reviewer_replay_quickcheck.js`

The reproducer uses public OpenML ARFF receipts embedded in the script and does not read local Product `.sovryn` state.

## Expected Output

Expected status:

`public_raw_replay_reproduced_with_rounding_caveat`

Expected rows:

`7`

Expected gate fields:

- `fundFound: false`
- `countsForDiscoveryScore: false`
- `standalonePublicReplayReadsProductState: false`
- `standalonePublicReplayExternalValidation: false`

## Review Questions

1. Does the public reproducer run from a fresh checkout without private state?
2. Are the seven task-level replay rows understandable and sufficient to inspect the methodology claim?
3. Is the receipt-first triage method meaningfully different from reject-all, task-size, source-family-only, and simple baseline-only heuristics?
4. Are the baseline, holdout, rival, and negative-control interpretations technically coherent?
5. Should the candidate remain a bounded pipeline methodology package, or is a stricter downgrade required?

## Decision Options

- `accept`
- `minor_revision`
- `major_revision`
- `reject`

Only a public review URL with independent reproduction or a substantive methodology assessment can affect Sovryn's readiness score.

## Public Review URL Submission

Publish the review at a stable public URL, then submit the URL for intake. A score-effective review must include:

- reviewer/source identity or affiliation context,
- public review URL,
- reproduction status,
- methodology decision,
- whether the review is supportive,
- whether the reproduction is independent,
- reasons for the decision.

Until such a URL is ingested and accepted by the Review Score Contract, this package remains `pipeline_fund_candidate`, not discovery-scored.
