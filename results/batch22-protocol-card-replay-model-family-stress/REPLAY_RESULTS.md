# Replay Results

| target | replay status | protocol status | source macro-F1 | random macro-F1 | delta |
| --- | --- | --- | --- | --- | --- |
| UCI HAR Smartphones | replay_passed | protocol_reproduced | 0.935249 | 0.975267 | 0.040018 |
| UCI Statlog Shuttle | replay_passed | protocol_reproduced | 0.382773 | 0.453021 | 0.070248 |
| UCI Statlog Landsat Satellite | replay_passed | protocol_reproduced | 0.742615 | 0.707262 | -0.035353 |
| UCI Letter Recognition | replay_passed | protocol_approximated | 0.692537 | 0.689473 | -0.003064 |
| UCI Vehicle Silhouettes | protocol_ambiguous | protocol_ambiguous | 0.810683 | 0.848314 | 0.037631 |

Two container-netoff-equivalent replay attempts were recorded for HAR and Shuttle after data provisioning; three fresh-seed/fresh-split replays were run on HAR, Shuttle, and Landsat. Replay did not reverse the main split-risk conclusions.
