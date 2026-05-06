# Split Risk Severity

| Target | Delta macro-F1 random-source | Delta accuracy random-source | Class distribution shift | Protocol ambiguity score | Group/file/temporal risk | Replay max delta | Claim risk score | Severity |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |
| UCI Human Activity Recognition Using Smartphones | 0.0288 | 0.0275 | 0.0238 | 0 | true | 0.0016 | 2 | moderate |
| UCI Statlog Shuttle | 0.0702 | -0.0032 | 0.0077 | 0 | true | 0.0703 | 3 | high |
| UCI Statlog Landsat Satellite | 0.0222 | 0.0215 | 0.0294 | 0 | true | 0.0176 | 3 | high |
| UCI Letter Recognition | 0.0028 | 0.0022 | 0.0330 | 1 | false | 0.0065 | 1 | low |

Severity labels:

- `none`: no meaningful delta or protocol concern observed.
- `low`: small metric delta or protocol ambiguity without large metric change.
- `moderate`: material delta or protocol/group risk requiring caution.
- `high`: material delta plus group/file/temporal risk, class-risk, replay instability, or ambiguity.
- `severe`: very high combined score; not reached in Batch 14.
