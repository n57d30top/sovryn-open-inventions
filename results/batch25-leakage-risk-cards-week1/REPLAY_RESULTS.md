# Replay Results

| replay | target | status | finding |
| --- | --- | --- | --- |
| container-netoff-equivalent replay | UCI Statlog Shuttle | passed | Replay reused already provisioned public source files and reran deterministic source split leakage checks without download calls. |
| fresh split replay | UCI HAR Smartphones | passed | Replay preserved the Batch 25 leakage interpretation: no confirmed duplicate/group leakage mechanism was found for the executed deltas. |
