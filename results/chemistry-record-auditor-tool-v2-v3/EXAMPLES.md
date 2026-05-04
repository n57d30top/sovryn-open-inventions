# Examples: Molecular Record Auditor for Chemistry-Style Dataset Quality

## What This Catches

- Duplicate ethanol, water, acetone, or benzene toy records after bounded identifier equivalence.
- Celsius and Kelvin boiling-point records that should agree after unit normalization.
- A suspicious acetone toy record with an implausible boiling-point value.
- Weak provenance or malformed fields that lower dataset reliability.

## What This Should Not Overclaim

- It is not a general SMILES canonicalizer or cheminformatics toolkit.
- It does not suggest synthesis, handling, hazard optimization, or lab work.
- It uses bounded toy equivalence rules unless a stronger approved toolkit is added later.

## Why This Is Useful

The result is useful because it keeps chemistry-style analysis safely focused on data quality, unit normalization, provenance, and reproducibility.

These examples are bounded demonstrations for public research artifacts. They
are not claims of production coverage, legal novelty, or freedom-to-operate.
