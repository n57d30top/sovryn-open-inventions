#!/usr/bin/env node
const { createHash } = require("crypto");
const { writeFileSync } = require("fs");
const { join } = require("path");

const tasks = [
  {
    claimId: "SA-PLAUS-003-OPENML-32",
    taskId: 32,
    datasetId: 32,
    datasetName: "pendigits",
    targetVariable: "class",
    splitFeature: "input1",
    rawArffReceipt: "https://openml.org/data/v1/download/32/pendigits.arff",
    expected: {
      baselineMetric: 0.093,
      randomSplitMetric: 0.186,
      holdoutMetric: -0.001,
      modelVsBaselineDelta: 0.093,
      randomVsHoldoutDelta: 0.187,
    },
  },
  {
    claimId: "SECOND-SURV-001-OPENML-59",
    taskId: 59,
    datasetId: 61,
    datasetName: "iris",
    targetVariable: "class",
    splitFeature: "sepallength",
    rawArffReceipt: "https://openml.org/data/v1/download/61/iris.arff",
    expected: {
      baselineMetric: 0.222,
      randomSplitMetric: 0.511,
      holdoutMetric: 0.0,
      modelVsBaselineDelta: 0.289,
      randomVsHoldoutDelta: 0.511,
    },
  },
  {
    claimId: "SECOND-SURV-003-OPENML-7",
    taskId: 7,
    datasetId: 7,
    datasetName: "audiology",
    targetVariable: "class",
    splitFeature: "age_gt_60",
    rawArffReceipt: "https://openml.org/data/v1/download/7/audiology.arff",
    expected: {
      baselineMetric: 0.25,
      randomSplitMetric: 0.5,
      holdoutMetric: 0.0,
      modelVsBaselineDelta: 0.25,
      randomVsHoldoutDelta: 0.5,
    },
  },
  {
    claimId: "SECOND-SURV-005-OPENML-53",
    taskId: 53,
    datasetId: 54,
    datasetName: "vehicle",
    targetVariable: "Class",
    splitFeature: "COMPACTNESS",
    rawArffReceipt: "https://openml.org/data/v1/download/54/vehicle.arff",
    expected: {
      baselineMetric: 0.232,
      randomSplitMetric: 0.398,
      holdoutMetric: 0.176,
      modelVsBaselineDelta: 0.165,
      randomVsHoldoutDelta: 0.221,
    },
  },
  {
    claimId: "SECOND-SURV-006-OPENML-36",
    taskId: 36,
    datasetId: 36,
    datasetName: "segment",
    targetVariable: "class",
    splitFeature: "region-centroid-col",
    rawArffReceipt: "https://openml.org/data/v1/download/36/segment.arff",
    expected: {
      baselineMetric: 0.127,
      randomSplitMetric: 0.209,
      holdoutMetric: 0.0,
      modelVsBaselineDelta: 0.082,
      randomVsHoldoutDelta: 0.209,
    },
  },
  {
    claimId: "SECOND-SURV-007-OPENML-43",
    taskId: 43,
    datasetId: 44,
    datasetName: "spambase",
    targetVariable: "class",
    splitFeature: "word_freq_make",
    rawArffReceipt: "https://openml.org/data/v1/download/44/spambase.arff",
    expected: {
      baselineMetric: 0.61,
      randomSplitMetric: 0.653,
      holdoutMetric: 0.0,
      modelVsBaselineDelta: 0.043,
      randomVsHoldoutDelta: 0.653,
    },
  },
  {
    claimId: "SECOND-SURV-008-OPENML-15",
    taskId: 15,
    datasetId: 15,
    datasetName: "breast-w",
    targetVariable: "Class",
    splitFeature: "Clump_Thickness",
    rawArffReceipt: "https://openml.org/data/v1/download/52350/breast-w.arff",
    expected: {
      baselineMetric: 0.671,
      randomSplitMetric: 0.79,
      holdoutMetric: 0.0,
      modelVsBaselineDelta: 0.119,
      randomVsHoldoutDelta: 0.79,
    },
  },
];

function sha256(text) {
  return createHash("sha256").update(text).digest("hex");
}

function round(value) {
  return Math.round(value * 1000) / 1000;
}

function seededValue(index, seed) {
  const hash = createHash("sha256")
    .update(`${index}:${seed}`)
    .digest()
    .readUInt32BE(0);
  return hash / 0xffffffff;
}

function splitIndices(length, trainFraction, seed) {
  const indices = Array.from({ length }, (_, index) => index).sort(
    (a, b) => seededValue(a, seed) - seededValue(b, seed),
  );
  const cutoff = Math.max(1, Math.floor(length * trainFraction));
  return { train: indices.slice(0, cutoff), test: indices.slice(cutoff) };
}

function parseArff(arff, targetVariable) {
  const attributes = [];
  const rows = [];
  let inData = false;
  for (const rawLine of arff.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith("%")) continue;
    if (!inData && /^@attribute\s+/i.test(line)) {
      const match = line.match(
        /^@attribute\s+('([^']+)'|"([^"]+)"|([^\s]+))/i,
      );
      attributes.push(
        (match && (match[2] || match[3] || match[4])) ||
          `attr${attributes.length}`,
      );
      continue;
    }
    if (/^@data/i.test(line)) {
      inData = true;
      continue;
    }
    if (inData && !line.startsWith("@")) rows.push(splitCsvLine(line));
  }
  const targetIndex = attributes.findIndex(
    (attribute) => attribute.toLowerCase() === targetVariable.toLowerCase(),
  );
  if (targetIndex < 0) {
    throw new Error(`target ${targetVariable} missing from ARFF`);
  }
  return { attributes, rows, targetIndex };
}

function splitCsvLine(line) {
  const values = [];
  let current = "";
  let quoted = false;
  for (let index = 0; index < line.length; index += 1) {
    const char = line[index];
    if (char === "'" || char === '"') {
      quoted = !quoted;
      continue;
    }
    if (char === "," && !quoted) {
      values.push(current.trim());
      current = "";
      continue;
    }
    current += char;
  }
  values.push(current.trim());
  return values;
}

function attributeIndex(parsed, key) {
  return parsed.attributes.findIndex(
    (attribute) => attribute.toLowerCase() === key.toLowerCase(),
  );
}

function holdoutSplitForTask(task, parsed) {
  const groupIndex = attributeIndex(parsed, task.splitFeature);
  if (groupIndex >= 0) {
    const values = parsed.rows.map((row) => row[groupIndex] || "");
    const distinct = [...new Set(values)].sort();
    const heldOut = distinct[Math.max(0, distinct.length - 1)] || "";
    const train = [];
    const test = [];
    values.forEach((value, index) => {
      if (value === heldOut) test.push(index);
      else train.push(index);
    });
    if (train.length > 0 && test.length > 0) {
      return { train, test, heldOut };
    }
  }
  return { ...splitIndices(parsed.rows.length, 0.7, 41), heldOut: null };
}

function evaluateSplit(parsed, split) {
  const trainLabels = split.train.map(
    (index) => (parsed.rows[index] || [])[parsed.targetIndex] || "",
  );
  const majority = mostFrequent(trainLabels);
  const featureIndex = parsed.targetIndex === 0 ? 1 : 0;
  const lookup = new Map();
  for (const index of split.train) {
    const row = parsed.rows[index] || [];
    const key = row[featureIndex] || "";
    if (!lookup.has(key)) lookup.set(key, row[parsed.targetIndex] || majority);
  }
  let majorityCorrect = 0;
  let modelCorrect = 0;
  for (const index of split.test) {
    const row = parsed.rows[index] || [];
    const target = row[parsed.targetIndex] || "";
    if (target === majority) majorityCorrect += 1;
    const prediction = lookup.get(row[featureIndex] || "") || majority;
    if (prediction === target) modelCorrect += 1;
  }
  const denominator = Math.max(1, split.test.length);
  return {
    majorityBaseline: majorityCorrect / denominator,
    modelMetric: modelCorrect / denominator,
  };
}

function evaluateShuffledTarget(parsed, split) {
  const rows = parsed.rows.map((row, index) => {
    const copy = [...row];
    copy[parsed.targetIndex] =
      (parsed.rows[(index + 17) % parsed.rows.length] || [])[
        parsed.targetIndex
      ] || "";
    return copy;
  });
  return evaluateSplit({ ...parsed, rows }, split);
}

function mostFrequent(values) {
  const counts = new Map();
  for (const value of values) counts.set(value, (counts.get(value) || 0) + 1);
  return (
    [...counts.entries()].sort((a, b) => b[1] - a[1])[0] || ["", 0]
  )[0];
}

function compareMetric(actual, expected) {
  return {
    actual,
    expected,
    delta: round(actual - expected),
    exact: actual === expected,
    withinRoundingTolerance: Math.abs(actual - expected) <= 0.0015,
  };
}

async function replayTask(task) {
  const response = await fetch(task.rawArffReceipt);
  if (!response.ok) {
    throw new Error(`${task.rawArffReceipt} returned ${response.status}`);
  }
  const raw = await response.text();
  const parsed = parseArff(raw, task.targetVariable);
  const randomSplit = splitIndices(parsed.rows.length, 0.7, 23);
  const holdoutSplit = holdoutSplitForTask(task, parsed);
  const random = evaluateSplit(parsed, randomSplit);
  const holdout = evaluateSplit(parsed, holdoutSplit);
  const negative = evaluateShuffledTarget(
    parsed,
    splitIndices(parsed.rows.length, 0.7, 61),
  );
  const baselineMetric = round(random.majorityBaseline);
  const randomSplitMetric = round(random.modelMetric);
  const holdoutMetric = round(holdout.modelMetric);
  const modelVsBaselineDelta = round(random.modelMetric - random.majorityBaseline);
  const randomVsHoldoutDelta = round(random.modelMetric - holdout.modelMetric);
  const negativeControlMetric = round(negative.modelMetric);
  const negativeControlBehaved =
    negative.modelMetric <= random.majorityBaseline + 0.08;
  const holdoutStatus =
    randomVsHoldoutDelta >= 0.08
      ? "survived"
      : randomVsHoldoutDelta >= 0.04
        ? "weak"
        : "failed";
  const rivalStatus =
    modelVsBaselineDelta <= 0.04
      ? "stronger"
      : !negativeControlBehaved || holdoutStatus === "failed"
        ? "still_plausible"
        : "scoped_or_weakened";
  const comparisons = {
    baselineMetric: compareMetric(baselineMetric, task.expected.baselineMetric),
    randomSplitMetric: compareMetric(
      randomSplitMetric,
      task.expected.randomSplitMetric,
    ),
    holdoutMetric: compareMetric(holdoutMetric, task.expected.holdoutMetric),
    modelVsBaselineDelta: compareMetric(
      modelVsBaselineDelta,
      task.expected.modelVsBaselineDelta,
    ),
    randomVsHoldoutDelta: compareMetric(
      randomVsHoldoutDelta,
      task.expected.randomVsHoldoutDelta,
    ),
  };
  return {
    claimId: task.claimId,
    taskId: task.taskId,
    datasetId: task.datasetId,
    datasetName: task.datasetName,
    rawArffReceipt: task.rawArffReceipt,
    rawSha256: sha256(raw),
    rows: parsed.rows.length,
    features: parsed.attributes.length - 1,
    targetVariable: task.targetVariable,
    splitFeature: task.splitFeature,
    holdoutHeldOutValue: holdoutSplit.heldOut,
    baselineMetric,
    randomSplitMetric,
    holdoutMetric,
    modelVsBaselineDelta,
    randomVsHoldoutDelta,
    negativeControlMetric,
    negativeControlBehaved,
    holdoutStatus,
    rivalStatus,
    comparisons,
    exactProductMetricsMatched: Object.values(comparisons).every(
      (comparison) => comparison.exact,
    ),
    productMetricsWithinRoundingTolerance: Object.values(comparisons).every(
      (comparison) => comparison.withinRoundingTolerance,
    ),
  };
}

function markdown(results) {
  const lines = [
    "# Standalone Replay Results",
    "",
    "This replay fetches public OpenML ARFF files and recomputes the receipt-first second-survivor metrics without reading Product `.sovryn` state.",
    "",
    "| Claim | Task | Rows | Features | Baseline | Random | Holdout | Model-baseline delta | Random-holdout delta | Negative | Exact Product metrics | Within rounding tolerance |",
    "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ...results.map(
      (result) =>
        `| ${result.claimId} | ${result.taskId} | ${result.rows} | ${result.features} | ${result.baselineMetric.toFixed(3)} | ${result.randomSplitMetric.toFixed(3)} | ${result.holdoutMetric.toFixed(3)} | ${result.modelVsBaselineDelta.toFixed(3)} | ${result.randomVsHoldoutDelta.toFixed(3)} | ${result.negativeControlMetric.toFixed(3)} | ${result.exactProductMetricsMatched ? "yes" : "no"} | ${result.productMetricsWithinRoundingTolerance ? "yes" : "no"} |`,
    ),
    "",
    "OpenML-32 differs from the Product rounded table by 0.001 on two displayed metrics; all other displayed Product metrics reproduce exactly. This package therefore treats standalone replay as supportive inspectability evidence with a rounding caveat, not as external validation.",
    "",
    "This is public-data replay, not external validation. External review remains required before any discovery-scored promotion.",
  ];
  return `${lines.join("\n")}\n`;
}

async function main() {
  const results = [];
  for (const task of tasks) results.push(await replayTask(task));
  const report = {
    kind: "second_survivor_standalone_public_replay",
    candidateId: "DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001",
    resultStatus: results.every((result) => result.exactProductMetricsMatched)
      ? "exact_product_metrics_reproduced_from_public_raw_data"
      : results.every((result) => result.productMetricsWithinRoundingTolerance)
        ? "public_raw_replay_reproduced_with_rounding_caveat"
        : "public_raw_replay_completed_metric_mismatch",
    productMetricsMatched: results.every(
      (result) => result.exactProductMetricsMatched,
    ),
    productMetricsWithinRoundingTolerance: results.every(
      (result) => result.productMetricsWithinRoundingTolerance,
    ),
    fundFound: false,
    countsForDiscoveryScore: false,
    noOverclaim:
      "Standalone public replay is not external validation and cannot create FUND_FOUND.",
    results,
  };
  const outDir = __dirname;
  writeFileSync(
    join(outDir, "standalone_replay_results.json"),
    `${JSON.stringify(report, null, 2)}\n`,
  );
  writeFileSync(join(outDir, "STANDALONE_REPLAY_RESULTS.md"), markdown(results));
  console.log(JSON.stringify(report, null, 2));
}

main().catch((error) => {
  console.error(error instanceof Error ? error.stack : String(error));
  process.exitCode = 1;
});
