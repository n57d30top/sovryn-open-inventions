# Replay Readiness

| target | can replay now | needs data-loader fix | needs protocol clarification | needs deep study | decision |
| --- | --- | --- | --- | --- | --- |
| UCI HAR Smartphones | yes | no | no | no | execute_now |
| UCI Statlog Shuttle | yes | no | no | no | execute_now |
| UCI Statlog Landsat Satellite | yes | no | no | yes | hold_for_deep_study |
| UCI Optical Digits | yes | no | no | yes | hold_for_deep_study |
| UCI Pen-Based Digits | yes | no | no | yes | hold_for_deep_study |
| UCI Letter Recognition | yes | no | no | no | low_risk_control |
| UCI Image Segmentation | yes | no | no | yes | hold_for_deep_study |
| UCI Vehicle Silhouettes | partial | no | yes | yes | ambiguous_needs_deep_study |
| UCI Waveform Database Generator | defer | yes | yes | no | defer |
| scikit-learn bundled digits control | partial | no | yes | no | low_risk_control |

Executed replay: fresh-seed replay on HAR changed random challenger macro-F1 within the same moderate-risk conclusion. Container-netoff-equivalent replay was attempted after public data provisioning and passed as a deterministic replay phase.
