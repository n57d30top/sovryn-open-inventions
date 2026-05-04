# Limitations: Molecular Record Auditor for Chemistry-Style Dataset Quality

- "disclaimer": "This is an autonomous open-research artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion. It was published automatically after automated policy gates and still requires human interpretation before use.",
- README_CLAIMS_GROUNDED: passed (warn). README and public docs should ground claims in evidence, tests, and limitations.
- Input case: toy water boiling point appears as 100 C and 373.15 K
- Purpose: Suspicious acetone toy record should be flagged.
- Input case: toy acetone boiling point appears as 999 C
- Input case: toy molecule record has an unknown identifier

## Scope Limits

- It is not a general SMILES canonicalizer or cheminformatics toolkit.
- It does not suggest synthesis, handling, hazard optimization, or lab work.
- It uses bounded toy equivalence rules unless a stronger approved toolkit is added later.

## Human Review Still Required

The result can be useful as an open-source research artifact, but humans must
interpret the evidence, decide whether the method applies to a real dataset or
repository, and check any domain-specific risks before use.

Sovryn produces autonomous open-research artifacts, defensive publications, and open-source research evidence. It is not a patent filing system and does not provide legal patentability, legal novelty, or freedom-to-operate opinions.
