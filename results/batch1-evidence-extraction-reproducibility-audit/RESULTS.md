# Results

| Metric | Value |
| --- | --- |
| README present | 1 |
| environment file present | 1 |
| repo top-level entries inspected | 4 |
| datasets directory present | 1 |
| src directory present | 1 |
| lockfile present | 0 |
| README-only checklist recall | 0.5 |
| repo-structure checklist recall | 0.75 |
| reproducibility score | 67 |

## Baseline Matrix

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| README-only checklist | README, paper title, broad dataset/code statement | 0.50 recall | misses environment and directory evidence |
| repo-structure checklist | README.md, datasets, environment.yml, src | 0.75 recall | still no lockfile or verified end-to-end run |
