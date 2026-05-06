# Repo/test reproduction with runtime evidence for scientist CLI

Program id: sci-v0-program-2-prob-repo-test-runtime-evidence
Route: repo_test_reproduction

## Hypothesis

Repo/test reproduction with runtime evidence for scientist CLI can produce bounded, replayable evidence using the repo_test_reproduction route.

## Null Hypothesis

The route does not add enough evidence beyond simple checks and should remain partial or downgraded.

## Execution

Executed: true
Success: true
Replay: passed

Command summaries:
- Repository package metadata runtime probe. Exit code 0; duration 51 ms; raw command streams are omitted from public release.
- Scientist CLI registration probe. Exit code 0; duration 51 ms; raw command streams are omitted from public release.
- Fresh replay probe over scientist service source. Exit code 0; duration 50 ms; raw command streams are omitted from public release.

Findings:
- Repo/test reproduction route can produce bounded runtime evidence for the new scientist command family.
- This program is support evidence for orchestration readiness, not an external scientific discovery claim.

Negative or partial findings:
- The repo/test route remains partial until it is applied to a third-party public repository with full test collection.
