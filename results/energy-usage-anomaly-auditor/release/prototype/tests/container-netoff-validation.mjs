import { readFileSync } from "node:fs";

const output = JSON.parse(readFileSync("sample-output.json", "utf8"));
const lock = JSON.parse(readFileSync("package-lock-summary.json", "utf8"));

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

assert(output.externalToolEvidence.package === "pandas", "pandas evidence missing");
assert(output.externalToolEvidence.usedForTabularValidation === true, "pandas usage not recorded");
assert(lock.packages.some((item) => item.name === "pandas"), "package lock missing pandas");
assert(output.datasetIssues.some((item) => item.issueType === "duplicate_timestamp"), "duplicate timestamp missing");
assert(output.datasetIssues.some((item) => item.issueType === "missing_interval"), "missing interval missing");
assert(output.datasetIssues.some((item) => item.issueType === "high_usage_spike"), "high usage spike missing");
assert(output.datasetIssues.some((item) => item.issueType === "weather_normalized_anomaly"), "weather anomaly missing");
assert(output.datasetIssues.some((item) => item.issueType === "weak_provenance"), "weak provenance missing");
