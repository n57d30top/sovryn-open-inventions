# Product Implementation

Implemented Route Policy v2 in Product. The route service now emits policyVersion, routeConfidence, matchedSignals, ambiguityScore, fallbackRoute, routeCostEstimateMinutes, evidence/package/deep-promotion thresholds, expectedFailureMode, publicPackageStatus, fallback usage, and route errors. The hard workload default now considers 400 targets and selects 160 blind targets.

Product commit: a0569a4e83ad47c4bf57f8115eb01cad24827b38.
