# Reproduce V2 100-Claim Challenge

This reproducer checks the public 100-claim V2 survivor-yield arithmetic without
reading Product `.sovryn` state.

Run from this result directory:

```bash
node reproduce_v2_100_claim_challenge.js
```

Inputs:

- `V2_SURVIVOR_YIELD_BENCHMARK.json`
- `V2_DEEP_VALIDATION_RESULTS.md`
- `BASELINE_ONLY_DEEP_VALIDATION_RESULTS.md`
- `V2_BASELINE_ONLY_COMPARISON.md`

Expected outputs:

- V2 selected plausible claims: `17`
- V2 survivors: `17`
- V2 survivor yield: `1.000`
- baseline-only selected plausible claims: `25`
- baseline-only survivors: `17`
- baseline-only survivor yield: `0.680`
- baseline-only false advances filtered by V2: `8`
- benchmark size: `100`
- independent tasks/datasets: `42`
- public receipt rows: `100`

The script writes `v2_100_claim_reproducer_result.json` and prints the same
machine-readable result to stdout.

This is package-level public replay of the 100-claim survivor-yield evidence. It
is not external validation, not discovery-scored, and not `FUND_FOUND`.
