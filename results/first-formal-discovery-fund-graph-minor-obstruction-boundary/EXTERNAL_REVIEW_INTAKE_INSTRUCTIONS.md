# External Review Intake Instructions

## Public Reviewer Step

1. Inspect this result directory.
2. Run or inspect `REPRODUCE.md` and `reproduce_graph_minor_candidate.py`.
3. Fill a review JSON record using `EXTERNAL_REVIEW_RECORD_TEMPLATE.json`.
4. Return the review record with a public-safe review report or URL.

## Product Intake Step

After a real returned review exists, copy the review JSON into the Product repo at:

`.sovryn/nobel-readiness/external-review-reviews/`

Then run:

`sovryn nobel-readiness external-review-intake --json`

## Score Rule

Invalid, mismatched, unresolved, not-public-safe, rejecting, non-reproduced, known/trivial, or overclaiming records cannot increase readiness. A supportive record can affect readiness only if it matches this candidate, resolves to a public-safe source, records independent reproduction, and assesses the bounded claim as nontrivial and plausibly novel.

## Current State

- External review dispatch status: `ready_to_request_external_review`
- External human review status: `awaiting_external_review`
- Valid external reviews recorded: `0`
- Supportive external reviews recorded: `0`
- External validation claimed by Sovryn: `no`
