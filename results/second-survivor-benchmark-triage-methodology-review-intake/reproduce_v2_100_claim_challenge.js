#!/usr/bin/env node
const { existsSync, readFileSync, writeFileSync } = require("fs");
const { basename, join } = require("path");

const candidateId = "DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001";
const cwd = __dirname;

const inputFiles = {
  benchmark: "V2_SURVIVOR_YIELD_BENCHMARK.json",
  v2DeepValidation: "V2_DEEP_VALIDATION_RESULTS.md",
  baselineOnlyDeepValidation: "BASELINE_ONLY_DEEP_VALIDATION_RESULTS.md",
  baselineOnlyComparison: "V2_BASELINE_ONLY_COMPARISON.md",
};

function requireFile(file) {
  const path = join(cwd, file);
  if (!existsSync(path))
    throw new Error(`Missing required public input: ${file}`);
  return readFileSync(path, "utf8");
}

function round(value) {
  return Math.round(value * 1000) / 1000;
}

function parseMarkdownTable(markdown) {
  const rows = [];
  for (const line of markdown.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed.startsWith("|")) continue;
    if (/^\|\s*-+/.test(trimmed)) continue;
    const cells = trimmed
      .slice(1, -1)
      .split("|")
      .map((cell) => cell.trim());
    if (cells[0] === "Claim") {
      rows.header = cells;
      continue;
    }
    if (!rows.header || cells.length !== rows.header.length) continue;
    const record = {};
    rows.header.forEach((header, index) => {
      record[header] = cells[index];
    });
    rows.push(record);
  }
  return rows;
}

function number(value) {
  const parsed = Number(String(value).replace(/,/g, ""));
  if (!Number.isFinite(parsed))
    throw new Error(`Expected numeric value, got ${value}`);
  return parsed;
}

function claimIds(rows) {
  return rows.map((row) => row.Claim);
}

function computeYield(rows) {
  const survivors = rows.filter((row) => row.Outcome === "survived");
  return {
    selectedPlausibleClaims: rows.length,
    survivors: survivors.length,
    survivorYield:
      rows.length === 0 ? 0 : round(survivors.length / rows.length),
    selectedClaimIds: claimIds(rows),
    survivorClaimIds: claimIds(survivors),
  };
}

function assert(condition, message, failures) {
  if (!condition) failures.push(message);
}

function main() {
  const failures = [];
  const benchmark = JSON.parse(requireFile(inputFiles.benchmark));
  const v2Rows = parseMarkdownTable(requireFile(inputFiles.v2DeepValidation));
  const baselineRows = parseMarkdownTable(
    requireFile(inputFiles.baselineOnlyDeepValidation),
  );
  const comparisonRows = parseMarkdownTable(
    requireFile(inputFiles.baselineOnlyComparison),
  );

  const publicReceiptRows = benchmark.filter(
    (claim) =>
      typeof claim.sourceObjectReceipt === "string" &&
      /^https:\/\/www\.openml\.org\//.test(claim.sourceObjectReceipt) &&
      typeof claim.rawDataReceiptHash === "string" &&
      /^[a-f0-9]{64}$/.test(claim.rawDataReceiptHash),
  );
  const independentTasks = new Set(benchmark.map((claim) => claim.taskId)).size;
  const plausibleClaims = benchmark.filter(
    (claim) => claim.claimClass === "plausible_non_control",
  );
  const weakClaims = benchmark.filter((claim) => claim.claimClass === "weak");
  const positiveControls = benchmark.filter(
    (claim) => claim.claimClass === "positive_control",
  );
  const manifestRows = benchmark.filter(
    (claim) =>
      claim.groupTimeEntityManifest &&
      claim.groupTimeEntityManifest.realPublicFieldManifest === true,
  );

  const v2 = computeYield(v2Rows);
  const baselineOnly = computeYield(baselineRows);
  const v2Selected = new Set(v2.selectedClaimIds);
  const baselineOnlyFalseAdvanceRows = baselineRows.filter(
    (row) => !v2Selected.has(row.Claim) && row.Outcome !== "survived",
  );
  const baselineOnlyFalseAdvanceClaimIds = claimIds(
    baselineOnlyFalseAdvanceRows,
  );
  const v2GroupTimeEntitySurvivors = v2Rows.filter(
    (row) => row.Manifest === "complete" && row.Outcome === "survived",
  ).length;
  const baselineOnlyGroupTimeEntitySurvivors = baselineRows.filter(
    (row) => row.Manifest === "complete" && row.Outcome === "survived",
  ).length;
  const replayRows = [...v2Rows, ...baselineRows];
  const replayPassedRows = replayRows.filter(
    (row) => row.Replay === "replay_passed",
  );

  assert(
    benchmark.length === 100,
    "benchmark does not contain 100 claims",
    failures,
  );
  assert(independentTasks >= 25, "independent task count below 25", failures);
  assert(
    plausibleClaims.length >= 30,
    "plausible non-control count below 30",
    failures,
  );
  assert(weakClaims.length >= 30, "weak claim count below 30", failures);
  assert(
    positiveControls.length >= 10,
    "positive control count below 10",
    failures,
  );
  assert(
    manifestRows.length >= 20,
    "manifest-backed claim count below 20",
    failures,
  );
  assert(
    publicReceiptRows.length === 100,
    "not all claims have public OpenML receipt hashes",
    failures,
  );
  assert(
    v2.selectedPlausibleClaims === 17,
    "V2 selected count mismatch",
    failures,
  );
  assert(v2.survivors === 17, "V2 survivor count mismatch", failures);
  assert(v2.survivorYield === 1, "V2 survivor yield mismatch", failures);
  assert(
    baselineOnly.selectedPlausibleClaims === 25,
    "baseline-only selected count mismatch",
    failures,
  );
  assert(
    baselineOnly.survivors === 17,
    "baseline-only survivor count mismatch",
    failures,
  );
  assert(
    baselineOnly.survivorYield === 0.68,
    "baseline-only yield mismatch",
    failures,
  );
  assert(
    baselineOnlyFalseAdvanceRows.length === 8,
    "baseline-only false-advance count mismatch",
    failures,
  );
  assert(
    replayPassedRows.length === replayRows.length,
    "selected deep-validation rows do not all report replay_passed",
    failures,
  );
  assert(
    comparisonRows.length === 25,
    "baseline-only comparison table should expose 25 selected plausible rows",
    failures,
  );

  const result = {
    kind: "v2_100_claim_standalone_reproduction",
    candidateId,
    status: failures.length === 0 ? "reproduced" : "failed",
    inputs: Object.values(inputFiles).map((file) => basename(file)),
    requiresProductSovrynState: false,
    requiresSecrets: false,
    usesPrivatePaths: false,
    benchmarkSize: benchmark.length,
    independentTasks,
    plausibleNonControlClaims: plausibleClaims.length,
    weakClaims: weakClaims.length,
    positiveControls: positiveControls.length,
    publicReceiptRows: publicReceiptRows.length,
    publicReplayStatusReported:
      "100/100 benchmark rows carry public OpenML receipts; all selected deep-validation rows report replay_passed.",
    groupTimeEntityManifestRows: manifestRows.length,
    groupTimeEntityManifestWording:
      "public-field deterministic split manifests, not official dataset-author protocols unless separately documented",
    v2,
    baselineOnly: {
      ...baselineOnly,
      falseAdvancesFilteredByV2: baselineOnlyFalseAdvanceRows.length,
      falseAdvanceClaimIds: baselineOnlyFalseAdvanceClaimIds,
    },
    v2BeatsBaselineOnlyOnSurvivorYield:
      v2.survivorYield > baselineOnly.survivorYield,
    v2GroupTimeEntitySurvivors,
    baselineOnlyGroupTimeEntitySurvivors,
    discoveryScored: false,
    fundFound: false,
    notificationAllowed: false,
    noOverclaim:
      "This reproduces the public 100-claim package arithmetic only. It is not external validation, not discovery-scored, and not FUND_FOUND.",
    failures,
  };

  writeFileSync(
    join(cwd, "v2_100_claim_reproducer_result.json"),
    `${JSON.stringify(result, null, 2)}\n`,
  );
  console.log(JSON.stringify(result, null, 2));
  if (failures.length > 0) process.exitCode = 1;
}

try {
  main();
} catch (error) {
  console.error(error instanceof Error ? error.stack : String(error));
  process.exitCode = 1;
}
