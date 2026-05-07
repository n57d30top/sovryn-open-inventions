# CLI Smoke Results

Verified:

- node dist/cli.js --help lists sovryn route commands.
- sovryn route status --json returns route_policy_v2 and hard_external_workload.
- sovryn route audit --json passes with 400 considered, 160 selected, 160 routed, 743 real evidence checks, 65 install/provision/execution attempts, 43 quick reject/not-testable/unsafe outcomes, and 60 public packages.
