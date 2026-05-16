# Review Request Draft

Subject: Request for independent review: receipt-first triage for ML benchmark claims

I am requesting an independent methodology review and/or reproduction of a
bounded benchmark-triage package.

https://github.com/n57d30top/sovryn-open-inventions/tree/main/results/second-survivor-benchmark-triage-methodology-review-intake

The package is not claimed as a discovery, not externally validated, and not
`FUND_FOUND`. Internally it is classified only as a `pipeline_fund_candidate`,
meaning: a review-ready pipeline/methodology candidate that still needs
independent external review before it can affect any higher-level score.

Bounded claim:

A receipt-first benchmark triage method may help filter ML benchmark claims by
requiring concrete public task IDs, raw-data replay, baselines, holdout/split
checks, rival explanations, and negative controls.

What reviewers can inspect:

- exact claim,
- public OpenML task/data receipts,
- standalone reproducer,
- expected outputs,
- baseline, rival, holdout, and negative-control summaries,
- limitations,
- review intake template.

Quick reproduction:

```bash
node reproduce_second_survivor_benchmark.js
```

Current local dry-run status:

`public_raw_replay_reproduced_with_rounding_caveat`.

Seven replay rows are validated; one OpenML-32 rounded metric differs by
`0.001`.

Review questions:

1. Can you run the public reproducer?
2. Do the replay rows reproduce within rounding tolerance?
3. Is the receipt-first triage method useful beyond an internal checklist?
4. Does it differ meaningfully from existing benchmark-audit or reproducibility
   practices?
5. Decision: `accept`, `minor_revision`, `major_revision`, or `reject`.

A rejection or major revision is useful. Please do not provide a positive review
unless it is actually justified.

A review can affect readiness only if it has an external public URL and source
receipt. Major-revision, rejected, private, or non-reproduced reviews will not
increase readiness.
