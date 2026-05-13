# Extended Gaia Validation Supplement

This supplement adds fresh public Gaia TAP panels and stronger rival controls. It does not strengthen the bounded claim and does not claim external validation.

Overall status: `extended_validation_rival_explained_signal`.

| Panel | Purpose | Rows | Measured outcome | Residual magnitude | Strongest rival | Strongest rival score | Cross-slice support | Counterexample collapsed |
| --- | --- | ---: | ---: | ---: | --- | ---: | --- | --- |
| primary_equatorial_replay | exact replay panel | 160 | 0.4256 | 0.1343 | ruwe_correlation_rival | 0.4951 | true | false |
| north_declination_holdout | independent declination holdout | 80 | 1.3326 | 1.2495 | ruwe_correlation_rival | 0.5442 | true | true |
| south_declination_holdout | independent declination holdout | 80 | 0.2249 | 0.1204 | ruwe_correlation_rival | 0.483 | true | false |
| bright_magnitude_control | negative/control magnitude slice | 80 | 0.1291 | 0.031 | ruwe_correlation_rival | 0.9825 | false | true |

## Interpretation

- The original exact replay remains the authoritative bounded package claim.
- RUWE is treated as a strong catalog-quality rival proxy, not as support for a new astrophysical mechanism.
- On the primary panel, residual magnitude after a linear G/color/RUWE control is `0.0263` and cross-slice support is `false`.
- If the RUWE-adjusted residual loses cross-slice support or falls below the nontrivial threshold, this public package no longer counts as a discovery-scored candidate.
- Holdout panels are independent public declination slices, but they are still Gaia-internal and do not equal outside expert validation.
- Any strong RUWE/catalo-quality rival should downgrade scientific interpretation unless an external reviewer accepts the narrower residual claim.
