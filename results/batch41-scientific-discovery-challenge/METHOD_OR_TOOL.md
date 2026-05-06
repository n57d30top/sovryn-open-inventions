# Method or Tool

A small result-local risk scoring function was built for this challenge only. It is not promoted as a product feature.

Positive test: HAR should score above a low-risk control because random splitting mixes subject IDs.

Negative test: sklearn digits should remain low risk.

Example output: HAR high/moderate-risk candidate; digits low-risk control.
