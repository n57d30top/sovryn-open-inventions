# Reproduce

From this result directory:

```bash
python3 reproduce_gaia_candidate.py
```

The script uses only Python standard library modules and public Gaia TAP endpoints. It writes:

- `standalone_reproduction_result.json`
- `REPRODUCTION_RESULT_TABLE.md`

Expected exact values are embedded in the script and are also available in `copied-product-evidence/gaia-source-cache.json`.

If Gaia TAP is unavailable, the replay may fail operationally. That should be recorded as replay unavailable, not as external validation failure.

## Extended validation supplement

Run:

```bash
python3 validate_gaia_candidate_extended.py
```

This fetches additional public Gaia TAP panels and writes:

- `extended_validation_result.json`
- `EXTENDED_VALIDATION_TABLE.md`

The supplement is slower than the exact replay because it performs additional public TAP queries. It is a review-pressure artifact, not a stronger claim and not external validation.
