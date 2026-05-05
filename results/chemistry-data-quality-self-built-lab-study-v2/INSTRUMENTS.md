# Instrument Report

Instrument: chemistry-property-record-auditor

## Purpose

Audit toy chemistry-style property records with limited identifier equivalence.

## Contract

- Inputs: curated dataset, experiment config, baseline output
- Outputs: metric summary, flags, limitations

## Calibration

Run deterministic positive, negative, boundary, and malformed safe fixture cases.

## Limitations

- Toy-scoped deterministic computational instrument.
- Not a production scientific conclusion engine.
- Requires calibration before reuse in broader settings.


# Instrument Report

Instrument: baseline-comparator

## Purpose

Compare baseline and candidate metric outputs.

## Contract

- Inputs: curated dataset, experiment config, baseline output
- Outputs: metric summary, flags, limitations

## Calibration

Run deterministic positive, negative, boundary, and malformed safe fixture cases.

## Limitations

- Toy-scoped deterministic computational instrument.
- Not a production scientific conclusion engine.
- Requires calibration before reuse in broader settings.


# Instrument Report

Instrument: replication-runner

## Purpose

Repeat deterministic experiment cases across seeds.

## Contract

- Inputs: curated dataset, experiment config, baseline output
- Outputs: metric summary, flags, limitations

## Calibration

Run deterministic positive, negative, boundary, and malformed safe fixture cases.

## Limitations

- Toy-scoped deterministic computational instrument.
- Not a production scientific conclusion engine.
- Requires calibration before reuse in broader settings.


# Instrument Report

Instrument: falsification-case-generator

## Purpose

Generate safe negative and counterexample cases.

## Contract

- Inputs: curated dataset, experiment config, baseline output
- Outputs: metric summary, flags, limitations

## Calibration

Run deterministic positive, negative, boundary, and malformed safe fixture cases.

## Limitations

- Toy-scoped deterministic computational instrument.
- Not a production scientific conclusion engine.
- Requires calibration before reuse in broader settings.
