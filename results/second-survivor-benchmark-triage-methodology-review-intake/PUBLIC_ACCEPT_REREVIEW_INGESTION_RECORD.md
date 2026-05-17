# Public Accept Re-Review Ingestion Record

Candidate: `DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001`

Public review URL:

- https://github.com/n57d30top/sovryn-open-inventions/issues/1#issuecomment-4470388033

## Ingested Decision

Decision: `accept`.

Accepted scope: bounded, conservative, publicly inspectable
`pipeline_fund_candidate` methodology package.

The comment reports that `node reproduce_v2_100_claim_challenge.js` was run at
corpus commit `c4f4827` and reproduced:

- 100 claims;
- 42 independent tasks/datasets;
- V2: 17/17 survivors, yield `1.000`;
- baseline-only: 17/25 survivors, yield `0.680`;
- 8 baseline-only false advances filtered by V2;
- conservative `public-field deterministic split manifests` wording;
- `fundFound=false`;
- `discoveryScored=false`;
- `notificationAllowed=false`.

## Source Receipt Check

The GitHub API receipt is public and resolvable.

Receipt fields:

- comment ID: `4470388033`;
- reviewer login visible on receipt: `n57d30top`;
- author association: `OWNER`;
- created: `2026-05-17T11:10:33Z`.

## Independence Classification

Independence: no.

Reason: the public GitHub receipt is owner-authored. It is a real public source
receipt for the accept re-review content, but it does not establish independent
third-party review or reproduction.

## Score Effect

Score-effective: no.

The accept decision is useful review-history evidence and closes the previous
`public_receipt_missing` blocker. It does not pass the Review Score Contract
because independence is not established.

## Gate Consequence

- Candidate remains `pipeline_fund_candidate`.
- Discovery-scored remains no.
- Notification allowed remains no.
- `FUND_FOUND=false`.

Next blocker: independent public reviewer/reproducer receipt.
