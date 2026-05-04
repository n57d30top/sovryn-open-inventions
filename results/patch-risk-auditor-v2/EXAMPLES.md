# Examples: Patch Risk Auditor

## What This Catches

- Synthetic dependency additions that deserve review.
- Install-script or package metadata changes in toy repository examples.
- Test-impact mismatches where changed code is not covered by expected tests.
- Weak patch provenance that lowers confidence.

## What This Should Not Overclaim

- It does not exploit real repositories or publish attack payloads.
- It does not prove that a pull request is malicious.
- It is a defensive risk-prioritization method for synthetic examples.

## Why This Is Useful

The result is useful because it turns vague patch concern into reproducible, inspectable defensive signals that reviewers can challenge.

These examples are bounded demonstrations for public research artifacts. They
are not claims of production coverage, legal novelty, or freedom-to-operate.
