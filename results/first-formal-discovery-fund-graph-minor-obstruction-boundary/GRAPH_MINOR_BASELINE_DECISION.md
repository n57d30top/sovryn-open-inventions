# Graph-Minor Baseline Decision

## Decision

`baseline_dominated_for_public_discovery_scoring`

## Reason

The `null_or_trivial_structural_rule` baseline is `0.438`, which is greater than the measured outcome `0.424` under the reviewer-facing directionality that higher scores indicate stronger structural signal. The Product threshold rule used `0.5` as the explanation cutoff, but the public package does not justify why a null/trivial structural score that exceeds the measured outcome should still be treated as non-explanatory.

## Consequence

The candidate should not currently count as externally review-ready discovery scoring evidence. It may remain a replayable internal/formal manifest package, but public status must be downgraded until either:

1. the 0.438 baseline is redefined with a non-comparable direction and a reviewer-readable derivation, or
2. a stronger claim beats this null/trivial structural rule under the same directionality.

## Gate Impact

- Product Fund Gate logic is unchanged.
- Public corpus review status is downgraded.
- No external validation is claimed.
- No Nobel, Einstein-level, breakthrough, or theorem claim is made.
