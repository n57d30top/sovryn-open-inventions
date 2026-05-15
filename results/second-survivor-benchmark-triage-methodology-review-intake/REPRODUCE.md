# Reproduce

## Standalone Public Replay

From this result directory:

```bash
node reproduce_second_survivor_benchmark.js
```

The script fetches public OpenML ARFF files and writes:

- `standalone_replay_results.json`
- `STANDALONE_REPLAY_RESULTS.md`

Current replay status: `public_raw_replay_reproduced_with_rounding_caveat`.

This standalone replay does not read Product `.sovryn` state. It is still not external validation.

## Product Replay

Run the upstream live replay first:

```bash
sovryn discover-daemon second-independent-survivor --live-openml --json
```

Then run this FundCandidateDraft readiness audit:

```bash
sovryn discover-daemon second-survivor-fund-draft --json
```
