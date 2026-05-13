# Raw Scientific Reproduction

The public replay uses four public-safe Gaia EDR3 TAP source-row CSV snapshots in `raw-reproduction-bundle/source-rows/` and recomputes the bounded metric calculation from raw rows. If the snapshots are removed, the replay script can fall back to the live Gaia TAP queries recorded in `raw-reproduction-bundle/SOURCE_CACHE.json`.

Snapshot receipts are recorded in `raw-reproduction-bundle/SOURCE_ROW_RECEIPTS.json`.

Expected values:

- measuredOutcome: `0.4256`
- residualMagnitude: `0.1343`
- phot_g_mean_magnitude_correlation: `0.1372`
- bp_rp_color_correlation: `0.1126`
- single_sky_slice_dominance_control: `0.5075`

Status: `external_review_ready_raw_scientific_reproduction_succeeded_caveated_no_external_validation`.

No external validation is claimed.
