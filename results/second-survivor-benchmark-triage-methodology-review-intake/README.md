# Second-Survivor Benchmark Triage Methodology Review Intake

This public package exposes the current second-survivor benchmark-triage methodology candidate for external inspection.

It is not a discovery-scored Fund, not an external validation record, and not a claim of Nobel-readiness, Einstein-level capability, breakthrough status, external adoption, legal validity, medical use, wet-lab capability, unsafe capability, or universal truth.

## Status

- Candidate ID: `DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001`
- Result kind: `benchmark_methodology_review_intake_package`
- Public review status:
  `pipeline_fund_candidate_major_revision_public_receipt_missing`
- Product FundClass before external review: `pipeline_fund_candidate`
- Counts for discovery score: no
- Notification allowed: no
- FUND_FOUND: no
- Major-revision review reported: yes
- Public review URL / source receipt: no

## Bounded Claim Under Review

A receipt-first benchmark triage method can identify OpenML benchmark claims whose random-split performance survives public raw replay as a bounded protocol-fragility signal across OpenML-32 and at least one independent task, with nonfatal baseline, holdout, rival, and negative-control checks.

The package is bounded to the listed OpenML tasks and receipts. It does not claim a general benchmark theorem or externally accepted methodology.

## What Reviewers Can Inspect

- exact claim and falsifiers
- public OpenML task/data receipts
- dataset/task table
- baseline, rival, holdout/replay, and negative-control summaries
- methodology value tests
- independent reproducer checklist
- external methodology review intake template
- standalone public raw-data replay script and replay outputs
- current blocker and next action

## Standalone Public Replay

Run:

```bash
node reproduce_second_survivor_benchmark.js
```

The script fetches the public OpenML ARFF receipts and recomputes the displayed replay metrics without reading Product `.sovryn` state. Current result: `public_raw_replay_reproduced_with_rounding_caveat`. Six of seven tasks reproduce the displayed Product metrics exactly; OpenML-32 differs by 0.001 on displayed rounded baseline/random metrics. This remains a replay/inspectability result, not external validation.

## Major-Revision Intake

A major-revision review was reported for this candidate. The review reportedly
reproduced the public reproducer and quickcheck with network access and
validated 7/7 replay rows, but did not accept the package as a discovery-scored
methodology contribution.

The review is not score-effective because no public review URL or source receipt
is available. It is recorded as revision guidance only.

## What Would Be Needed To Improve Status

A real external public benchmark-methodology review or independent reproduction
must be ingested with a valid source receipt. A future supportive review would
need to support the bounded claim with caveats, reproduce the public replay
target set, assess the method as nontrivial and plausibly novel, and contain no
forbidden overclaim text.

Until then, the candidate remains non-notifying and cannot close Einstein/Nobel readiness.
