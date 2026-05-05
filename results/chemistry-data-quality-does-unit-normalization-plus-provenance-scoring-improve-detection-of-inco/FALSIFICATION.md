# Falsification: Does unit-normalization plus provenance scoring improve detection of inconsistent chemistry-style molecular property records compared with unit normalization alone?

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

### consistent-unit-conversion

- Purpose: Consistent Celsius/Kelvin records should not be flagged as conflicts.
- Input case: toy water boiling point appears as 100 C and 373.15 K
- Expected behavior: no conflict after unit normalization
- Falsification target: false-positive risk
- Safe synthetic only: true

### suspicious-acetone-record

- Purpose: Suspicious acetone toy record should be flagged.
- Input case: toy acetone boiling point appears as 999 C
- Expected behavior: outlier flag
- Falsification target: false-negative risk
- Safe synthetic only: true

### unknown-identifier

- Purpose: Unknown identifier should be low confidence rather than silently canonicalized.
- Input case: toy molecule record has an unknown identifier
- Expected behavior: low confidence equivalence
- Falsification target: identifier-confidence risk
- Safe synthetic only: true

### malformed-unit

- Purpose: Malformed unit should be rejected or flagged.
- Input case: toy record uses unsupported temperature unit text
- Expected behavior: invalid unit flag
- Falsification target: input validation risk
- Safe synthetic only: true


## Overclaim Findings

No blocking overclaim findings.

## Recommended Action

Keep as reviewable public corpus evidence; continue human interpretation before use.

This is an independent falsification and review artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion.
