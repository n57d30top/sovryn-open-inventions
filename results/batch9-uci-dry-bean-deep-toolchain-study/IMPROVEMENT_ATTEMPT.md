# Improvement Attempt

Attempted extension: `class_weight_balanced_logistic_regression`.

Baseline: plain LogisticRegression with standard scaling.

Result:

- Plain LogisticRegression macro-F1: 0.9347
- Class-weight balanced LogisticRegression macro-F1: 0.9309
- Macro-F1 delta: -0.0038
- Decision: reject_no_macro_f1_gain

Minority-class deltas:

{
  "BARBUNYA": 0.0029536096806471734,
  "BOMBAY": 0.0
}

The extension is rejected as a general improvement claim because macro-F1 decreased on the primary split. The useful part is not an improved score; it is the class-risk reporting that prevents a fake improvement claim.
