# Patch Risk Auditor

A safe open-source defensive method for auditing synthetic software patch-risk records.

The `patch-risk-auditor` prototype checks synthetic toy patch records for dependency
additions, install-script signals, test-impact mismatch, weak provenance, and
risky diff patterns. It provisioned or fixture-provisioned `acorn` under
policy and validated the public evidence through Node Alpha using
`container-netoff` with no silent fallback.

## Findings

- dependency_addition: Patch adds dependencies requiring provenance review.
- install_script_added: Patch adds an install-time script requiring defensive review.
- risky_diff_pattern: Patch includes dynamic evaluation pattern in synthetic sample.
- test_impact_mismatch: Code changed without matching test changes.
- weak_provenance: Patch provenance is weak or unverified.

## Safety Scope

Synthetic toy patch records only. This is defensive review support, not an
unsafe operational tool, not a real-target scanner, and not a harmful-code
generator.

## Disclaimer

This is an autonomous open-research artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion. It was published automatically after automated policy gates and still requires human interpretation before use.
