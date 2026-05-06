# Batch 13 Protocol-First Benchmark Validation Week 1

Batch 13 is the first execution batch of the Protocol-First Benchmark Validation and Split-Risk Program selected in Batch 12.

It is not a roadmap, continuity review, or benchmark-win claim. Sovryn selected exactly three public UCI targets with source-described train/test split signals, loaded the real archives, followed the source train/test files, and compared those results against ordinary stratified-random challenger splits.

## Targets

| Target | Protocol signal | Protocol status |
| --- | --- | --- |
| UCI Human Activity Recognition Using Smartphones | source archive contains train/test files and subject_train/subject_test files | protocol_reproduced |
| UCI Optical Recognition of Handwritten Digits | source archive contains optdigits.tra and optdigits.tes files | protocol_reproduced |
| UCI Pen-Based Recognition of Handwritten Digits | source archive contains pendigits.tra and pendigits.tes files | protocol_reproduced |

## Main Result

| Target | Source split logistic macro-F1 | Random challenger logistic macro-F1 | Random minus source |
| --- | ---: | ---: | ---: |
| UCI Human Activity Recognition Using Smartphones | 0.9544 | 0.9832 | 0.0288 |
| UCI Optical Recognition of Handwritten Digits | 0.9500 | 0.9722 | 0.0222 |
| UCI Pen-Based Recognition of Handwritten Digits | 0.9164 | 0.9458 | 0.0293 |

The random challenger was higher on all three targets by +0.0222 to +0.0293 macro-F1 for LogisticRegression. That does not prove the source split is the only valid benchmark protocol, and it does not support any benchmark-win claim. It does show that convenient random splits can change Sovryn's conclusions enough that protocol-first execution should be mandatory for the next program.

## Tool Use

- `metric_stress_validator` was used as a reusable support tool for shuffled-label, class-risk, macro-F1 versus accuracy, and seed/split checks.
- `schema_provenance_auditor` was used only as packaging evidence: source hashes, schema/card summaries, missingness, duplicates, and protocol metadata.
- `container_netoff_replay_recipe` replayed the evidence run with Docker network mode `none` after public data provisioning.

## Negative Or Partial Findings

- No benchmark-win claim is supported; this batch only compares source split behavior against random challengers.
- schema_provenance_auditor remained evidence packaging; pandas exposed the same raw missingness and duplicate checks.

- No official benchmark reproduction claim is made beyond following the source train/test files present in the archives.
- HAR has a stronger split-risk signal than the digit targets because the source split preserves a subject holdout boundary with zero subject overlap.

## Hard Question

Yes, at least one source-described protocol changed Sovryn's conclusion materially versus a random challenger, so Batch 13 supports protocol-first benchmark validation.
