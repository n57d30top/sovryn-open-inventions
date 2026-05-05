# Hypotheses

## sci-h-c5bec512d93a

Unit normalization plus provenance scoring will reduce false positives when auditing inconsistent chemistry-style molecular-property records compared with unit normalization alone.

- Null hypothesis: Unit normalization plus provenance scoring will not reduce false positives compared with unit normalization alone on the same synthetic chemistry-style records.
- Alternative hypothesis: Adding provenance scoring separates weak-source quality notes from true property conflicts while preserving recall for known inconsistent values.
- Falsification criteria: The unit-normalization-only baseline has equal or lower false-positive rate with comparable recall.; The candidate treats limited toy identifier equivalence as full cheminformatics canonicalization.; Weak provenance alone causes normal records to be falsely marked as chemical-property conflicts.

## sci-h-fab8d31841cd

Explicit low-confidence identifier-equivalence labels will improve audit interpretability compared with treating toy identifier variants as canonical matches.

- Null hypothesis: Low-confidence identifier-equivalence labels will not improve interpretability compared with treating toy identifier variants as canonical matches.
- Alternative hypothesis: The detector makes safer audit records by separating low-confidence equivalence from validated canonicalization.
- Falsification criteria: Reports claim general SMILES canonicalization.; Unknown identifiers are silently merged into a canonical group.; Low-confidence equivalence does not appear in outputs.

