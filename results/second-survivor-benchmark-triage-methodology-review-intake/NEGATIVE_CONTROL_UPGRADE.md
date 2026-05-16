# Negative Control Upgrade

The major-revision review found the negative controls too weak. V2 strengthens
the interpretation by adding a margin test and by naming required future
controls.

## Current Executed Control

The current public reproducer executes a shuffled-target control. In V1, a
control was considered behaved if:

```text
negativeControlMetric <= baselineMetric + 0.08
```

V2 adds a stricter margin:

```text
negativeControlMargin = randomSplitMetric - negativeControlMetric
```

The control is strong only when:

```text
negativeControlMargin >= 0.02
```

This prevents a row from passing strongly when the negative-control model is
nearly as good as the random-split model.

## Required Future Controls

For a stronger re-review benchmark, the package must add:

- shuffled target,
- random feature,
- label permutation,
- source-identity leakage probe,
- duplicate/entity overlap probe,
- metric sensitivity,
- baseline plus margin threshold sensitivity.

## V2 Effect

The stricter negative-control margin demotes
`SECOND-SURV-007-OPENML-43` (`spambase`) because:

```text
randomSplitMetric = 0.653
negativeControlMetric = 0.652
negativeControlMargin = 0.001
```

That row remains visible, but it can no longer support the method-value claim.
