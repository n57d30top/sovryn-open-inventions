# Graph-Minor Baseline Directionality Audit

## Baseline Summary

| Baseline | Value | What It Measures | Directionality | Explains Signal? | Decision |
|---|---:|---|---|---|---|
| `size_density_degree_treewidth_proxy_baseline` | 0.319 | Mean row baseline from density and average degree | Higher means stronger structural baseline score | Does not dominate `measuredOutcome = 0.424` by value | Non-fatal but incomplete |
| `matched_known_family_negative_control` | 0.356 | Mean obstruction score among rows where `candidateMechanismHolds = false` | Higher means stronger negative-control obstruction score | Does not dominate `measuredOutcome = 0.424` by value | Non-fatal but family-confounded |
| `null_or_trivial_structural_rule` | 0.438 | Mean `min(density, averageDegree / vertices)` | Higher means stronger null/trivial structural score | Numerically exceeds `measuredOutcome = 0.424` | Fatal for public discovery scoring until resolved |

## 0.438 Issue

The Product gate marked `null_or_trivial_structural_rule = 0.438` as `explainsSignal: false` because the internal rule used a threshold of `>= 0.5`. That is not sufficient for external review. If the value is directionally comparable to the measured outcome, then `0.438` exceeds `0.424` and should be treated as a dominating null/trivial structural explanation.

## Family-Level Evidence

The largest positive residuals are concentrated in canonical families:

| Family | Count | Mean Outcome | Mean Baseline | Signed Residual | Hold Rate | Rival Explains Rate |
|---|---:|---:|---:|---:|---:|---:|
| `wheel` | 12 | 0.693 | 0.283 | 0.410 | 1.000 | 0.000 |
| `complete_bipartite` | 12 | 0.532 | 0.392 | 0.141 | 0.500 | 0.000 |
| `grid` | 12 | 0.314 | 0.174 | 0.140 | 1.000 | 0.000 |
| `complete` | 12 | 0.603 | 0.700 | -0.098 | 0.000 | 1.000 |
| `cycle` | 12 | 0.164 | 0.186 | -0.022 | 0.000 | 0.500 |
| `ladder` | 12 | 0.238 | 0.180 | 0.058 | 0.000 | 0.000 |

This makes the signal look family-driven rather than a precise obstruction/minor result.

## Holdout Caveat

The development and holdout summaries are numerically identical after rounding:

- development measured outcome: 0.423917
- holdout measured outcome: 0.423917
- development positive residual: 0.127667
- holdout positive residual: 0.127667

That is replay consistency, but not strong independence. It is consistent with a repeated generated-family pattern.
