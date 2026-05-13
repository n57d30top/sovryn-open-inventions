# Method

1. Query Gaia EDR3 through the public TAP sync endpoint for four RA slices: 0-90, 90-180, 180-270, and 270-360 degrees.
2. In each slice, select the first 40 ordered `source_id` rows with `dec` between -30 and 30, `phot_g_mean_mag` between 14 and 20, non-null `bp_rp`, and non-null `astrometric_excess_noise`.
3. Compute mean `astrometric_excess_noise` as the measured outcome.
4. Compute a simple rival residual model: `0.08 + max(0, G - 16) * 0.1 + abs(bp_rp - 1.2) * 0.08`.
5. Compute mean residual per RA slice and the mean absolute slice residual magnitude.
6. Compute three simple rival/baseline controls: magnitude correlation, color correlation, and single-slice dominance.
7. Treat the claim as bounded to this exact data slice and this exact metric calculation.

This method does not prove a broad astrophysical mechanism. It creates an externally inspectable candidate for expert review.

## Extended validation supplement

The supplementary script `validate_gaia_candidate_extended.py` keeps the original replay method unchanged, then adds:

- north and south declination holdout panels,
- a bright-magnitude control panel,
- RUWE and visibility-period rival proxy correlations,
- counterexample-collapse checks for cross-slice support and single-slice dominance.

The supplement currently records `extended_validation_major_rival_caveat`: exact primary replay succeeds, one independent declination holdout is supportive with caveats, and RUWE remains the strongest catalog-quality rival proxy. This does not strengthen the Product claim.
