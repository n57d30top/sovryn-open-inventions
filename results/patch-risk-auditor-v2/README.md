# Patch Risk Auditor

Sovryn produces autonomous open-research artifacts, defensive publications, and open-source research evidence. It is not a patent filing system and does not provide legal patentability, legal novelty, or freedom-to-operate opinions.

## Problem Statement

AI-generated pull requests can change dependencies, scripts, tests, and provenance in ways that deserve defensive review. This result scores synthetic patch risk without exploiting real systems or publishing attack payloads.

## Method

The method parses synthetic patch metadata, checks dependency and install-script changes, compares expected test impact to changed files, and reports defensive patch-risk signals.

## Custom Tool

patch-risk-auditor

The curated result uses the recorded tool evidence and package evidence to keep
the method reproducible. External package/tool evidence: acorn.

## What This Catches

- Synthetic dependency additions that deserve review.
- Install-script or package metadata changes in toy repository examples.
- Test-impact mismatches where changed code is not covered by expected tests.
- Weak patch provenance that lowers confidence.

## What This Does Not Catch

- It does not exploit real repositories or publish attack payloads.
- It does not prove that a pull request is malicious.
- It is a defensive risk-prioritization method for synthetic examples.

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
- Install-script or package metadata changes in toy repository examples.
- These examples are bounded demonstrations for public research artifacts. They
- Limitations: Patch Risk Auditor
- This is an autonomous open-research artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion. It was published automatically after automated policy gates and still requires human interpretation before use.
- Legal disclaimer: This is an autonomous open-research artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion. It was published automatically after automated policy gates and still requires human interpretation before use.

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
