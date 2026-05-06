# Batch 7 Banknote Metric Stress Validator

## What concrete task was blocked?

UCI Banknote Authentication classification dataset

Existing generic tools were tried first, but they did not produce the exact public-safe evidence needed for this Batch 7 target.

## What Sovryn built

Sovryn built `metric_stress_validator` as the smallest useful custom instrument for this target.

## Did it work?

Logistic regression reached accuracy=0.976, balanced_accuracy=0.978, f1_macro=0.976; the shuffled-label control stayed near balanced_accuracy=0.476.

Tool status: `used_successfully_limited`.

Tool decision: `downgraded_to_narrow_but_useful`.

## What Sovryn learned

The metric validator is useful for comparing a challenger against dummy and shuffled-label controls, but it is explicitly limited because one deterministic split cannot certify an official benchmark protocol or prove absence of leakage.

## Safety and publication scope

Safe computational research only. No private data, no harmful domain content, no benchmark-win or breakthrough claim, and no legal patentability/FTO claim.
