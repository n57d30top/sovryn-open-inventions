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
