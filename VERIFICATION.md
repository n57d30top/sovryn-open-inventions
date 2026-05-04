# Verification

This repository was assembled from a deterministic Sovryn OS Beta.9 pilot run.

## Source Run

- Pilot count: 3
- Publication dry-run count: 3
- Security audit: passed
- Reliability replay critical pass rate: 100
- Real GitHub publication: false

## Per-Result Public Release Audits

Each `results/<pilot-id>/release/` folder was checked as a curated public
release package:

- `results/evidence-chain/release`: passed
- `results/toolchain-policy/release`: passed
- `results/corpus-deduplication/release`: passed

## Public Hygiene

The repository was checked for common secret patterns, local absolute paths, and
raw command-log artifacts. Mentions of "raw command logs" inside reports refer
to gates that exclude them; raw stdout/stderr logs and command journals are not
included.

This repository contains Open Inventions, Defensive Publications, and Open
Source Research Artifacts. It is not a legal patent filing, not a patentability
opinion, and not a freedom-to-operate opinion.
