# First External Review Request

Title: Request for independent review: receipt-first triage for ML benchmark claims

This is a request for independent methodology review and/or reproduction of a bounded benchmark-triage package.

## Candidate

Candidate ID: `DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001`

Fund class: `pipeline_fund_candidate`

Meaning: a review-ready pipeline/methodology candidate that still needs independent external review before it can affect any higher-level score.

Current public status: `external_review_intake_ready_with_major_caveats`

The bounded claim is that a receipt-first benchmark triage method may help filter ML benchmark claims by requiring concrete public task IDs, raw-data replay, baselines, holdout/split checks, rival explanations, and negative controls.

The package asks whether that method is useful beyond an internal checklist or simple benchmark-audit heuristics.

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

Current local dry-run status:

`public_raw_replay_reproduced_with_rounding_caveat`

Expected rows:

`7`

Known caveat:

One OpenML-32 rounded metric differs by `0.001`; all seven replay rows are within rounding tolerance.

Expected gate fields:

- `fundFound: false`
- `countsForDiscoveryScore: false`
- `standalonePublicReplayReadsProductState: false`
- `standalonePublicReplayExternalValidation: false`

## Review Questions

1. Can you run the public reproducer?
2. Do the replay rows reproduce within rounding tolerance?
3. Is the receipt-first triage method useful beyond an internal checklist?
4. Does it differ meaningfully from existing benchmark-audit or reproducibility practices?
5. Are the baseline, holdout, rival, and negative-control interpretations technically coherent?
6. Should the candidate remain a bounded pipeline methodology package, or is a stricter downgrade required?

## Decision Options

- `accept`
- `minor_revision`
- `major_revision`
- `reject`

Only a public review URL with independent reproduction or a substantive methodology assessment can affect Sovryn's readiness score.

A rejection or major revision is useful. Please do not provide a positive review unless it is actually justified.

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
