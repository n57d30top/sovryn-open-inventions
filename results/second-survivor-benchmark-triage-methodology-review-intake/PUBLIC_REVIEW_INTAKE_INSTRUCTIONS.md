# Public Review Intake Instructions

This package is ready for real external methodology review intake with major
caveats. It is not discovery-scored and does not claim external validation.

## Required External Review Record

A score-impacting review must provide:

- an external public URL,
- a source receipt generated from that URL,
- reviewer decision: `accept`, `minor_revision`, `major_revision`, or `reject`,
- independent reproduction status,
- methodology novelty assessment,
- comparison against relevant benchmark-triage or benchmark-methodology methods,
- explicit overclaim check.

## Source Receipt Command

Use Product Sovryn only after the external public URL exists:

```bash
sovryn nobel-readiness external-review-source-receipt --url <reviewSourceRef> --json
```

Then ingest with:

```bash
sovryn nobel-readiness external-review-intake --json
```

## Score Rule

Only a real external public URL plus valid source receipt can affect readiness
score. Local notes, private messages, synthetic reviewer panels, manifest replay,
or Product-owned self-review cannot increase Einstein/Nobel readiness.

## Non-Scoring Outcomes

These outcomes do not create `FUND_FOUND`:

- package completeness,
- public replay by Sovryn,
- reviewer quickcheck by Sovryn,
- internal audit pass,
- Product Fund Gate pass for `pipeline_fund_candidate`,
- major revision,
- rejected review,
- private or unverifiable review.
