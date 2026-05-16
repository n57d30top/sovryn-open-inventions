# Major-Revision Critique Summary

Decision: `major_revision`

The reviewer reproduced the public replay path as reported, but did not accept
the package as a discovery-scored methodology contribution.

## What The Review Supports

- The public reproducer can be run with network access.
- The reviewer quickcheck can be run.
- 7/7 replay rows are reported as validated.
- The replay status remains
  `public_raw_replay_reproduced_with_rounding_caveat`.
- The package is reviewable as a `pipeline_fund_candidate`.

## What The Review Does Not Support

- No discovery-scored methodology contribution is accepted.
- No external validation is recorded.
- No higher readiness claim is allowed.
- No `FUND_FOUND` state is allowed.

## Required Revisions

1. Checklist vs methodology concern:
   Show that receipt-first triage has a decision rule and measured value beyond
   a documentation checklist.
2. Weak reject-all comparison:
   Demonstrate that the method retains useful candidates and improves survivor
   yield, not only rejects weak claims.
3. Holdout policy justification:
   Define when group, time, entity, recurrence, or repeated-split holdouts are
   required and why.
4. Negative control weakness:
   Add negative controls that can actually falsify leakage, metric, label, or
   split claims.
5. Shallow rival closure:
   Make rival explanations measurable and close or preserve them explicitly.
6. Missing comparative ablations:
   Compare full receipt-first triage against ablated variants and existing
   benchmark-audit practices.

## Blocking Classification

Current blocker: `major_revision_public_receipt_missing_and_method_value_unproven`
