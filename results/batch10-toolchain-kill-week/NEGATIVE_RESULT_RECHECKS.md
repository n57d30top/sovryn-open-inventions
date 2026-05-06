# Negative Result Rechecks

## Batch 6 Diamonds

Original negative result:

The public diamonds CSV contained 146 duplicate rows, 8 rows with nonpositive `x`, 7 rows with nonpositive `y`, and 20 rows with nonpositive `z`.

Attack:

- Does the finding prove the dataset is unusable?
- Could the counts be ordinary data-quality audit signals rather than fatal flaws?
- Was the result already bounded?

Decision:

Preserved with scope. The result already states that these are useful data-quality findings, not a claim that the dataset is unusable.

## Batch 9 class-weight extension

Original negative result:

`class_weight_balanced_logistic_regression` decreased macro-F1 by -0.0038 on the primary split.

Decision:

Preserved. The extension rejection is an example of the toolchain preventing a fake improvement claim.

## Batch 8 pyproject-hooks

Original negative result:

`pytest_repro_summary` preserved runtime errors under a minimal environment.

Decision:

Preserved. The failure case supports keeping repo-test summarization as support-only.
