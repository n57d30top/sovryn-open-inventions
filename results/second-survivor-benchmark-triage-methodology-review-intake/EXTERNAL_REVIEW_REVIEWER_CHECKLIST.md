# External Review Reviewer Checklist

| Gate | Question | Public evidence refs | Required reviewer outcome |
| --- | --- | --- | --- |
| claim_identity | Does the package preserve the exact candidate identity and claim without scope drift? | `EXACT_CLAIM.md`, `METHODOLOGY_EXACT_CLAIM.md`, `CLAIM_EVIDENCE_BINDINGS.json` | Confirm the reviewed claim is the same bounded package claim or request revision. |
| method_reproduction | Can the method and replay instructions be followed from public artifacts? | `METHOD.md`, `REPRODUCE.md`, `reproduce_second_survivor_benchmark.js`, `standalone_replay_results.json` | Record successful reproduction, bounded replay caveat, or blocking failure. |
| evidence_bindings | Do the claim-evidence bindings connect every major claim element to resolvable public evidence? | `CLAIM_EVIDENCE_BINDINGS.json`, `PUBLIC_REVIEW_URLS.md` | Confirm bindings are inspectable and sufficient or list missing evidence. |
| baseline_rival_holdout_pressure | Do baselines, rival mechanisms, holdouts, negative controls, and replay pressure support the bounded claim? | `BASELINES.md`, `RIVAL_EXPLANATIONS.md`, `HOLDOUT_REPLAY.md`, `NEGATIVE_CONTROLS.md`, `METHODOLOGY_VALUE_TESTS.md` | Confirm the pressure is nonfatal for the bounded claim or identify a fatal blocker. |
| public_raw_replay | Does standalone replay use public raw receipts without reading Product state? | `STANDALONE_REPLAY_RESULTS.md`, `standalone_replay_results.json`, `REVIEWER_REPLAY_QUICKCHECK.md`, `reviewer_replay_quickcheck_result.json` | Confirm public raw replay, reproduce it independently, or record the replay failure. |
| limitations_and_no_overclaim | Are limitations explicit, and does the package avoid prohibited overclaim categories? | `LIMITATIONS.md`, `README.md`, `SUMMARY.json` | Confirm limitations are adequate or request narrower wording. |
| review_record | Can the review result be written as a source-backed record? | `EXTERNAL_REVIEW_RECORD_TEMPLATE.json`, `EXTERNAL_REVIEW_INTAKE_INSTRUCTIONS.md` | Provide a public-source review record only after real review/reproduction work. |
