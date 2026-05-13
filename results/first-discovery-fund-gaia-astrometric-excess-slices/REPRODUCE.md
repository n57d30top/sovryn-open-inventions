# Reproduce

From this result directory:

```bash
python3 reproduce_gaia_candidate.py
```

The script uses only Python standard library modules and public Gaia TAP endpoints. It writes:

- `standalone_reproduction_result.json`
- `REPRODUCTION_RESULT_TABLE.md`

By default the script first uses the public-safe source-row CSV snapshots in
`raw-reproduction-bundle/source-rows/`. If those snapshots are removed, it falls
back to the live Gaia TAP queries recorded in `raw-reproduction-bundle/SOURCE_CACHE.json`.

Expected exact values are embedded in the script and are also available in `copied-product-evidence/gaia-source-cache.json`.

If Gaia TAP is unavailable and the source-row snapshots are unavailable, the replay may fail operationally. That should be recorded as replay unavailable, not as external validation failure.

## Extended validation supplement

Run:

```bash
python3 validate_gaia_candidate_extended.py
```

This fetches additional public Gaia TAP panels and writes:

- `extended_validation_result.json`
- `EXTENDED_VALIDATION_TABLE.md`
- `ruwe_rival_closure_result.json`
- `RUWE_RIVAL_CLOSURE_RESULTS.md`

By default the extended validation script now uses the public-safe extended source-row snapshots in `raw-reproduction-bundle/extended-source-rows/`. If those snapshots are removed, it falls back to live Gaia TAP and writes fresh snapshots.

The supplement is a review-pressure artifact, not a stronger claim and not external validation. Its current public decision is `extended_validation_rival_explained_signal`.
