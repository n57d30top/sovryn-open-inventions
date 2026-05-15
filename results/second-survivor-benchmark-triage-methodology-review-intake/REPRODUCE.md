# Reproduce

## Standalone Public Replay

From this result directory:

```bash
node reproduce_second_survivor_benchmark.js
node reviewer_replay_quickcheck.js
```

The standalone replay fetches public OpenML ARFF files and writes `standalone_replay_results.json` plus `STANDALONE_REPLAY_RESULTS.md`. The reviewer quickcheck reruns that replay and writes `reviewer_replay_quickcheck_result.json` plus `REVIEWER_REPLAY_QUICKCHECK_RESULT.md`.

This is public-data replay inspectability evidence only. It is not external validation.

## Product Replay

Run the upstream live replay first:

```bash
sovryn discover-daemon second-independent-survivor --live-openml --json
```

Then run this FundCandidateDraft readiness audit:

```bash
sovryn discover-daemon second-survivor-fund-draft --json
```
