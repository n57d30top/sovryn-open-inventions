# Novelty Gap Report

The items below are candidate novelty gaps and possible differentiators. They are not patentability conclusions, legal novelty opinions, or freedom-to-operate opinions.

## evidence-bound-research-factory

Candidate novelty gap: combine source discovery, source reading, feature extraction, candidate selection, prototype verification, and release packaging in one auditable open-source factory.

Source overlap summary: Sources overlap on evidence traces, agent verification, and reproducible research workflows.
Possible differentiator: possible differentiator: source-card-backed evidence gates plus generated Open Invention dossiers and sandbox-local prototype execution.
Why it could matter: A complete evidence chain can make open defensive publication artifacts more credible and reproducible.
Why it may already exist: Existing research automation, CI systems, lab notebooks, or agent frameworks may already implement overlapping workflows.
Required experiment: Run a fixture-backed factory cycle and verify source-card, matrix, prototype-execution, and dry-run publication evidence.
Prototype feasibility: high
Evidence strength: medium
Novelty risk: high
Recommended next action: Prototype a deterministic evidence scorer that rejects query-link-only prior-art evidence.

Missing in sources:
- manual review of query links
- retry failed adapters

## curated-public-evidence-without-raw-logs

Candidate novelty gap: publish public research evidence summaries while keeping raw command logs and local execution details private.

Source overlap summary: Existing release systems may publish logs, summaries, or redacted artifacts.
Possible differentiator: possible differentiator: factory-level public release curation tied to research evidence hashes.
Why it could matter: Public readers can inspect evidence quality without seeing private local paths, tokens, or raw command output.
Why it may already exist: Many CI and release systems already redact logs or publish summaries; compare carefully.
Required experiment: Package release/public and assert it contains no stdout, stderr, command journal, or absolute local paths.
Prototype feasibility: high
Evidence strength: medium
Novelty risk: medium
Recommended next action: Verify release/public contains only curated summaries and no stdout/stderr logs.

Missing in sources:
- factory-specific public evidence allowlist

## mock-aware-research-quality-gate

Candidate novelty gap: cap factory readiness when evidence consists of query links, adapter failures, or mock placeholders.

Source overlap summary: Related systems may score quality, but often do not distinguish query links, adapter failures, and mock placeholders as separate evidence classes.
Possible differentiator: possible differentiator: strict evidence mode turns weak source classes into explicit blockers.
Why it could matter: It prevents generated research documents from appearing stronger than their source evidence supports.
Why it may already exist: Quality gates and confidence scoring are common; the differentiator must be the specific open-invention evidence model.
Required experiment: Enable strictEvidenceMode and verify no concrete sources or no source reads block the factory run.
Prototype feasibility: high
Evidence strength: low
Novelty risk: medium
Recommended next action: Test scoring caps for missing concrete sources, missing prototype, and missing tests.

Missing in sources:
- manual review of query links
- retry failed adapters

## Limitations

- These are candidate novelty gaps, not legal novelty or patentability conclusions.
- Each gap requires human review against concrete prior art before serious use.
