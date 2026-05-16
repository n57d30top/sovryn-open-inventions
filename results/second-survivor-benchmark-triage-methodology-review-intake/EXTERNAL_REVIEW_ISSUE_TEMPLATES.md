# External Review Issue Templates

These templates are for independent reviewers. They are intended for public GitHub Issue comments or equivalent public review records.

Using one of these templates does not guarantee score impact. A score-effective review still needs to satisfy `REVIEW_SCORE_CONTRACT.md`.

## Template A: Reproduction-Only Review

````markdown
## Reproduction-only review

Reviewer/source:

Public profile or affiliation context:

Review URL:

Candidate:
DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001

Commands run:

```bash
node reproduce_second_survivor_benchmark.js
node reviewer_replay_quickcheck.js
```

Environment:

- OS:
- Node version:
- Fresh clone or copied script only:

Result:

- Reproducer completed: yes/no
- Quickcheck completed: yes/no
- Validated rows:
- Replay status:
- Product metrics within rounding tolerance: yes/no
- Rounding caveat observed: yes/no

Decision:
accept / minor_revision / major_revision / reject

Notes:

Independence statement:
I am not involved in preparing the Sovryn package or the internal Codex review.
````

## Template B: Methodology Review

```markdown
## Methodology review

Reviewer/source:

Public profile or affiliation context:

Review URL:

Candidate:
DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001

Scope reviewed:

- Exact claim:
- Method:
- Public task/data receipts:
- Baselines:
- Holdout/split checks:
- Rival explanations:
- Negative controls:
- Limitations:

Methodology assessment:

- Is receipt-first benchmark triage useful beyond an internal checklist? yes/no/unclear
- Does it differ meaningfully from existing benchmark-audit or reproducibility practices? yes/no/unclear
- Are the baseline/holdout/rival/negative-control interpretations coherent? yes/no/unclear

Decision:
accept / minor_revision / major_revision / reject

Required revisions or caveats:

Independence statement:
I am not involved in preparing the Sovryn package or the internal Codex review.
```

## Template C: Rejection or Major-Revision Review

```markdown
## Rejection / major-revision review

Reviewer/source:

Public profile or affiliation context:

Review URL:

Candidate:
DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001

Decision:
major_revision / reject

Reason:

- Reproducer issue:
- Methodology issue:
- Baseline/rival issue:
- Holdout/split issue:
- Negative-control issue:
- Existing-practice redundancy:
- Claim too broad or unclear:

Minimal change that would make the package more reviewable:

Independence statement:
I am not involved in preparing the Sovryn package or the internal Codex review.
```

## Gate Reminder

Public issue creation, owner comments, and internal Codex review do not count as independent review. An external reviewer must be independent of the package preparation path.
