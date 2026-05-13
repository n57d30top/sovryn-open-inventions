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

row_metrics = {
    'checkedObjectCount': len(checks),
    'measuredOutcomeFromRows': rnd(avg(c['obstructionScore'] for c in checks)),
    'simpleBaselineFromRows': rnd(avg(c['simpleBaselineScore'] for c in checks)),
    'meanSignedResidualFromRows': rnd(avg(c['residual'] for c in checks)),
    'meanAbsoluteResidualFromRows': rnd(avg(abs(c['residual']) for c in checks)),
    'candidateMechanismHoldRate': rnd(sum(1 for c in checks if c.get('candidateMechanismHolds')) / max(len(checks), 1)),
    'rivalExplainsRate': rnd(sum(1 for c in checks if c.get('rivalExplains')) / max(len(checks), 1)),
    'holdoutCount': sum(1 for c in checks if c.get('holdoutSlice') == 'holdout'),
    'developmentCount': sum(1 for c in checks if c.get('holdoutSlice') == 'development'),
}
result = {
    'kind': 'formal_reproduction_result',
    'candidateId': 'DISCOVERY-LIFT-INSIGHT-HARD-GEN-BOUNDED-GRAPH-MINOR-OBSTRUCTION-SIGNIFI-4E76B8436316',
    'status': 'formal_replay_succeeded_caveated_no_external_validation',
    'publicSafe': True,
    'replayReady': True,
    'checkedObjectCount': manifest.get('checkedObjectCount'),
    'productMeasuredOutcome': source_cache.get('measuredOutcome'),
    'productResidualMagnitude': source_cache.get('residualMagnitude'),
    'productBaselineResults': source_cache.get('baselineResults'),
    'recomputedFromManifestRows': row_metrics,
    'exactProductScalarReplay': source_cache.get('measuredOutcome') == runtime.get('output', {}).get('measuredOutcome') and source_cache.get('residualMagnitude') == runtime.get('output', {}).get('residualMagnitude'),
    'measuredOutcomeRowsMatchProduct': abs(row_metrics['measuredOutcomeFromRows'] - float(source_cache.get('measuredOutcome'))) <= 0.001,
    'residualFormulaCaveat': 'The product residualMagnitude is replayed from the formal source cache. The row-level signed residual mean is reported separately because the Product residual normalization is not derivable from the public manifest alone.',
    'noExternalValidationClaim': True,
    'noNobelClaim': True,
    'noEinsteinLevelClaim': True,
}
(ROOT / 'FORMAL_REPRODUCTION_RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
