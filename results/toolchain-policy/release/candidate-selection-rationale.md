# Candidate Selection Rationale

Selected candidates are scored from source evidence strength, source diversity, novelty risk, safety risk, prototype feasibility, testability, defensive-publication value, and reproducibility.

## Selected Candidates

### evidence-gated-research-factory: Evidence-gated research factory for Develop a policy-gated toolchain installation protocol for autonomous Linux research nodes that prevents unsafe host installs and records reproducible tool evidence.

Selection score: 83
Evidence strength score: 78
Feasibility score: 88
Publication readiness score: 82
Novelty risk: medium
Safety risk: low
Unresolved prior-art risk: high

Why selected: evidence-derived scoring favored this candidate's balance of source support, prototype feasibility, testability, low safety risk, reproducibility, and defensive-publication value.

Supporting evidence:
- source-4
- source-5
- source-6
- source-7
- source-8

Top counter-evidence:
- source-4/source-feature-1: high
- source-5/source-feature-2: high
- source-6/source-feature-3: high

What would invalidate it:
- A concrete source shows the same source-card binding, replay, prototype execution, and curated publication gate combination.
- Prototype tests fail to distinguish weak evidence from ready evidence.

Weak evidence and strengthening experiment:
- Evidence is sufficient for Alpha review but still requires human source comparison.
- Run additional source reads and verify counter-evidence does not fully cover the candidate.

## Rejected Candidates

### public-evidence-curator: Curated public evidence curator

Selection score: 76
Reason: Rejected because evidence strength is weaker than the selected candidate.

### source-matrix-novelty-gap-scorer: Source matrix novelty-gap scorer

Selection score: 75
Reason: Rejected because the selected candidate has stronger combined reproducibility, evidence, and defensive-publication value.

## Candidate Score Inputs

- evidence-gated-research-factory: score=83, sourceEvidence=82, diversity=75, reproducibility=85
- source-matrix-novelty-gap-scorer: score=75, sourceEvidence=70, diversity=75, reproducibility=75
- public-evidence-curator: score=76, sourceEvidence=50, diversity=75, reproducibility=88

This rationale is for open-source research selection only. It is not a patent filing or legal claim chart.
