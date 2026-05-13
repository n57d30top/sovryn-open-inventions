# Graph-Minor Residual Formula

## Public Row Fields

Each row in `raw-reproduction-bundle/formal-object-check-manifest.json` contains:

- `obstructionScore`
- `simpleBaselineScore`
- `residual`
- `density`
- `averageDegree`
- `vertices`
- `candidateMechanismHolds`
- `rivalExplains`

## Product/Manifest Definitions

`measuredOutcome`
: Mean of `obstructionScore` over all 72 rows.

`simpleBaseline`
: Mean of `simpleBaselineScore` over all 72 rows.

`rowResidual`
: `obstructionScore - simpleBaselineScore`.

`meanSignedResidualFromRows`
: Mean of `rowResidual` over all rows.

`productResidualMagnitude`
: Mean of `max(0, rowResidual)` over all rows. This explains why the Product value `0.128` differs from the signed row mean `0.105`: negative residual rows are clipped to zero before averaging.

`matched_known_family_negative_control`
: Mean `obstructionScore` among rows where `candidateMechanismHolds` is false.

`null_or_trivial_structural_rule`
: Mean of `min(density, averageDegree / vertices)` over all rows.

## Recomputed Values

| Quantity | Value |
|---|---:|
| checkedObjectCount | 72 |
| measuredOutcomeFromRows | 0.423917 |
| rounded measuredOutcome | 0.424 |
| simpleBaselineFromRows | 0.319083 |
| rounded simpleBaseline | 0.319 |
| meanSignedResidualFromRows | 0.104833 |
| rounded signed residual | 0.105 |
| meanPositiveResidualFromRows | 0.127667 |
| rounded Product residualMagnitude | 0.128 |
| meanAbsoluteResidualFromRows | 0.150500 |
| matchedKnownFamilyNegativeControlFromRows | 0.355571 |
| rounded matched negative control | 0.356 |
| nullRuleFromRows | 0.437697 |
| rounded null/trivial structural rule | 0.438 |

## Critical Caveat

The formula for the Product residual magnitude is now public and reproducible from the row fields. The scientific interpretation remains caveated because the rows are generated canonical family rows, not independently fetched HOG/GraphClasses graph objects.
