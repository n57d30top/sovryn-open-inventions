# Reviewer Summary

## Precise bounded claim

For the exact public Gaia EDR3 TAP slices used here, mean astrometric_excess_noise is 0.4256 and the simple magnitude/color residual model leaves a cross-slice mean absolute residual of 0.1343. The residual is bounded to four public RA slices, 160 rows, and the recorded magnitude, color, and single-slice dominance controls; it is not a claim of a new astrophysical object, global Gaia calibration law, or external validation.

## Main scalar checks

- Measured outcome: `0.4256`
- Residual magnitude: `0.1343`
- Baselines: magnitude correlation `0.1372`, color correlation `0.1126`, single-slice dominance `0.5075`

## Extended validation supplement

An additional public Gaia TAP supplement preserves exact primary replay and adds fresh declination holdouts, a bright-magnitude control, RUWE, and visibility-period rival proxies.

- Extended validation status: `extended_validation_major_rival_caveat`
- Primary exact replay: `true`
- Holdout-supported panel count: `1`
- Major rival caveat: RUWE is the strongest rival proxy in the primary and holdout/control panels.

This supplement does not strengthen the claim. It narrows the external-review question: a reviewer should decide whether the bounded residual is scientifically meaningful after accounting for Gaia catalog-quality proxies, especially RUWE.

## Caveats

This is an internally generated discovery-scored candidate package with exact public raw replay for the bounded metric calculation. It is not external validation. A domain expert must still judge novelty, physical interpretation, sample adequacy, and whether the residual is scientifically important rather than a catalog-selection artifact.

The strongest newly exposed caveat is that RUWE behaves as a major catalog-quality rival proxy. The candidate should be downgraded if that rival fully explains the residual under expert review.

## Downgrade triggers

Downgrade if the Gaia TAP replay no longer reproduces the metrics, if a stronger catalog-quality or scan-law rival explains the residual, if independent slices fail, or if a reviewer finds the mechanism already known/trivial for this bounded slice.
