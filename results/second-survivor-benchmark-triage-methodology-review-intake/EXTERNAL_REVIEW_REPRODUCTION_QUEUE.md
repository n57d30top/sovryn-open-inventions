# External Review Reproduction Queue

| Step | Action | Public input refs | Expected reviewer evidence | Status |
| --- | --- | --- | --- | --- |
| review-package-inventory | Open the public package and verify required artifacts are present. | `README.md`, `SUMMARY.json`, `PUBLIC_REVIEW_URLS.md` | Artifact inventory matches the public bundle manifest. | queued_for_human_review |
| review-claim-bindings | Inspect `CLAIM_EVIDENCE_BINDINGS.json` and sample every evidence-ref class. | `CLAIM_EVIDENCE_BINDINGS.json`, `EXTERNAL_REVIEW_EVIDENCE_REF_INDEX.md` | Each claim element has a resolvable public supporting ref or a documented gap. | queued_for_human_review |
| run-public-replay | Follow `REPRODUCE.md` and run the standalone replay script if feasible. | `REPRODUCE.md`, `reproduce_second_survivor_benchmark.js`, `standalone_replay_results.json` | Reviewer-owned command/result summary with exact or caveated replay status. | queued_for_human_review |
| evaluate-pressure | Assess baseline, rival, holdout, negative-control, and methodology-value artifacts. | `BASELINES.md`, `RIVAL_EXPLANATIONS.md`, `HOLDOUT_REPLAY.md`, `NEGATIVE_CONTROLS.md`, `METHODOLOGY_VALUE_TESTS.md` | Reviewer decision: support, request changes, or reject the bounded claim. | queued_for_human_review |
| write-source-backed-review | If real review occurs, fill the public review template and bind it to an external review URL/source receipt. | `EXTERNAL_REVIEW_RECORD_TEMPLATE.json`, `EXTERNAL_REVIEW_INTAKE_INSTRUCTIONS.md` | Source-backed review record suitable for Sovryn intake. | queued_for_human_review |

No step in this queue creates `FUND_FOUND`; a future review can affect readiness only after source-backed intake and unchanged Product gates.
