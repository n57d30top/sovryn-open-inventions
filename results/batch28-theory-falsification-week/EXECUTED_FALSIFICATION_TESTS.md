# Executed Falsification Tests

```json
[
  {
    "test": "low-risk target observed high-risk",
    "result": "not_found",
    "action": "preserve_low-risk_boundary"
  },
  {
    "test": "metric choice explains the effect",
    "result": "partial",
    "action": "narrow_metric-risk_claim"
  },
  {
    "test": "ambiguity blocks conclusion",
    "result": "found_on_vehicle",
    "action": "downgrade_ambiguous_protocol_claim"
  },
  {
    "test": "target-selection/cherry-pick explains confidence",
    "result": "partial",
    "action": "require_low-risk_controls"
  },
  {
    "test": "replay instability explains effect",
    "result": "not_primary",
    "action": "preserve_replay_scope_with_caveats"
  }
]
```
