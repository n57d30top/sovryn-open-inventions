# Radical Principle Cards

## RGC-01: Accessible Falsifier Boundary
- Claim: A claim can be stronger when a decisive public falsifier is directly executable, even if some descriptive fields are thin; complete fields without falsifier access remain weak.
- Challenges: field count is enough
- Variables: falsifier_accessibility, execution_resolution_cost, negative_control_decisiveness, field_completeness, replay_status
- Falsifiers: rival predicts observation with fewer caveats; negative control reverses result; replay failure blocks claim
- Novelty-vs-prior score: 82

## RGC-02: Resolution-Cost Gradient
- Claim: Missing evidence should cause harsher downgrades when resolving it requires high-cost, unavailable, or unstable execution.
- Challenges: documentation beats execution
- Variables: resolution_cost, download_success, install_success, runtime_success, replay_cost
- Falsifiers: rival predicts observation with fewer caveats; negative control reverses result; replay failure blocks claim
- Novelty-vs-prior score: 81

## RGC-03: Executable Specificity Dominance
- Claim: A narrow executable claim can be safer than a broad well-documented claim if the executable behavior is specific and falsifiable.
- Challenges: positive evidence dominates controls
- Variables: behavior_specificity, smoke_success, negative_case_success, claim_width
- Falsifiers: rival predicts observation with fewer caveats; negative control reverses result; replay failure blocks claim
- Novelty-vs-prior score: 80

## RGC-04: Negative-Control Asymmetry
- Claim: A failed or decisive negative control should outweigh otherwise favorable fields, replay, or baseline results.
- Challenges: all missingness has equal cost
- Variables: control_gap, control_failure, baseline_gap, metric_sensitivity
- Falsifiers: rival predicts observation with fewer caveats; negative control reverses result; replay failure blocks claim
- Novelty-vs-prior score: 79

## RGC-05: Artifact Friction Limit
- Claim: Artifact Friction Limit proposes a narrower measurable boundary, but was not selected for execution.
- Challenges: field count is enough
- Variables: claim_width, field_gap, execution_depth
- Falsifiers: rival predicts observation with fewer caveats; negative control reverses result; replay failure blocks claim
- Novelty-vs-prior score: 51

## RGC-06: Reviewer Burden Inversion
- Claim: Reviewer Burden Inversion proposes a narrower measurable boundary, but was not selected for execution.
- Challenges: documentation beats execution
- Variables: claim_width, field_gap, execution_depth
- Falsifiers: rival predicts observation with fewer caveats; negative control reverses result; replay failure blocks claim
- Novelty-vs-prior score: 50

## RGC-07: Field Count Saturation
- Claim: Field Count Saturation proposes a narrower measurable boundary, but was not selected for execution.
- Challenges: positive evidence dominates controls
- Variables: claim_width, field_gap, execution_depth
- Falsifiers: rival predicts observation with fewer caveats; negative control reverses result; replay failure blocks claim
- Novelty-vs-prior score: 49

## RGC-08: Decisive Counterexample Priority
- Claim: Decisive Counterexample Priority proposes a narrower measurable boundary, but was not selected for execution.
- Challenges: all missingness has equal cost
- Variables: claim_width, field_gap, execution_depth
- Falsifiers: rival predicts observation with fewer caveats; negative control reverses result; replay failure blocks claim
- Novelty-vs-prior score: 48

## RGC-09: Claim Width Penalty
- Claim: Claim Width Penalty proposes a narrower measurable boundary, but was not selected for execution.
- Challenges: field count is enough
- Variables: claim_width, field_gap, execution_depth
- Falsifiers: rival predicts observation with fewer caveats; negative control reverses result; replay failure blocks claim
- Novelty-vs-prior score: 47

## RGC-10: Control Gap Dominance
- Claim: Control Gap Dominance proposes a narrower measurable boundary, but was not selected for execution.
- Challenges: documentation beats execution
- Variables: claim_width, field_gap, execution_depth
- Falsifiers: rival predicts observation with fewer caveats; negative control reverses result; replay failure blocks claim
- Novelty-vs-prior score: 46
