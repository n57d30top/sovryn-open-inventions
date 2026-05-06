# Replay Results

| Target | Replay type | Primary macro-F1 | Replay macro-F1 | Delta |
| --- | --- | --- | --- | --- |
| rice-cammeo-osmancik | fresh_seed_split | 0.9174 | 0.9223 | 0.0049 |
| optical-handwritten-digits | fresh_seed_split | 0.9704 | 0.9675 | -0.0029 |

| Target | Replay type | Schema tool | Metric tool | Logistic macro-F1 |
| --- | --- | --- | --- | --- |
| rice-cammeo-osmancik | container_netoff | true | true | 0.9268 |
| optical-handwritten-digits | container_netoff | true | true | 0.9745 |

The container replay used network mode `none`.
