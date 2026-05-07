# Product Implementation

Product commit: `f7edbdbcbc0936e0793d42c63a883fc6c3a9d470`.

Implemented daemon product capabilities:

- `AutonomousDiscoveryDaemonService`
- `CandidateIdentityLedger`
- `CandidateGraveyardService`
- `FundGateEvaluator`
- `SilentSearchLoopRunner`
- `SearchStateCheckpointService`
- `DeathCauseClassifier`
- `DiscoveryDomainRotator`
- `CandidateSourceRanker`
- `FreshTargetSampler`
- `DeepValidationScheduler`
- `FundNotificationPackageBuilder`

Runtime state is written under the relative artifact root `.sovryn/discovery-daemon/`. That runtime directory is intentionally ignored by Git and recreated by `discover-daemon init` or `discover-daemon status`.
