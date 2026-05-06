# Repo Test Summary Attacks

Tool attacked: `pytest_repro_summary`.

Prior evidence:

- Batch 7 Pluggy: AST and grep found 107 static test definitions, while pytest execution reported 126 runtime passing cases.
- Batch 8 iniconfig: AST and grep found 31 static tests, runtime reported 49 passing cases.
- Batch 8 pyproject-hooks: AST and grep found 32 static tests, runtime produced 6 collection/runtime errors in the minimal environment.

Attack:

- Static inventory is not runtime reproduction.
- Dynamic parametrization makes static counts lower than runtime case counts.
- Dependency readiness can dominate the test result.
- A public-safe summary is useful, but it cannot certify a repo has been reproduced.

Decision:

`pytest_repro_summary` remains `narrow_but_useful_support_only`.

Future use:

Use it to package static inventory, runtime count, return code, and dependency-failure notes. Do not use it as a standalone reproduction claim.
