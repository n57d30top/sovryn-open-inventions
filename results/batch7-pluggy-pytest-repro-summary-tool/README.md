# Batch 7 Pluggy Pytest Reproduction Summary Tool

## What concrete task was blocked?

pytest-dev/pluggy repository test suite

Existing generic tools were tried first, but they did not produce the exact public-safe evidence needed for this Batch 7 target.

## What Sovryn built

Sovryn built `pytest_repro_summary` as the smallest useful custom instrument for this target.

## Did it work?

The repository test run returned code 0 with 126 passing runtime cases. AST and grep agreed on static definitions, while runtime cases were higher due to test expansion.

Tool status: `used_successfully_limited`.

Tool decision: `keep_but_mark_dynamic_parametrization_limit`.

## What Sovryn learned

The summarizer can create a public-safe reconciliation between static inventory and execution counts, but it must be marked limited because dynamic parametrization means static definitions do not equal runtime cases.

## Safety and publication scope

Safe computational research only. No private data, no harmful domain content, no benchmark-win or breakthrough claim, and no legal patentability/FTO claim.
