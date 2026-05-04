# Molecular Record Auditor for Chemistry-Style Dataset Quality

Sovryn produces autonomous open-research artifacts, defensive publications, and open-source research evidence. It is not a patent filing system and does not provide legal patentability, legal novelty, or freedom-to-operate opinions.

## Problem Statement

Chemistry-style public datasets can contain duplicate molecular identifiers, mixed temperature units, suspicious property values, and weak provenance. This result frames the problem as safe data-quality auditing, not chemical design or wet-lab guidance.

## Method

The method normalizes identifiers and units, groups known toy-equivalent molecules, checks duplicate property values, flags outliers, and reports provenance confidence using a lightweight custom auditor.

## Custom Tool

mol-record-auditor

The curated result uses the recorded tool evidence and package evidence to keep
the method reproducible. External package/tool evidence: pint.

## What This Catches

- Duplicate ethanol, water, acetone, or benzene toy records after bounded identifier equivalence.
- Celsius and Kelvin boiling-point records that should agree after unit normalization.
- A suspicious acetone toy record with an implausible boiling-point value.
- Weak provenance or malformed fields that lower dataset reliability.

## What This Does Not Catch

- It is not a general SMILES canonicalizer or cheminformatics toolkit.
- It does not suggest synthesis, handling, hazard optimization, or lab work.
- It uses bounded toy equivalence rules unless a stronger approved toolkit is added later.

## Tests

The result keeps prototype and test evidence in the curated release package.
The tests are meant to demonstrate the method on bounded public-safe examples,
not to prove production readiness.

## Source Evidence Summary

The public corpus entry is backed by source-card, claim/feature, counter-evidence,
worker, replay, quality, safety, and public-hygiene summaries. Query links,
adapter failures, and placeholders are not treated as reviewed prior art.

## Counter-Evidence And Limitations

- "disclaimer": "This is an autonomous open-research artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion. It was published automatically after automated policy gates and still requires human interpretation before use.",
- README_CLAIMS_GROUNDED: passed (warn). README and public docs should ground claims in evidence, tests, and limitations.
- Input case: toy water boiling point appears as 100 C and 373.15 K
- Purpose: Suspicious acetone toy record should be flagged.
- Input case: toy acetone boiling point appears as 999 C
- Input case: toy molecule record has an unknown identifier

## How To Reproduce

See [REPRODUCE.md](REPRODUCE.md). The reproduction path uses only public
curated artifacts and does not require private Sovryn state.

## Autopublish Record

See [AUTOPUBLISH_RECORD.json](AUTOPUBLISH_RECORD.json). This result was
published automatically after automated gates. Human interpretation is still
required before operational use.

## Safety Scope

This is a bounded open-source research artifact. It is not a legal filing, not
a legal novelty opinion, and not operational advice for unsafe activity.
