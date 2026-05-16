# Reproducer Dry Run Record

Date: 2026-05-16

Purpose: verify that the public reproducer can run from a fresh temporary location without local Product `.sovryn` state.

## Fresh Location

The reproducer script was copied into a fresh temporary directory outside the repository. The public record intentionally omits the local temporary path.

## Dependency Install Status

No third-party runtime dependency installation was required.

Required runtime:

- Node.js 18 or newer with built-in `fetch`

## Command

```bash
cp results/second-survivor-benchmark-triage-methodology-review-intake/reproduce_second_survivor_benchmark.js <fresh-temp-dir>/
cd <fresh-temp-dir>
node reproduce_second_survivor_benchmark.js > dry-run-stdout.json
```

## Result

Pass/fail: pass

Replay status:

`public_raw_replay_reproduced_with_rounding_caveat`

Validated replay rows:

`7`

Product metric status:

- exact Product metrics matched: no
- within rounding tolerance: yes

Gate fields:

- `fundFound=false`
- `countsForDiscoveryScore=false`
- `standalonePublicReplayReadsProductState=false`
- `standalonePublicReplayExternalValidation=false`

## Rounding Caveat

The reproducer confirms all Product-displayed metrics within rounding tolerance. It does not remove the caveat that OpenML-32 differs from the Product rounded table by 0.001 on two displayed metrics.

## Interpretation

This is a public-safe dry run by the project maintainer environment. It is not independent external reproduction and does not create score-effective external validation.
