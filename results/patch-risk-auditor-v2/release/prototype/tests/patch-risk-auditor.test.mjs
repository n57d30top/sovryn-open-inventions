import { readFileSync } from "node:fs";
import { spawnSync } from "node:child_process";

const run = spawnSync(process.execPath, ["src/patch-risk-auditor.mjs", "sample-input.json", "sample-output.json"], { encoding: "utf8" });
if (run.status !== 0) throw new Error(run.stderr || "auditor failed");
const output = JSON.parse(readFileSync("sample-output.json", "utf8"));

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

assert(output.externalToolEvidence.package === "acorn", "acorn evidence missing");
assert(output.externalToolEvidence.usedForParsingCheck === true, "acorn parse check missing");
assert(output.findings.some((item) => item.findingType === "dependency_addition"), "dependency addition missing");
assert(output.findings.some((item) => item.findingType === "install_script_added"), "install script missing");
assert(output.findings.some((item) => item.findingType === "test_impact_mismatch"), "test impact mismatch missing");
assert(output.findings.some((item) => item.findingType === "weak_provenance"), "weak provenance missing");
assert(output.findings.some((item) => item.findingType === "risky_diff_pattern"), "risky diff pattern missing");
assert(output.patchScores.some((item) => item.patchId === "benign-docs-update" && item.status === "low_risk"), "benign patch not low risk");
assert(output.patchScores.some((item) => item.patchId === "risky-ai-generated-dependency" && item.status === "review_required"), "risky patch not flagged");
