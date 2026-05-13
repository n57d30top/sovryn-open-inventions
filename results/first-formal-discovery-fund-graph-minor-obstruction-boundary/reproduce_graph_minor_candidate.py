#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'raw-reproduction-bundle' / 'formal-object-check-manifest.json').read_text())
source_cache = json.loads((ROOT / 'raw-reproduction-bundle' / 'formal-source-cache.json').read_text())
runtime = json.loads((ROOT / 'raw-reproduction-bundle' / 'runtime-evidence-output-01.json').read_text())
checks = manifest.get('checks', [])

def avg(values):
    values = list(values)
    return sum(values) / len(values) if values else 0.0

def rnd(value):
    return round(float(value), 3)

def null_trivial_score(row):
    return min(float(row.get('density', 0.0)), float(row.get('averageDegree', 0.0)) / max(float(row.get('vertices', 0.0)), 1.0))

def group_summary(field):
    groups = {}
    for row in checks:
        groups.setdefault(row.get(field, 'unknown'), []).append(row)
    return {
        str(key): {
            'count': len(rows),
            'measuredOutcome': rnd(avg(row['obstructionScore'] for row in rows)),
            'simpleBaseline': rnd(avg(row['simpleBaselineScore'] for row in rows)),
            'meanSignedResidual': rnd(avg(row['residual'] for row in rows)),
            'meanPositiveResidual': rnd(avg(max(0.0, row['residual']) for row in rows)),
            'candidateMechanismHoldRate': rnd(sum(1 for row in rows if row.get('candidateMechanismHolds')) / max(len(rows), 1)),
            'rivalExplainsRate': rnd(sum(1 for row in rows if row.get('rivalExplains')) / max(len(rows), 1)),
        }
        for key, rows in sorted(groups.items())
    }

row_metrics = {
    'checkedObjectCount': len(checks),
    'measuredOutcomeFromRows': rnd(avg(c['obstructionScore'] for c in checks)),
    'simpleBaselineFromRows': rnd(avg(c['simpleBaselineScore'] for c in checks)),
    'meanSignedResidualFromRows': rnd(avg(c['residual'] for c in checks)),
    'meanPositiveResidualFromRows': rnd(avg(max(0.0, c['residual']) for c in checks)),
    'meanAbsoluteResidualFromRows': rnd(avg(abs(c['residual']) for c in checks)),
    'matchedKnownFamilyNegativeControlFromRows': rnd(avg(c['obstructionScore'] for c in checks if not c.get('candidateMechanismHolds'))),
    'nullOrTrivialStructuralRuleFromRows': rnd(avg(null_trivial_score(c) for c in checks)),
    'candidateMechanismHoldRate': rnd(sum(1 for c in checks if c.get('candidateMechanismHolds')) / max(len(checks), 1)),
    'rivalExplainsRate': rnd(sum(1 for c in checks if c.get('rivalExplains')) / max(len(checks), 1)),
    'holdoutCount': sum(1 for c in checks if c.get('holdoutSlice') == 'holdout'),
    'developmentCount': sum(1 for c in checks if c.get('holdoutSlice') == 'development'),
    'familySummary': group_summary('graphFamily'),
    'holdoutSummary': group_summary('holdoutSlice'),
}
result = {
    'kind': 'formal_reproduction_result',
    'candidateId': 'DISCOVERY-LIFT-INSIGHT-HARD-GEN-BOUNDED-GRAPH-MINOR-OBSTRUCTION-SIGNIFI-4E76B8436316',
    'status': 'package_repair_required_before_external_review',
    'publicSafe': True,
    'manifestReplayReady': True,
    'publicFormalReproductionReady': False,
    'publicRawOrFormalReproductionReady': False,
    'countsForEinsteinNobelDiscoveryScore': False,
    'checkedObjectCount': manifest.get('checkedObjectCount'),
    'productMeasuredOutcome': source_cache.get('measuredOutcome'),
    'productResidualMagnitude': source_cache.get('residualMagnitude'),
    'productBaselineResults': source_cache.get('baselineResults'),
    'recomputedFromManifestRows': row_metrics,
    'exactProductScalarReplay': source_cache.get('measuredOutcome') == runtime.get('output', {}).get('measuredOutcome') and source_cache.get('residualMagnitude') == runtime.get('output', {}).get('residualMagnitude'),
    'measuredOutcomeRowsMatchProduct': abs(row_metrics['measuredOutcomeFromRows'] - float(source_cache.get('measuredOutcome'))) <= 0.001,
    'productResidualMagnitudeExplained': 'The Product residualMagnitude is the mean positive row residual.',
    'baselineDecision': {
        'status': 'baseline_dominated_for_public_discovery_scoring',
        'blockingBaseline': 'null_or_trivial_structural_rule',
        'blockingBaselineValue': row_metrics['nullOrTrivialStructuralRuleFromRows'],
        'measuredOutcome': row_metrics['measuredOutcomeFromRows'],
        'reason': 'The null/trivial structural-rule baseline is directionally comparable and exceeds the measured outcome under the public audit.',
    },
    'independentSourceReplayStatus': 'failed_manifest_only_replay_available',
    'knownTrivialityDecision': 'baseline_dominated_likely_known_needs_human_review',
    'noExternalValidationClaim': True,
    'noNobelClaim': True,
    'noEinsteinLevelClaim': True,
}
(ROOT / 'FORMAL_REPRODUCTION_RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
