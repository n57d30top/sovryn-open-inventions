# Falsification: Patch Risk Auditor

Evaluation label: passes_falsification
Score: 96

## Purpose

This report tries to weaken or falsify the public result before it remains a
showcase or reviewable corpus artifact.

## Checks

- PUBLIC_HYGIENE_PASSED: passed (block). Public hygiene must pass before falsification can accept a result.
- NO_OVERCLAIMS: passed (block). No overclaiming language found.
- NEGATIVE_TESTS_PRESENT: passed (warn). Domain-specific negative tests should exist.
- BENIGN_CASES_NOT_OVERFLAGGED: passed (warn). Falsification should include benign cases that should not be overflagged.
- ADVERSARIAL_SAFE_CASES_FLAGGED: passed (warn). Falsification should include safe synthetic cases that should be flagged.
- README_CLAIMS_GROUNDED: passed (warn). README and public docs should ground claims in evidence, tests, and limitations.
- QUALITY_NOT_WEAK: passed (block). Weak quality labels cannot pass falsification.

## Negative Tests

### benign-dependency-update

- Purpose: Benign dependency update should not be scored as high risk without other suspicious signals.
- Input case: synthetic package patch with a version bump and matching tests
- Expected behavior: low or medium risk, not high risk
- Falsification target: false-positive risk
- Safe synthetic only: true

### suspicious-install-script

- Purpose: Suspicious install-script addition should be flagged for review.
- Input case: synthetic package patch adds a postinstall script and weak provenance
- Expected behavior: high review priority
- Falsification target: false-negative risk
- Safe synthetic only: true

### harmless-refactor

- Purpose: Harmless refactor should not be labeled dangerous.
- Input case: synthetic code-only refactor with no dependency or script changes
- Expected behavior: low risk
- Falsification target: false-positive risk
- Safe synthetic only: true

### test-impact-mismatch

- Purpose: Patch touching behavior without matching tests should be flagged.
- Input case: synthetic behavior change with unchanged tests
- Expected behavior: test-impact mismatch
- Falsification target: coverage risk
- Safe synthetic only: true


## Overclaim Findings

No blocking overclaim findings.

## Recommended Action

Keep as reviewable public corpus evidence; continue human interpretation before use.

This is an independent falsification and review artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion.
