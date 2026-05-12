# Generator Audit

Passed: true.
Generator set: significance.
Family count: 3.
Latest run found: true.
Runtime checks: 30.
Hard-seed birth attempts: 30.
Hard seeds born: 6.
Generator replacement required: false.

## Generator Replacement Requirements

| Generator | Status | Runtime checks | HardSeeds born | Dominant blocker | Required change |
| --- | --- | ---: | ---: | --- | --- |
| matbench_descriptor_transfer_significance_generator | productive_or_not_run | 10 | 2 | unsupported_domain_significance_hypothesis | No replacement required from the latest run. |
| gaia_astrometric_excess_significance_generator | productive_or_not_run | 10 | 2 | unsupported_domain_significance_hypothesis | No replacement required from the latest run. |
| bounded_graph_minor_obstruction_significance_generator | productive_or_not_run | 10 | 2 | unsupported_domain_significance_hypothesis | No replacement required from the latest run. |

## Generator Pressure Yield

Pressure run found: true.
Seeds loaded: 9.
Tests run: 63.
Seeds killed by baseline: 0.
InsightCandidates created: 9.
DiscoveryCandidates created: 0.
No InsightCandidate after born seeds: false.
Dominant blocker: none.
Recommended action: continue generator-born InsightCandidate closure with full downstream gates.

## Generator FundClass Closure Yield

Closure run found: true.
Closure candidates: 9.
Discovery-scored candidates: 0.
Non-discovery classified candidates: 9.
All closed as non-discovery: true.
Dominant FundClass: pipeline_fund_candidate.
Recommended action: create a new stable DiscoveryCandidate claim lift with external scientific significance before rerunning long searches; current closure candidates classify as pipeline_fund_candidate because the frozen InsightCandidate scope still carries anti-discovery or pipeline-scope caveats.

| Gate | Passed | Message |
| --- | --- | --- |
| registry_has_three_new_families | true | Generator registry must include the three required mechanism-first families for the selected generator set. |
| registry_families_have_external_problem_anchors | true | Every generator family must start from a public external problem anchor with explicit domain scientific significance and at least two public significance refs. |
| latest_run_present | true | Generator audit requires a focused generator run artifact. |
| runtime_checks_target_met | true | Focused generator validation must run at least thirty runtime checks when all families run. |
| every_output_has_birth_decision | true | Every generator output must explicitly decide hardSeedBirth born or blocked. |
| external_value_gate_blocks_internal_only_outputs | true | ExternalValueGate must run before HardSeed birth and block internal-only outputs when present. |
| success_or_precise_blockers | true | Focused validation must either produce a birth-eligible hard seed or prove precise blocker causes for every output. |
| no_birth_requires_replacement_requirements | true | If runtime generator validation creates no HardSeeds, the audit must expose concrete generator replacement requirements instead of a green-only audit. |
| pressure_yield_not_fake_green | true | Generator audit must not stay green after generator-pressure kills every born hard seed before InsightCandidate birth. |
| post_closure_discovery_yield_not_fake_green | true | Generator audit must not stay green after package/Fund closure classifies every closure candidate as non-discovery unless a later claim-lift intake produced a discovery-scored Fund. |
| no_fake_fund | true | Generator runs must not create FUND_FOUND.md or fund-candidate.json; a later discovery-scored claim-lift intake may own root Fund state. |
