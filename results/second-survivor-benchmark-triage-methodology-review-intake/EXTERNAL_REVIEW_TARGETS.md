# External Review Targets

No one has been contacted by this package. This list identifies suitable target
communities and reviewer profiles for manual outreach.

## Target Reviewer Profiles

1. ML benchmark methodology researchers
   - Focus: benchmark protocol design, leaderboard validity, dataset split
     fragility, evaluation methodology.
   - What to ask: whether the bounded triage method adds value beyond existing
     benchmark hygiene checks.

2. OpenML and AutoML community reviewers
   - Focus: OpenML task metadata, reproducible benchmark tasks, AutoML benchmark
     selection, public task replay.
   - What to ask: whether the selected OpenML replay protocol is meaningful and
     whether the method catches real weak benchmark claims.

3. Reproducibility researchers
   - Focus: public data replay, independent reproduction packaging, source
     receipts, rerunnable scripts.
   - What to ask: whether the package is independently reproducible and what
     should be improved before it is cited as evidence.

4. AI evaluation researchers
   - Focus: benchmark overfitting, protocol sensitivity, metric artifacts,
     negative controls.
   - What to ask: whether the method provides a useful bounded triage screen for
     evaluation fragility claims.

5. Model governance and MLOps practitioners
   - Focus: practical benchmark risk triage, holdout policy, decision workflow,
     review operations.
   - What to ask: whether the method is operationally useful as a pre-review
     filter and what failure modes remain.

## Suitable Venues Or Channels

- Public GitHub issue or discussion thread in a repository controlled by the
  reviewer or reviewing project.
- Public review note with permanent URL.
- Public reproducibility report or notebook.
- Public OpenML/AutoML/benchmark-methodology discussion thread.

## Unsuitable Inputs

- Private chat feedback.
- Anonymous unsupported acceptance.
- Synthetic reviewer output.
- Product-owned self-review.
- Review without source URL or receipt.
- Review that claims external validation without independent reproduction.
