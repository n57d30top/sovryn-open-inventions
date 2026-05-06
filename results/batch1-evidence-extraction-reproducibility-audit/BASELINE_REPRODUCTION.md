# Baseline Reproduction

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| README-only checklist | README, paper title, broad dataset/code statement | 0.50 recall | misses environment and directory evidence |
| repo-structure checklist | README.md, datasets, environment.yml, src | 0.75 recall | still no lockfile or verified end-to-end run |

Baseline reproduction is bounded to public-safe data or source-card evidence. Missing full-scale reproduction is recorded as a limitation, not hidden.
