# Next Action

Do not create `FUND_FOUND`.

Do not claim discovery-scored status.

Manual next action:

1. Send `REVIEW_REQUEST_DRAFT.md` and the public package URL to one or more
   suitable external reviewers or independent reproducers.
2. Ask them to run `node reproduce_second_survivor_benchmark.js` and
   `node reviewer_replay_quickcheck.js`.
3. Require any score-impacting review to be published at an external public URL.
4. Generate a source receipt for that URL with:

   ```bash
   sovryn nobel-readiness external-review-source-receipt --url <reviewSourceRef> --json
   ```

5. Run:

   ```bash
   sovryn nobel-readiness external-review-intake --json
   ```

Only after that should Product gates decide whether any readiness score changes.
