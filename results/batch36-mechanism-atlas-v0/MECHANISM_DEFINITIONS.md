# Mechanism Definitions

## protocol_sensitivity
Name: Protocol Sensitivity

Definition: evaluation outcome changes when a source-described protocol replaces a convenient split.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## random_split_inflation
Name: Random Split Inflation

Definition: random or stratified split gives a more optimistic metric than the source protocol.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## class_imbalance_metric_illusion
Name: Class Imbalance Metric Illusion

Definition: accuracy or weighted summaries mask rare-class failure visible in macro/per-class metrics.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## protocol_ambiguity_barrier
Name: Protocol Ambiguity Barrier

Definition: multiple plausible protocol interpretations block strong claims.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## duplicate_transfer
Name: Duplicate Transfer

Definition: shared exact or near-identical feature rows cross train/test boundaries.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## group_file_subject_overlap
Name: Group/File/Subject Overlap

Definition: random split mixes groups that source protocol keeps separated.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## model_family_sensitivity
Name: Model Family Sensitivity

Definition: mechanism evidence changes across linear, tree, or ensemble families.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## replay_instability
Name: Replay Instability

Definition: fresh seeds or replay environments change the conclusion.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## ordinary_benchmark_difficulty
Name: Ordinary Benchmark Difficulty

Definition: source split is harder without a specific leakage-like mechanism.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## evidence_packaging_dominance
Name: Evidence Packaging Dominance

Definition: custom tool value is mainly structured evidence rather than discovery.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## tool_value_compression
Name: Tool Value Compression

Definition: tool value narrows after baselines and kill-week attacks.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.

## no_material_mechanism_control
Name: No Material Mechanism Control

Definition: low-risk controls do not show material mechanism evidence.

Causal story: the mechanism changes what evidence a metric sees before a claim is interpreted.

Measurable indicators: macro-F1 delta, accuracy delta, class support, group overlap, duplicate overlap, protocol clarity, model variance, replay divergence.

Required controls: low-risk target, negative label control, source-vs-random challenger, replay.

Likely false positives: unsupported protocol assumptions or metric-only changes.

Likely false negatives: missing group fields or insufficient source documentation.

Known limitations: not universal and not confirmed without target-specific evidence.
