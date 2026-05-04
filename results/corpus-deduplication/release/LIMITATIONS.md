# Factory Limitations

Research goal: Develop a corpus deduplication method for defensive publications that detects overlapping Open Inventions using source cards, claim features, and release metadata.

Public search enabled: true
Source reading enabled: true
Concrete sources found: 12
Concrete sources read: 12
Query-link-only leads: 6
Adapter failures: 3
Mock placeholders used: 0

## Weak Evidence

- Query links are research leads, not reviewed prior art.
- One or more public-source adapters failed and require retry or manual review.
- Readings are bounded by configured depth and are not legal novelty conclusions.

## Required Human Review

- Review concrete source overlap and differences.
- Review generated candidate novelty gaps.
- Review safety notes before public release.
- Legal, patentability, novelty, and freedom-to-operate review are outside Sovryn scope.

## Safety Scope

High safety risk blocks packaging: true
The conservative safety scanner is not a sandbox and does not replace OS-level isolation.
