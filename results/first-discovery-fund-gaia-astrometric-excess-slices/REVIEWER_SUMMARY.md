# Reviewer Summary

## Precise bounded claim

For the exact public Gaia EDR3 TAP slices used here, mean astrometric_excess_noise is 0.4256 and the simple magnitude/color residual model leaves a cross-slice mean absolute residual of 0.1343. The residual is bounded to four public RA slices, 160 rows, and the recorded magnitude, color, and single-slice dominance controls; it is not a claim of a new astrophysical object, global Gaia calibration law, or external validation.

## Main scalar checks

- Measured outcome: `0.4256`
- Residual magnitude: `0.1343`
- Baselines: magnitude correlation `0.1372`, color correlation `0.1126`, single-slice dominance `0.5075`

## Extended validation supplement

An additional public Gaia TAP supplement preserves exact primary replay and adds fresh declination holdouts, a bright-magnitude control, RUWE, and visibility-period rival proxies.

- Extended validation status: `extended_validation_rival_explained_signal`
- Primary exact replay: `true`
- Holdout-supported panel count: `1`
- RUWE rival explains primary signal: `true`
- Primary G/color/RUWE adjusted residual magnitude: `0.0263`
- Primary G/color/RUWE adjusted cross-slice support: `false`

This supplement does not strengthen the claim. It downgrades the public interpretation: the raw scalar replay succeeds, but the strongest public catalog-quality rival explains/collapses the primary residual support. The public package should be treated as a replayable killed/downgraded candidate, not as a discovery-scored result.

## Caveats

This is an internally generated candidate package with exact public raw replay for the bounded metric calculation. It is not external validation. The current public extended validation blocks Einstein/Nobel discovery scoring because RUWE explains the residual under the added control.

The strongest newly exposed caveat is now decisive for public scoring: RUWE behaves as a catalog-quality rival proxy and the G/color/RUWE adjustment collapses cross-slice support.

## Downgrade triggers

The candidate is already downgraded for public discovery scoring. Reconsider only if a new or narrowed candidate survives a preregistered Gaia quality-control rival, independent support, replay, and external expert scrutiny.
