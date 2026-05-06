# Batch 7 Wine Quality Schema Provenance Tool

## What concrete task was blocked?

UCI Wine Quality red and white CSV datasets

Existing generic tools were tried first, but they did not produce the exact public-safe evidence needed for this Batch 7 target.

## What Sovryn built

Sovryn built `schema_provenance_auditor` as the smallest useful custom instrument for this target.

## Did it work?

The tool audited 6497 rows across two files, found schema_match=true, missing_cells=0, and duplicate_full_rows=1177.

Tool status: `used_successfully`.

Tool decision: `keep_as_reusable_candidate`.

## What Sovryn learned

The red and white Wine Quality files share the expected 12-column schema and have no missing cells, but they contain 1177 duplicate full rows across the combined public files. That makes this a useful negative data-quality finding for downstream benchmark use.

## Safety and publication scope

Safe computational research only. No private data, no harmful domain content, no benchmark-win or breakthrough claim, and no legal patentability/FTO claim.
