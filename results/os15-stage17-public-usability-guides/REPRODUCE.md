# Reproduce

Run the Product smoke checks against the OS v1.5 artifacts:

- `sovryn os final-audit --json`
- `sovryn route policy-v4-audit --json`
- `sovryn corpus search-index audit --json`
- `sovryn corpus package-index verify --json`

Then inspect the stage artifacts in this result directory.
