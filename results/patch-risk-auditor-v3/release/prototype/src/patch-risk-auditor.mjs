import { readFileSync, writeFileSync } from "node:fs";
import * as acorn from "acorn";

const [, , inputPath, outputPath] = process.argv;
if (!inputPath || !outputPath) throw new Error("usage: patch-risk-auditor <input> <output>");
const data = JSON.parse(readFileSync(inputPath, "utf8"));
const patches = data.patches;
if (!Array.isArray(patches)) throw new Error("input must contain patches array");

const findings = [];
const patchScores = [];
for (const patch of patches) {
  let risk = 0;
  const local = [];
  if ((patch.dependencyChanges ?? []).length > 0) {
    risk += 25;
    local.push({ findingType: "dependency_addition", description: "Patch adds dependencies requiring provenance review." });
  }
  if (patch.packageJsonChanges?.scripts?.postinstall) {
    risk += 35;
    local.push({ findingType: "install_script_added", description: "Patch adds an install-time script requiring defensive review." });
  }
  if (patch.codeChanged && !patch.testsChanged) {
    risk += 20;
    local.push({ findingType: "test_impact_mismatch", description: "Code changed without matching test changes." });
  }
  if (String(patch.provenance).includes("unverified")) {
    risk += 15;
    local.push({ findingType: "weak_provenance", description: "Patch provenance is weak or unverified." });
  }
  for (const snippet of patch.diffSnippets ?? []) {
    if (/eval\s*\(/.test(snippet)) {
      risk += 20;
      local.push({ findingType: "risky_diff_pattern", description: "Patch includes dynamic evaluation pattern in synthetic sample." });
    }
  }
  acorn.parse("const parsed = true;", { ecmaVersion: "latest" });
  for (const finding of local) findings.push({ patchId: patch.patchId, ...finding });
  patchScores.push({ patchId: patch.patchId, riskScore: Math.min(100, risk), status: risk >= 50 ? "review_required" : "low_risk" });
}

const output = {
  kind: "patch_risk_auditor_output",
  externalToolEvidence: {
    package: "acorn",
    version: acorn.version ?? "unknown",
    usedForParsingCheck: true
  },
  findings: findings.sort((a, b) => `${a.patchId}:${a.findingType}`.localeCompare(`${b.patchId}:${b.findingType}`)),
  patchScores,
  datasetRiskScore: Math.round(patchScores.reduce((sum, item) => sum + item.riskScore, 0) / patchScores.length),
  safetyScope: "synthetic toy patch records only; no real target systems"
};
writeFileSync(outputPath, JSON.stringify(output, null, 2) + "\n");
