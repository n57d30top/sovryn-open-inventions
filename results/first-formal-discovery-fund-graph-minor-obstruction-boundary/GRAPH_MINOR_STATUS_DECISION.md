# Graph-Minor Status Decision

## Decision

`package_repair_required_before_external_review`

## Conditions Checked

| Condition | Status |
|---|---|
| Precise mathematical claim | repaired into bounded manifest claim only |
| Residual formula public | repaired |
| `0.438` baseline not fatal | failed |
| Independent source replay | failed |
| Known/triviality not fatal | failed for discovery scoring; human review still needed |

## Public Status

The public package is downgraded from `formal_replay_succeeded_caveated_no_external_validation` to `package_repair_required_before_external_review`.

## What Remains Valid

- The exported manifest can be replayed.
- The row-level measured outcome and residual formula are now public.
- No external validation is claimed.
- Product Fund Gate logic was not changed.

## What No Longer Counts Publicly

- The package should not count as public discovery-scored evidence.
- The package should not be presented as externally review-ready until independent source replay and baseline directionality are repaired.

## Required Repair Before Review

1. Add concrete HOG/GraphClasses object IDs or graph encodings.
2. Recompute metrics from source objects.
3. Resolve the `0.438` null/trivial structural-rule baseline.
4. State a precise graph-theory claim, obstruction, boundary, checked proof, or checked refutation.
