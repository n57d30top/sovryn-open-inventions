# Next 4-Week Frontier Program

Selected program: Protocol-First Benchmark Validation and Split-Risk Program

Domain: benchmark metric validation plus scientific dataset reliability

Primary research question:

When public benchmarks include source-described split or protocol information, how much do Sovryn's conclusions change compared with ordinary random or stratified splits?

Why selected:

Batches 9 and 11 repeatedly hit the same limitation: strong baselines ran, but official protocols were not reproduced. Batch 10 narrowed the tools to support roles, so the next useful frontier is protocol-aware execution, not more single-table scoring.

Rejected alternatives:

| Alternative | Reason rejected |
| --- | --- |
| More single-table UCI metric validation | Rejected because Batch 11 found mostly pandas/sklearn-dominated raw findings. |
| Pure repo/test reproduction | Deferred because pytest static/runtime reconciliation and dependency variance need a smaller support-tool upgrade first. |
| Source/evidence extraction program | Rejected for now because recent results were less execution-backed than dataset and benchmark work. |
| Time-series anomaly benchmark program | Narrowed because Air Quality was valuable but the current toolchain fits protocol-bearing classification/regression targets better. |

## Weekly Goals

- Week 1: select three protocol-bearing benchmark targets, create source protocol cards, load official files, and run first official-vs-random baseline comparisons.
- Week 2: expand to four targets, run metric stress, shuffled-label controls, class-risk checks, and split-family comparisons.
- Week 3: choose one deep target for container replay, duplicate-crossing checks, one small split-risk helper if needed, and an extension attempt.
- Week 4: attack the program results, downgrade overstrong protocol claims, publish preserved/negative findings, and select the next deep target.

## Target Types

- public benchmarks with source-described train/test splits
- public benchmarks with contributor, writer, subject, file, or temporal split risk
- public benchmarks where simple baselines are strong enough to challenge claims

## Candidate External Targets

- UCI Human Activity Recognition Using Smartphones
- UCI Letter Recognition
- UCI Optical Recognition of Handwritten Digits
- UCI Pen-Based Recognition of Handwritten Digits
- UCI Statlog Landsat Satellite
- UCI Statlog Shuttle
- UCI Image Segmentation
- UCI Statlog Vehicle Silhouettes follow-up

## Required Tools

- metric_stress_validator
- schema_provenance_auditor as packaging-only evidence
- reproduction ladder artifact pack
- container_netoff_replay_recipe
- tiny target-specific split loader only if a source protocol requires it

## Expected Execution Requirements

- real public dataset loads
- official split or source-described protocol attempt
- random/stratified split challenger
- dummy, linear, and tree baselines
- container or fresh-workspace replay for at least two targets

## Expected Baselines

- majority or stratified dummy
- linear/logistic model
- tree or forest model
- source-protocol baseline

## Expected Negative Controls

- shuffled labels
- random split versus official split
- per-class weakness report
- duplicate-crossing check where duplicates exist

## Replay Plan

At least two container or fresh-workspace replays, plus fresh-seed/split replays for every target with random split challengers.

## Stop Criteria

- Fewer than three targets can be loaded or source protocols cannot be verified.
- Every candidate reduces to ordinary random split scoring with no protocol-specific question.
- Public-safe source cards cannot be created for the selected targets.

## Success Criteria

- At least three official/source-protocol attempts run.
- At least two targets show measured protocol-vs-random split comparison.
- At least one negative or downgrade result is published.
- All claims survive baseline, negative-control, and replay checks.

## Failure Criteria

- The program reports benchmark wins instead of protocol-risk evidence.
- The tools are credited for findings fully explained by simple baselines without saying so.
- Replay is skipped or fallback targets are hidden.

## Publication Criteria

- public corpus package with source cards, protocol cards, execution matrices, baselines, metric stress, replay evidence, and limitations
- no unsupported benchmark reproduction claim
- explicit downgrade section for every weak target or tool
