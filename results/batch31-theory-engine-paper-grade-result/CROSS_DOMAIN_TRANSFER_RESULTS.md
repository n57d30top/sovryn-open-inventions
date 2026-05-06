# Cross-Domain Transfer Results

```json
[
  {
    "domain": "repo/test reproduction with runtime evidence",
    "mapping": "Changing test collection/runtime protocol can change reproduction claims.",
    "prediction": "Runtime protocol evidence should weaken static-only repo/test claims.",
    "executed": true,
    "result": "partial_success",
    "summary": "Repo/test transfer check. Exit code 0; duration 57 ms; command streams are omitted from public release."
  },
  {
    "domain": "scientific dataset reliability",
    "mapping": "Changing cleaning/split protocol can change reliability conclusions.",
    "prediction": "Protocol-aware reliability evidence should narrow simple schema claims.",
    "executed": true,
    "result": "partial_success",
    "summary": "Dataset reliability transfer check. Exit code 0; duration 50 ms; command streams are omitted from public release."
  },
  {
    "domain": "time-series anomaly benchmark",
    "mapping": "Temporal split protocol may change anomaly score conclusions.",
    "prediction": "Evaluation Fragility may transfer, but only after temporal controls exist.",
    "executed": false,
    "result": "not_testable_in_this_trial",
    "summary": "Transfer remains partial because no new public time-series protocol execution was run."
  }
]
```
