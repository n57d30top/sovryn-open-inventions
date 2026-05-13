# Dataset And Target Table

| Field | Value |
| --- | --- |
| Public source | Gaia EDR3 TAP archive |
| Source ref | https://gea.esac.esa.int/archive/ |
| Rows | 160 |
| Slice design | Four RA slices: 0-90, 90-180, 180-270, 270-360; dec -30..30; G 14..20 |
| Measured variable | cross-slice recurrence of astrometric-excess residual after magnitude, color, sky-position, and source-density baselines |
| Target outcome | public Gaia EDR3 astrometric-excess residual recurrence after magnitude, color, and single-slice dominance controls |
| Loader/check command | `sovryn discover-daemon discovery-anchor-source-load --anchor DISC-ANCHOR-GAIA-ASTROMETRIC-EXCESS-SLICES` |
| Source hash | `7c43de1cee140dabf413eb7c7456481a850821a2931ddf01139cc76576131268` |
