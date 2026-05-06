# Batch 6 Reproduction Ladder Report

Week 2 / Batch 6 executed the strict Reproduction Ladder instead of adding a framework layer. Three public-safe external targets were selected, installed or provisioned as needed, executed, and packaged as public corpus results.

## Results

- batch6-scikit-learn-iris-reproduction-ladder: Level 8; The package install and example-scale classifier path are reproducible in this environment, but this is not a full repository reproduction because upstream tests were not run.
- batch6-uci-concrete-baseline-reproduction-ladder: Level 8; On this exact split, a simple random forest substantially outperformed dummy baselines, while the data-quality pass found 25 duplicate full rows and no missing cells.
- batch6-diamonds-data-quality-netoff-ladder: Level 9; The public CSV loads cleanly with no missing cells, but the audit found duplicate rows and physically suspicious zero-dimension records, making this a negative data-quality result that future examples should filter or document.

## Requirement summary

- 3 new public corpus results: yes.
- All 3 include real execution attempt evidence: yes.
- At least 2 executed code or loaded real public data: yes, all 3.
- At least 2 installed or provisioned external dependencies/tools/packages: yes.
- At least 1 used container-netoff or equivalent isolated execution: yes, diamonds audit used a network-denied sandbox-exec replay after Docker container-netoff was unavailable.
- At least 1 negative, failed, or partial reproduction: yes, scikit-learn is partial and diamonds is a negative data-quality finding.
- At least 1 baseline-vs-challenger comparison: yes, UCI Concrete.
- At least 1 independent replay/fresh workspace attempt: yes, diamonds network-off replay.

## Core question

Every result answers: what did Sovryn actually execute, and what do we know now that we did not know before?
