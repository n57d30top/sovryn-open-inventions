# UCI Concrete Strength Baseline Reproduction Ladder

Sovryn provisioned ucimlrepo, pandas and scikit-learn, loaded the UCI Concrete Compressive Strength dataset, executed an 80/20 regression baseline comparison, and found that RandomForestRegressor beat mean and median dummy baselines on the selected split.

## What was executed

Fetched UCI dataset id 165 through ucimlrepo, checked basic schema quality, split 1030 rows into train and test partitions, and ran mean, median, and RandomForestRegressor models.

## What Sovryn learned

On this exact split, a simple random forest substantially outperformed dummy baselines, while the data-quality pass found 25 duplicate full rows and no missing cells.

## Ladder status

Highest reproduction ladder level reached: **Level 8**.

## Public sources

| Source | URL | Role |
| --- | --- | --- |
| UCI Concrete Compressive Strength dataset | https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength | Public UCI dataset with 1030 rows, eight features and concrete compressive strength target. |

## Status

- Result label: `baseline_comparison_executed`
- Negative or partial result: `false`
- Publication safety: public, computational, non-sensitive data only

## Disclaimer

Sovryn produces autonomous open-research artifacts, defensive publications, and open-source research evidence. It is not a patent filing system and does not provide legal patentability, legal novelty, or freedom-to-operate opinions.
