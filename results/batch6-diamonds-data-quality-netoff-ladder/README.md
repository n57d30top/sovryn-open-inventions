# seaborn-data Diamonds Network-Off Quality Reproduction Ladder

Sovryn downloaded the public seaborn-data diamonds CSV, then replayed the audit under a container-netoff-equivalent sandbox-exec profile with network access denied. The audit confirmed duplicate rows and nonpositive dimension values, so the result is a useful negative data-quality finding rather than a clean-data claim.

## What was executed

Loaded 53940 CSV rows with pandas in a network-off sandbox and checked missing cells, duplicate rows, nonpositive numeric values, empty categorical values, positive carat with nonpositive dimensions, and upper-tail price count.

## What Sovryn learned

The public CSV loads cleanly with no missing cells, but the audit found duplicate rows and physically suspicious zero-dimension records, making this a negative data-quality result that future examples should filter or document.

## Ladder status

Highest reproduction ladder level reached: **Level 9**.

## Public sources

| Source | URL | Role |
| --- | --- | --- |
| seaborn-data repository | https://github.com/mwaskom/seaborn-data | Public repository containing example datasets used by the seaborn ecosystem. |
| diamonds.csv | https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv | Public CSV audited for schema and value quality. |

## Status

- Result label: `data_quality_issues_confirmed_under_network_off_replay`
- Negative or partial result: `true`
- Publication safety: public, computational, non-sensitive data only

## Disclaimer

Sovryn produces autonomous open-research artifacts, defensive publications, and open-source research evidence. It is not a patent filing system and does not provide legal patentability, legal novelty, or freedom-to-operate opinions.
