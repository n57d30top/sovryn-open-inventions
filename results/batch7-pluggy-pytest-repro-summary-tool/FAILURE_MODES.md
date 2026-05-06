# Failure Modes

- Dynamic parametrization and fixture expansion make runtime case counts larger than static definitions.
- The tool intentionally stores only curated counts, not execution transcripts.

False-positive/false-negative analysis: AST-vs-grep agreement prevents one simple static counting false positive, but it does not eliminate runtime expansion differences.
