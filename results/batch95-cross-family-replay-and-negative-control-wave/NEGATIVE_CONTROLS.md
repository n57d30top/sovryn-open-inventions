# Negative Controls

| target | controlType | observedMetric | decisionEffect |
| --- | --- | --- | --- |
| iris | shuffled_label | 0.3852 | weakens benchmark claim if near real metric; otherwise supports baseline sanity only |
| wine | shuffled_label | 0.3167 | weakens benchmark claim if near real metric; otherwise supports baseline sanity only |
| breast_cancer | shuffled_label | 0.4534 | weakens benchmark claim if near real metric; otherwise supports baseline sanity only |
| digits | shuffled_label | 0.0998 | weakens benchmark claim if near real metric; otherwise supports baseline sanity only |
| sunspots.SUNACTIVITY | shuffled_time | 30.5738 | temporal claim is weakened if shuffled-time behaves like temporal model |
| co2.co2 | shuffled_time | 14.6884 | temporal claim is weakened if shuffled-time behaves like temporal model |
| macrodata.realgdp | shuffled_time | 2556.8875 | temporal claim is weakened if shuffled-time behaves like temporal model |
| macrodata.realcons | shuffled_time | 1836.6903 | temporal claim is weakened if shuffled-time behaves like temporal model |
