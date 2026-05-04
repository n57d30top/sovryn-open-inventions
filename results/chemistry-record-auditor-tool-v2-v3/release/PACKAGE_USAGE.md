# Package Usage

- External package: `pint`
- Purpose: Celsius/Kelvin unit normalization during the provisioning/preflight
  audit.
- Final validation: container-netoff replays the generated evidence without
  network access and verifies that the output is bound to `pint` package
  evidence.
- Scope: data-quality only; no synthesis, wet-lab guidance, drug design, or
  hazardous optimization behavior.
