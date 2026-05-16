# Benchmark Triage Method V2

This revision turns the receipt-first benchmark package from a checklist into a
bounded triage method. It does not strengthen the scientific claim and does not
make the candidate discovery-scored.

## Method Purpose

The method ranks public benchmark claims for external review by combining replay
readiness, baseline survival, holdout separation, negative-control behavior, and
rival-closure evidence.

The method is not a benchmark theorem. It is a review triage rule for deciding
which claims deserve deeper external benchmark-methodology review.

## Inputs

Each benchmark claim must provide:

- concrete task or dataset ID,
- public raw-data receipt,
- deterministic loading path,
- target variable,
- model metric,
- majority or simple baseline metric,
- stronger holdout or split metric,
- negative-control metric,
- rival explanation status,
- replay status.

Claims missing receipts or replay are rejected before scoring.

## Formal Decision Rule

For each claim, compute:

```text
receiptReplay = 1 if raw receipt exists and public replay is within tolerance, else 0
baselineSurvival = clamp(modelVsBaselineDelta / 0.15, 0, 1)
holdoutSurvival = clamp(randomVsHoldoutDelta / 0.20, 0, 1)
negativeControlSurvival = 1 if randomMetric - negativeControlMetric >= 0.02 and control behaved, else 0.5 if >= 0.005, else 0
rivalClosure = 1 if rivalStatus is scoped_or_weakened, else 0
splitQuality = 0.6 for current first-feature bucket holdouts, 1.0 for real group/time/entity holdouts

v2Score =
  0.25 * receiptReplay +
  0.20 * baselineSurvival +
  0.20 * holdoutSurvival +
  0.15 * negativeControlSurvival +
  0.10 * rivalClosure +
  0.10 * splitQuality
```

Hard blockers:

- missing receipt or replay,
- `modelVsBaselineDelta < 0.08`,
- `randomVsHoldoutDelta < 0.08`,
- `randomMetric - negativeControlMetric < 0.02`,
- rival not scoped or weakened.

## Output Classes

| Class                           | Rule                                   | Meaning                                   |
| ------------------------------- | -------------------------------------- | ----------------------------------------- |
| `retain_for_external_re_review` | score >= 0.70 and no hard blockers     | Reviewable after V2 repair                |
| `major_revision_caveat_retain`  | score >= 0.55 but at least one blocker | Keep visible, do not claim method support |
| `reject_or_abstain`             | score < 0.55 or missing required input | Do not use for method-value claim         |

## Falsifiers

The method should be downgraded if:

- reject-all ties or beats it on survivor yield,
- baseline-only ties or beats it on survivor yield across a larger holdout,
- retained claims fail public replay,
- retained claims are explained by negative controls,
- holdout deltas vanish under real group/time/entity splits,
- rival explanations remain stronger after measurable checks.

## Current V2 Application

On the current seven replay rows, V2 retains six rows for re-review and demotes
one row (`SECOND-SURV-007-OPENML-43`, spambase) to
`major_revision_caveat_retain` because the model-vs-baseline margin is small and
the negative-control metric is essentially equal to the random-split metric.

This is an improvement over accepting all replayable rows, but not enough to
settle the major-revision critique. Baseline-only selection ties V2 on this
small package, so a larger re-review benchmark is still required.

## Limitations

- The current package has only seven replay rows.
- Current holdouts are first-feature bucket holdouts, not real group/time/entity
  manifests.
- V2 is not externally validated.
- V2 is not discovery-scored.
- `FUND_FOUND` remains false.
