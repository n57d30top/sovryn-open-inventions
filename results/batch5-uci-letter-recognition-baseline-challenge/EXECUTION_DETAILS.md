# Execution Details

- Execution profile: container-netoff
- Worker assurance: container-netoff
- Actual execution included: true
- Public artifact policy: aggregate metrics only

## Procedure

The preregistered task converted 26-way letter labels into a binary vowel-versus-consonant target. Training rows were used only to tune simple thresholds. The holdout run compared the best single-feature threshold baseline against a compact four-feature geometric vowel score.

## Evidence

Container-netoff benchmark over 20000 rows. Best single-feature baseline F1 0.391; compact challenger F1 0.34; challenger rejected.
