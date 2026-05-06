# Batch 14 Protocol Risk Expansion Week 2

Batch 14 expands the Protocol-First Benchmark Validation program from the three Batch 13 targets to four targets with harder split-risk coverage.

It is not a roadmap, continuity note, benchmark-win claim, or full official benchmark reproduction. The executed claim is narrower: Sovryn followed or approximated public source-described split protocols, compared them with same-size stratified-random challengers, and scored split-risk severity.

## Targets

| Target | New vs Batch 13 | Protocol status | Split-risk severity |
| --- | --- | --- | --- |
| UCI Human Activity Recognition Using Smartphones | carry_forward_control | protocol_reproduced | moderate |
| UCI Statlog Shuttle | new | protocol_reproduced | high |
| UCI Statlog Landsat Satellite | new | protocol_reproduced | high |
| UCI Letter Recognition | new | protocol_approximated | low |

## Main Result

| Target | Source/protocol Logistic macro-F1 | Random challenger Logistic macro-F1 | Random minus source | Severity |
| --- | ---: | ---: | ---: | --- |
| UCI Human Activity Recognition Using Smartphones | 0.9544 | 0.9832 | 0.0288 | moderate |
| UCI Statlog Shuttle | 0.3828 | 0.4530 | 0.0702 | high |
| UCI Statlog Landsat Satellite | 0.7971 | 0.8192 | 0.0222 | high |
| UCI Letter Recognition | 0.7699 | 0.7728 | 0.0028 | low |

Batch 14 found two high-severity targets: Shuttle and Landsat. Shuttle was the largest change, with random split Logistic macro-F1 higher by +0.0702 even while accuracy barely moved. Letter Recognition was different: the random delta was small, but the protocol itself is only approximated from documentation order rather than reproduced from separate train/test files.

## Hard Question

Yes. Batch 14 found protocol-first evaluation still changes conclusions across 4 targets; 2 targets reached high or severe split-risk severity, and 1 target introduced documentation-order protocol ambiguity. Highest risk came from class imbalance, documentation-only order splits, and source train/test files whose random challengers substantially changed macro-F1.

## Negative Or Partial Findings

- No benchmark-win claim is supported; this batch only compares source-described protocols with random challengers.
- At least one protocol was approximated from documentation rather than reproduced from separate train/test files.
- At least one target had high or severe split-risk severity.
- Accuracy alone hid enough class-level weakness to require macro-F1 and per-class reporting.
- schema_provenance_auditor remained evidence packaging; pandas exposed the raw missingness and duplicate checks.
