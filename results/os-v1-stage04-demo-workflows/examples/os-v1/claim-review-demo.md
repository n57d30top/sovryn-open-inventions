# Claim Review Demo

- Input: A public technical claim with source URL and bounded claim text.
- Command: `sovryn route intake --target claim-review-demo --json && sovryn route execute --target claim-review-demo --json`
- Expected package: claim decision package with evidence route, limitations, and reproduce note
- Interpretation: Use the output to decide whether the claim is supported, weakened, not testable, or needs more evidence.
- Limitations: Does not replace expert review and does not validate broad claims.
