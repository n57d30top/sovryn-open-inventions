# Independent Reproducer README

This is the public-safe reproduction path for
`DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001`.

It is a bounded benchmark-triage methodology replay. It is not external
validation, not a discovery-scored Fund, and not a `FUND_FOUND` claim.

## Requirements

- Node.js 18 or newer.
- Public network access to `openml.org`.
- No Product repository checkout is required.
- No `.sovryn` state is required.
- No secret, token, credential, or private path is required.

There are no third-party npm runtime dependencies. The reproducer uses built-in
Node APIs: `fetch`, `crypto`, `fs`, and `path`.

## Files

- `reproduce_second_survivor_benchmark.js`: fetches public OpenML ARFF files,
  recomputes replay metrics, writes JSON and Markdown outputs, and prints a
  machine-readable JSON report.
- `reviewer_replay_quickcheck.js`: reruns the public reproducer and checks
  package invariants.
- `EXPECTED_REPRODUCER_OUTPUTS.json`: expected status, rows, public task IDs,
  and no-overclaim invariants.

## Commands

From this result directory:

```bash
node reproduce_second_survivor_benchmark.js
node reviewer_replay_quickcheck.js
```

Expected high-level result:

- `standalone_replay_results.json` is written.
- `STANDALONE_REPLAY_RESULTS.md` is written.
- `reviewer_replay_quickcheck_result.json` is written.
- seven public OpenML replay rows are validated.
- `productMetricsWithinRoundingTolerance` is true.
- `fundFound` remains false.
- `countsForDiscoveryScore` remains false.

## What This Reproduces

The script recomputes the public raw-data replay table used to inspect the
bounded benchmark-triage candidate:

- majority baseline metric,
- random split metric,
- group/feature holdout metric,
- model-vs-baseline delta,
- random-vs-holdout delta,
- shuffled-target negative control,
- raw OpenML ARFF SHA-256 hash.

## What This Does Not Prove

This replay does not prove external validation, external adoption, discovery
scoring, Nobel relevance, Einstein-level capability, or breakthrough status.
Those statuses require separate score-gated evidence and external public review
or reproduction records.
