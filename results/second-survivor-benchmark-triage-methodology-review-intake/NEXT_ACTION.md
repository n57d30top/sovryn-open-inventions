# Next Action

Do not create `FUND_FOUND`.

Do not claim discovery-scored status.

Manual next action:

1. Public GitHub review request is open:

   https://github.com/n57d30top/sovryn-open-inventions/issues/1

2. Send the issue URL, `FIRST_EXTERNAL_REVIEW_REQUEST.md`,
   `CANDIDATE_ONE_PAGE_SUMMARY.md`, and the public package URL to one or more
   suitable external reviewers or independent reproducers.
3. Ask them to run `node reproduce_second_survivor_benchmark.js` and
   `node reviewer_replay_quickcheck.js`.
4. Require any score-impacting review to be published at an external public URL.
5. Generate a source receipt for that URL with:

   ```bash
   sovryn nobel-readiness external-review-source-receipt --url <reviewSourceRef> --json
   ```

6. Run:

   ```bash
   sovryn nobel-readiness external-review-intake --json
   ```

Only after that should Product gates decide whether any readiness score changes.

Current public Issue #1 and the internal Codex review do not satisfy this
requirement because both are owner/workspace-associated records, not independent
external review or reproduction.

Reviewer-friction reducers now available:

- `REVIEW_IN_10_MINUTES.md`
- `EXTERNAL_REVIEW_ISSUE_TEMPLATES.md`
- `EXPECTED_REVIEWER_OUTPUTS.json`
- `GITHUB_EXTERNAL_REVIEW_COMMENT_TEMPLATE.md`
- `VENUE_SPECIFIC_REVIEW_MESSAGES.md`
