# Review Response To Minor Revision

Reported decision: `minor_revision`.

The re-review says the baseline-only critique is substantially addressed by the
larger V2 survivor-yield challenge:

- V2 selected 17 plausible claims and all 17 survived.
- baseline-only selected 25 plausible claims and 17 survived.
- V2 yield is `1.000`; baseline-only yield is `0.680`.
- the 8 extra baseline-only advances were false advances filtered by V2.

## Revision 1: Standalone 100-Claim Reproducer

Added:

- `REPRODUCE_V2_100_CLAIM_CHALLENGE.md`
- `reproduce_v2_100_claim_challenge.js`
- `EXPECTED_V2_100_CLAIM_OUTPUT.json`

The script reads only public package files and writes
`v2_100_claim_reproducer_result.json`. It does not read Product `.sovryn`
state.

## Revision 2: Conservative Manifest Wording

Added:

- `GROUP_TIME_ENTITY_WORDING_CLARIFICATION.md`
- `UPDATED_LIMITATIONS.md`

Updated wording distinguishes:

- public-field deterministic split manifests;
- stress-test splits constructed from public fields;
- official dataset-author protocols, which are not claimed unless documented by
  an external source.

## Status After Response

The minor-revision blockers are addressed for package reviewability, but not for
discovery scoring.

- public independent re-review URL: no
- score-effective review: no
- FundClass: `pipeline_fund_candidate`
- discovery-scored: no
- `FUND_FOUND`: no
