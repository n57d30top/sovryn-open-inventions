# Comparative Ablation Plan

The major-revision review criticized the weak reject-all comparison. V2 treats
comparators as first-class baselines.

## Comparators

| Comparator                       | Definition                                                             | What It Tests                                  |
| -------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------- |
| Reject-all                       | Select zero claims                                                     | Whether V2 has any retention value             |
| Accept-all                       | Select every replayable row                                            | Whether V2 filters weak replayable rows        |
| Random task selection            | Select a fixed number without evidence                                 | Whether V2 beats chance                        |
| Stratified baseline selection    | Select across task families if labels exist                            | Whether diversity alone explains selection     |
| Task-size heuristic              | Select largest tasks                                                   | Whether scale explains survival                |
| Baseline-only heuristic          | Select `modelVsBaselineDelta >= 0.08`                                  | Whether V2 adds value beyond baseline margin   |
| Leakage-aware heuristic          | Select `randomVsHoldoutDelta >= 0.20`                                  | Whether holdout delta alone explains selection |
| GroupKFold where applicable      | Use real group key                                                     | Not available in current seven-row package     |
| StratifiedKFold where applicable | Use target-stratified repeated split                                   | Required for next re-review benchmark          |
| Multiple holdout policies        | Compare random, first-feature bucket, group/entity/time when available | Whether holdout policy drives outcome          |

## Success Criteria For Future Re-Review

V2 is not considered fully repaired unless it:

- beats reject-all on useful retained claims,
- beats or scopes baseline-only selection on a larger mixed benchmark,
- retains at least one externally plausible non-control claim,
- rejects at least one replayable but weak claim,
- improves survivor yield after deep validation.

The current seven-row package can test only a small part of this plan.
