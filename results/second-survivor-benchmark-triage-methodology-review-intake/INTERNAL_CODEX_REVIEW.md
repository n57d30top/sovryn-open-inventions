# Internal Codex Review

Candidate: `DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001`

Review date: 2026-05-16

Reviewer/source: Codex assistant operating in the project workspace.

Independence: no. This reviewer participated in preparing the public review
request and repository bookkeeping, so this record is not an independent
external review and cannot satisfy the Review Score Contract.

Score effect: none.

Decision: `minor_revision` as an internal methodology review only.

## Reproduction Result

Commands run:

```bash
node reproduce_second_survivor_benchmark.js
node reviewer_replay_quickcheck.js
```

Fresh-directory check:

```bash
tmpdir=$(mktemp -d)
cp reproduce_second_survivor_benchmark.js "$tmpdir"/
(cd "$tmpdir" && node reproduce_second_survivor_benchmark.js)
```

Observed result:

- public reproducer completed,
- reviewer quickcheck completed,
- seven replay rows were validated,
- `productMetricsWithinRoundingTolerance=true`,
- `fundFound=false`,
- `countsForDiscoveryScore=false`,
- `standalonePublicReplayReadsProductState=false`,
- `standalonePublicReplayExternalValidation=false`.

The OpenML-32 row retains the known rounding caveat: displayed baseline,
random-split, and holdout metrics differ from the recorded rounded Product table
by `0.001`, while derived deltas remain within tolerance.

## Methodology Assessment

The package is technically reviewable. It exposes the bounded claim, public
OpenML task/data receipts, a standalone public-data reproducer, expected
outputs, baseline checks, holdout/split summaries, rival explanations, negative
controls, limitations, and a review template.

The receipt-first framing is useful as a review-preparation and triage
discipline: it prevents claims without concrete task/data receipts from being
treated as ready for deeper benchmark review, and it makes replay failure or
missing receipts easy to detect.

The current evidence does not justify a stronger decision because the individual
components are mostly standard benchmark-audit and reproducibility practices:
public task IDs, raw-data replay, baselines, held-out checks, leakage/rival
explanations, and negative controls. The candidate's possible value is the
bundled gate discipline, not novelty of those individual components.

## Caveats

- The deterministic first-feature holdout is a protocol-fragility probe, not an
  official or semantic split for every OpenML task.
- The term `survived` should be read narrowly as "retained as a bounded
  protocol-fragility signal", not as evidence of robust model generalization.
- The package lacks an external prior-art reviewer deciding whether the bundled
  gate differs meaningfully from existing benchmark-audit practice.
- No external reviewer or independent reproducer has accepted, rejected, or
  revised the claim.
- The local `sovryn` CLI was not available in this shell, so no Product
  external-review intake command or source-receipt command was run.

## Review Questions

1. Can the public reproducer run?

Yes, internally.

2. Do the replay rows reproduce within rounding tolerance?

Yes. Seven rows reproduce within the recorded rounding tolerance.

3. Is the receipt-first triage method useful beyond an internal checklist?

Plausibly yes as a review-readiness filter, but this remains unproven by
external evidence.

4. Does it differ meaningfully from existing benchmark-audit or reproducibility
practices?

Unclear. The package combines standard practices into a strict gate, but an
external methodology reviewer should decide whether that combination is
nontrivial.

5. Decision?

`minor_revision` for internal review purposes only. Required revisions before
score-effective consideration: independent external review, source receipt,
clearer prior-art differentiation, and stronger wording around the deterministic
holdout probe.

## Gate Consequence

- supportive: limited/internal only,
- independent: no,
- score-effective: no,
- discovery-scored: no,
- `FUND_FOUND`: no.

Next blocker: a real independent public external review or independent
reproduction record with source receipt.
