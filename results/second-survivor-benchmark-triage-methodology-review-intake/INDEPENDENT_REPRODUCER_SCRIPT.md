# Independent Reproducer Script

Canonical script: `reproduce_second_survivor_benchmark.js`

Reviewer quickcheck: `reviewer_replay_quickcheck.js`

## Script Contract

The canonical reproducer must:

- fetch only public OpenML ARFF data URLs,
- parse ARFF locally,
- reconstruct deterministic random and holdout splits,
- compute majority baseline, model metric, holdout metric, deltas, and shuffled
  target negative control,
- emit machine-readable JSON to stdout,
- write `standalone_replay_results.json`,
- write `STANDALONE_REPLAY_RESULTS.md`,
- avoid reading Product `.sovryn` state,
- avoid private paths,
- avoid secrets,
- keep `fundFound=false`,
- keep `countsForDiscoveryScore=false`.

## Execution

```bash
node reproduce_second_survivor_benchmark.js
```

Optional invariant check:

```bash
node reviewer_replay_quickcheck.js
```

## Public Data Bound by the Script

| Claim                       | OpenML task | Dataset   | Raw ARFF                                                  |
| --------------------------- | ----------: | --------- | --------------------------------------------------------- |
| `SA-PLAUS-003-OPENML-32`    |          32 | pendigits | `https://openml.org/data/v1/download/32/pendigits.arff`   |
| `SECOND-SURV-001-OPENML-59` |          59 | iris      | `https://openml.org/data/v1/download/61/iris.arff`        |
| `SECOND-SURV-003-OPENML-7`  |           7 | audiology | `https://openml.org/data/v1/download/7/audiology.arff`    |
| `SECOND-SURV-005-OPENML-53` |          53 | vehicle   | `https://openml.org/data/v1/download/54/vehicle.arff`     |
| `SECOND-SURV-006-OPENML-36` |          36 | segment   | `https://openml.org/data/v1/download/36/segment.arff`     |
| `SECOND-SURV-007-OPENML-43` |          43 | spambase  | `https://openml.org/data/v1/download/44/spambase.arff`    |
| `SECOND-SURV-008-OPENML-15` |          15 | breast-w  | `https://openml.org/data/v1/download/52350/breast-w.arff` |

## Expected Result

The expected high-level JSON fields are recorded in
`EXPECTED_REPRODUCER_OUTPUTS.json`. Small numeric differences are acceptable
only where they remain within the package's recorded rounding tolerance.
