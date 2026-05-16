# Review in 10 Minutes

This is the shortest useful review path for an independent reviewer.

## 1. Clone or Download

```bash
git clone https://github.com/n57d30top/sovryn-open-inventions.git
cd sovryn-open-inventions/results/second-survivor-benchmark-triage-methodology-review-intake
```

## 2. Run the Reproducer

Node.js 18 or newer is required. No third-party runtime dependencies are required.

```bash
node reproduce_second_survivor_benchmark.js
node reviewer_replay_quickcheck.js
```

## 3. Compare Expected Output

Open:

- `EXPECTED_REPRODUCER_OUTPUTS.json`
- `standalone_replay_results.json`
- `reviewer_replay_quickcheck_result.json`

Expected summary:

- replay rows: 7
- replay status: `public_raw_replay_reproduced_with_rounding_caveat`
- metrics within rounding tolerance: true
- `fundFound=false`
- `countsForDiscoveryScore=false`

Known caveat:

- OpenML-32 has a displayed rounded metric difference of `0.001`.

## 4. Answer Three Questions

1. Did the reproducer run?
2. Did the replay rows match within rounding tolerance?
3. Is the receipt-first triage method useful beyond an internal checklist?

## 5. Paste a Public Comment

Use `GITHUB_EXTERNAL_REVIEW_COMMENT_TEMPLATE.md` or one of the templates in `EXTERNAL_REVIEW_ISSUE_TEMPLATES.md`.

## Score-Impact Boundary

This fast path can only become score-effective if the review is public, independent, and includes an explicit decision. A private note or owner/internal comment will not count.
