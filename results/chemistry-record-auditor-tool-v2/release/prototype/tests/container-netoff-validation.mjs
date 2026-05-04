import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const output = JSON.parse(readFileSync("sample-output.json", "utf8"));
const lock = JSON.parse(readFileSync("package-lock-summary.json", "utf8"));

assert.equal(output.externalToolEvidence.package, "pint");
assert.equal(output.externalToolEvidence.usedForUnitNormalization, true);
assert.equal(lock.packages[0].name, "pint");
assert.equal(lock.sudoUsed, false);
assert.equal(lock.curlPipeShellUsed, false);
assert.equal(output.datasetReliabilityScore < 100, true);
assert.equal(
  output.datasetIssues.some(
    (item) =>
      item.compound === "acetone" &&
      item.issueType === "suspicious_property_outlier",
  ),
  true,
);
assert.equal(
  output.compounds.some(
    (item) =>
      item.compound === "water" &&
      item.consistentAfterUnitNormalization === true,
  ),
  true,
);
