# Rival Theory Results Table

| Rival explanation | Check | Result | Status |
| --- | --- | --- | --- |
| Apparent residual is explained by G magnitude | Absolute Pearson correlation between phot_g_mean_mag and astrometric_excess_noise | 0.1372 | Weakened for this bounded slice |
| Apparent residual is explained by bp_rp color | Absolute Pearson correlation between bp_rp and astrometric_excess_noise | 0.1126 | Weakened for this bounded slice |
| Apparent residual is one-slice dominance | Largest absolute slice residual share | 0.5075 | Below collapse threshold used by Product |
| Apparent residual is explained by Gaia catalog-quality proxy RUWE | Extended validation absolute Pearson correlation between RUWE and astrometric_excess_noise in the primary panel | 0.4951 | Major rival caveat; not resolved by this package |
| Apparent residual is explained by visibility-period proxy | Extended validation absolute Pearson correlation between visibility_periods_used and astrometric_excess_noise in the primary panel | 0.1883 | Weaker than RUWE for this panel |

These checks do not eliminate all possible Gaia catalog-quality or scan-law explanations. They only document the Product-bound rival checks.

The extended validation supplement makes the catalog-quality rival sharper: RUWE is the strongest rival proxy in the primary replay, north holdout, south holdout, and bright-magnitude control panels.
