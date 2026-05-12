#!/usr/bin/env python3
"""Standalone reproduction check for the Matbench candidate.

This script intentionally does not depend on private Product `.sovryn` state.
It downloads or reads the public Matbench experimental band-gap JSON, computes
transparent composition-only proxy checks, replays the public-safe Product
runtime scalar formula, and compares both with the Product-recorded candidate
scalars.

The Product runtime scalars can be exactly replayed from
PRODUCT_RUNTIME_REPRODUCTION_SPEC.json. The scientific descriptor-transfer
residual still cannot be independently recomputed from raw Matbench data
because the descriptor matrix, model configuration, exact split, and raw-data
residual formula are not exposed. The script reports that gap explicitly and
downgrades public discovery-score eligibility.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
import statistics
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_URL = "https://huggingface.co/datasets/smgjch/Matbench/resolve/main/matbench_expt_gap.json"
PACKAGE_DIR = Path(__file__).resolve().parent
RAW_REPRODUCTION_BUNDLE_DIR = PACKAGE_DIR / "raw-reproduction-bundle"
BUNDLE_MANIFEST_PATH = RAW_REPRODUCTION_BUNDLE_DIR / "BUNDLE_MANIFEST.json"
BUNDLE_RUNTIME_EVIDENCE_PATH = (
    RAW_REPRODUCTION_BUNDLE_DIR
    / "product-state"
    / "discovery-daemon"
    / "generator-families"
    / "runtime-evidence"
    / "matbench_descriptor_transfer_significance_generator-output-01.json"
)
BUNDLE_SOURCE_CACHE_PATH = (
    RAW_REPRODUCTION_BUNDLE_DIR
    / "product-state"
    / "discovery-daemon"
    / "discovery-anchor-run"
    / "source-cache"
    / "DISC-ANCHOR-MATBENCH-DIELECTRIC-GAP.json"
)
LEGACY_RUNTIME_EVIDENCE_PATH = PACKAGE_DIR / "copied-product-evidence" / "runtime-evidence-output-01.json"
PRODUCT_RUNTIME_SPEC_PATH = PACKAGE_DIR / "PRODUCT_RUNTIME_REPRODUCTION_SPEC.json"

PRODUCT_RECORDED_VALUES = {
    "measured_outcome": 0.72,
    "residual_magnitude": 0.21,
    "composition_formula_size_target_family_baseline": 0.34,
    "matched_negative_control": 0.29,
    "null_or_trivial_rule": 0.23,
}

FEATURE_SCHEMA = [
    {
        "name": "element_count",
        "description": "Number of distinct elements parsed from the composition formula.",
    },
    {
        "name": "total_atoms",
        "description": "Sum of stoichiometric counts parsed from the composition formula.",
    },
    {
        "name": "mean_atomic_number",
        "description": "Stoichiometry-weighted mean atomic number.",
    },
    {
        "name": "atomic_number_range",
        "description": "Maximum atomic number minus minimum atomic number in the formula.",
    },
    {
        "name": "transition_metal_fraction",
        "description": "Fraction of parsed stoichiometric count belonging to transition metals.",
    },
    {
        "name": "max_atomic_number",
        "description": "Maximum atomic number in the formula.",
    },
    {
        "name": "min_atomic_number",
        "description": "Minimum atomic number in the formula.",
    },
]

MISSING_INPUTS = [
    {
        "input": "descriptor matrix / feature definition",
        "why_needed": "The Product claim refers to a descriptor-transfer residual, but the public package does not expose the exact pymatgen/matminer/ASE feature matrix or featurizer configuration.",
    },
    {
        "input": "model and training configuration",
        "why_needed": "The public package does not expose the model class, hyperparameters, preprocessing, target scaling, or random seed that map raw formulas to the Product measured outcome 0.72.",
    },
    {
        "input": "exact train/validation/holdout split and family labels",
        "why_needed": "The Product evidence names composition/formula-size/target-family and holdout pressure, but the public package does not expose the exact split manifest or target-family labels.",
    },
    {
        "input": "residual formula and score normalization",
        "why_needed": "The public package does not define the exact scalar transformation that produces residual magnitude 0.21 from model, baseline, holdout, and control outputs.",
    },
    {
        "input": "baseline implementation details",
        "why_needed": "The Product values 0.34, 0.29, and 0.23 are recorded scalars, but their exact algorithms are not exposed as executable public code.",
    },
    {
        "input": "target subset manifest",
        "why_needed": "The copied Product source-cache artifact records rawTargetCount 300, while the current public Matbench JSON contains more rows; the exact Product subset selection is not public.",
    },
    {
        "input": "external runnable holdout/counterexample manifests",
        "why_needed": "The public package records holdout, replay, and counterexample status, but does not expose an independent runnable manifest for those checks.",
    },
]

ATOMIC_NUMBERS = {
    "H": 1,
    "He": 2,
    "Li": 3,
    "Be": 4,
    "B": 5,
    "C": 6,
    "N": 7,
    "O": 8,
    "F": 9,
    "Ne": 10,
    "Na": 11,
    "Mg": 12,
    "Al": 13,
    "Si": 14,
    "P": 15,
    "S": 16,
    "Cl": 17,
    "Ar": 18,
    "K": 19,
    "Ca": 20,
    "Sc": 21,
    "Ti": 22,
    "V": 23,
    "Cr": 24,
    "Mn": 25,
    "Fe": 26,
    "Co": 27,
    "Ni": 28,
    "Cu": 29,
    "Zn": 30,
    "Ga": 31,
    "Ge": 32,
    "As": 33,
    "Se": 34,
    "Br": 35,
    "Kr": 36,
    "Rb": 37,
    "Sr": 38,
    "Y": 39,
    "Zr": 40,
    "Nb": 41,
    "Mo": 42,
    "Tc": 43,
    "Ru": 44,
    "Rh": 45,
    "Pd": 46,
    "Ag": 47,
    "Cd": 48,
    "In": 49,
    "Sn": 50,
    "Sb": 51,
    "Te": 52,
    "I": 53,
    "Xe": 54,
    "Cs": 55,
    "Ba": 56,
    "La": 57,
    "Ce": 58,
    "Pr": 59,
    "Nd": 60,
    "Pm": 61,
    "Sm": 62,
    "Eu": 63,
    "Gd": 64,
    "Tb": 65,
    "Dy": 66,
    "Ho": 67,
    "Er": 68,
    "Tm": 69,
    "Yb": 70,
    "Lu": 71,
    "Hf": 72,
    "Ta": 73,
    "W": 74,
    "Re": 75,
    "Os": 76,
    "Ir": 77,
    "Pt": 78,
    "Au": 79,
    "Hg": 80,
    "Tl": 81,
    "Pb": 82,
    "Bi": 83,
    "Po": 84,
    "At": 85,
    "Rn": 86,
}

TRANSITION_METALS = {
    "Sc",
    "Ti",
    "V",
    "Cr",
    "Mn",
    "Fe",
    "Co",
    "Ni",
    "Cu",
    "Zn",
    "Y",
    "Zr",
    "Nb",
    "Mo",
    "Tc",
    "Ru",
    "Rh",
    "Pd",
    "Ag",
    "Cd",
    "Hf",
    "Ta",
    "W",
    "Re",
    "Os",
    "Ir",
    "Pt",
    "Au",
    "Hg",
}


@dataclass(frozen=True)
class MatbenchRecord:
    formula: str
    band_gap: float
    composition: dict[str, float]


def fetch_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "sovryn-matbench-review/1.0"})
    with urllib.request.urlopen(request, timeout=90) as response:
        return response.read()


def package_relative(path: Path) -> str:
    try:
        return path.relative_to(PACKAGE_DIR).as_posix()
    except ValueError:
        return str(path)


def read_json_if_present(path: Path) -> dict[str, object] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def load_source(data_url: str, data_file: Path | None) -> tuple[bytes, str]:
    if data_file is not None:
        raw = data_file.read_bytes()
        return raw, str(data_file)
    return fetch_bytes(data_url), data_url


def parse_formula(formula: str) -> dict[str, float]:
    formula_parts = re.findall(r"[A-Z][a-z]?|[()\[\]]|\d+(?:\.\d+)?", formula)
    stack: list[dict[str, float]] = [{}]
    i = 0
    while i < len(formula_parts):
        part = formula_parts[i]
        if part in ("(", "["):
            stack.append({})
            i += 1
            continue
        if part in (")", "]"):
            group = stack.pop() if len(stack) > 1 else {}
            multiplier = 1.0
            if i + 1 < len(formula_parts) and re.fullmatch(r"\d+(?:\.\d+)?", formula_parts[i + 1]):
                multiplier = float(formula_parts[i + 1])
                i += 1
            for element, count in group.items():
                stack[-1][element] = stack[-1].get(element, 0.0) + count * multiplier
            i += 1
            continue
        if re.fullmatch(r"[A-Z][a-z]?", part):
            count = 1.0
            if i + 1 < len(formula_parts) and re.fullmatch(r"\d+(?:\.\d+)?", formula_parts[i + 1]):
                count = float(formula_parts[i + 1])
                i += 1
            stack[-1][part] = stack[-1].get(part, 0.0) + count
            i += 1
            continue
        i += 1
    return stack[0]


def extract_records(raw: bytes) -> list[MatbenchRecord]:
    obj = json.loads(raw)
    rows: Iterable[object]
    if isinstance(obj, list):
        rows = obj
    elif isinstance(obj, dict) and isinstance(obj.get("data"), list):
        rows = obj["data"]
    else:
        raise ValueError("Unsupported Matbench JSON shape: expected list or dict with data list")

    records: list[MatbenchRecord] = []
    for row in rows:
        formula: str | None = None
        value: float | None = None
        if isinstance(row, dict):
            if isinstance(row.get("problem"), str):
                match = re.search(r"->\s*([^\s]+)", row["problem"])
                if match:
                    formula = match.group(1).strip()
            elif isinstance(row.get("composition"), str):
                formula = row["composition"]
            elif isinstance(row.get("formula"), str):
                formula = row["formula"]
            for key in ("answer", "target", "band_gap", "gap"):
                if key in row:
                    value = float(row[key])
                    break
        elif isinstance(row, list) and len(row) >= 2:
            formula = str(row[0])
            value = float(row[1])
        if not formula or value is None:
            continue
        composition = parse_formula(formula)
        if composition:
            records.append(MatbenchRecord(formula=formula, band_gap=value, composition=composition))
    return records


def formula_features(record: MatbenchRecord) -> list[float]:
    counts = record.composition
    total_atoms = sum(counts.values())
    element_count = float(len(counts))
    z_values = [ATOMIC_NUMBERS.get(element, 0) for element in counts]
    weighted_z = sum(ATOMIC_NUMBERS.get(element, 0) * count for element, count in counts.items())
    mean_z = weighted_z / total_atoms if total_atoms else 0.0
    min_z = float(min(z_values) if z_values else 0)
    max_z = float(max(z_values) if z_values else 0)
    z_range = max_z - min_z
    transition_count = sum(count for element, count in counts.items() if element in TRANSITION_METALS)
    transition_fraction = transition_count / total_atoms if total_atoms else 0.0
    return [
        element_count,
        total_atoms,
        mean_z,
        z_range,
        transition_fraction,
        max_z,
        min_z,
    ]


def feature_dict(values: list[float]) -> dict[str, float]:
    return {schema["name"]: values[index] for index, schema in enumerate(FEATURE_SCHEMA)}


def deterministic_split(records: list[MatbenchRecord]) -> tuple[list[int], list[int]]:
    train: list[int] = []
    holdout: list[int] = []
    for idx, record in enumerate(records):
        digest = hashlib.sha256(record.formula.encode("utf-8")).hexdigest()
        bucket = int(digest[:8], 16) % 5
        if bucket == 0:
            holdout.append(idx)
        else:
            train.append(idx)
    if not holdout or not train:
        raise ValueError("Deterministic split produced an empty train or holdout set")
    return train, holdout


def select_columns(matrix: list[list[float]], columns: list[int]) -> list[list[float]]:
    return [[row[index] for index in columns] for row in matrix]


def standardize(train_x: list[list[float]], test_x: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    if not train_x:
        return train_x, test_x
    width = len(train_x[0])
    means = [statistics.mean(row[j] for row in train_x) for j in range(width)]
    scales = []
    for j in range(width):
        values = [row[j] for row in train_x]
        stdev = statistics.pstdev(values)
        scales.append(stdev if stdev > 1e-12 else 1.0)

    def transform(rows: list[list[float]]) -> list[list[float]]:
        return [[(row[j] - means[j]) / scales[j] for j in range(width)] for row in rows]

    return transform(train_x), transform(test_x)


def solve_linear_system(a: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    aug = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(aug[row][col]))
        if abs(aug[pivot][col]) < 1e-12:
            continue
        aug[col], aug[pivot] = aug[pivot], aug[col]
        divisor = aug[col][col]
        aug[col] = [value / divisor for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [aug[row][i] - factor * aug[col][i] for i in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def fit_linear_regression(train_x: list[list[float]], train_y: list[float], ridge: float = 1e-8) -> list[float]:
    design = [[1.0] + row for row in train_x]
    width = len(design[0])
    xtx = [[0.0 for _ in range(width)] for _ in range(width)]
    xty = [0.0 for _ in range(width)]
    for row, target in zip(design, train_y):
        for i in range(width):
            xty[i] += row[i] * target
            for j in range(width):
                xtx[i][j] += row[i] * row[j]
    for i in range(1, width):
        xtx[i][i] += ridge
    return solve_linear_system(xtx, xty)


def predict(coefficients: list[float], rows: list[list[float]]) -> list[float]:
    predictions = []
    for row in rows:
        predictions.append(coefficients[0] + sum(coefficients[i + 1] * value for i, value in enumerate(row)))
    return predictions


def metrics(actual: list[float], predicted: list[float]) -> dict[str, float]:
    if len(actual) != len(predicted):
        raise ValueError("actual and predicted lengths differ")
    mean_y = statistics.mean(actual)
    sse = sum((y - p) ** 2 for y, p in zip(actual, predicted))
    sst = sum((y - mean_y) ** 2 for y in actual)
    mae = sum(abs(y - p) for y, p in zip(actual, predicted)) / len(actual)
    rmse = math.sqrt(sse / len(actual))
    r2 = 1.0 - (sse / sst) if sst > 1e-12 else 0.0
    return {"r2": r2, "mae": mae, "rmse": rmse}


def run_linear_proxy(
    features: list[list[float]],
    targets: list[float],
    train_idx: list[int],
    holdout_idx: list[int],
    columns: list[int],
    shuffle_targets: bool = False,
) -> dict[str, float]:
    train_x = select_columns([features[i] for i in train_idx], columns)
    holdout_x = select_columns([features[i] for i in holdout_idx], columns)
    train_y = [targets[i] for i in train_idx]
    if shuffle_targets:
        shuffled = train_y[:]
        random.Random(1729).shuffle(shuffled)
        train_y = shuffled
    holdout_y = [targets[i] for i in holdout_idx]
    train_x, holdout_x = standardize(train_x, holdout_x)
    coefficients = fit_linear_regression(train_x, train_y)
    predicted = predict(coefficients, holdout_x)
    return metrics(holdout_y, predicted)


def run_linear_model(
    features: list[list[float]],
    targets: list[float],
    train_idx: list[int],
    holdout_idx: list[int],
    columns: list[int],
    shuffle_targets: bool = False,
) -> dict[str, object]:
    train_x_raw = select_columns([features[i] for i in train_idx], columns)
    holdout_x_raw = select_columns([features[i] for i in holdout_idx], columns)
    train_y = [targets[i] for i in train_idx]
    if shuffle_targets:
        shuffled = train_y[:]
        random.Random(1729).shuffle(shuffled)
        train_y = shuffled
    holdout_y = [targets[i] for i in holdout_idx]
    train_x, holdout_x = standardize(train_x_raw, holdout_x_raw)
    coefficients = fit_linear_regression(train_x, train_y)
    predictions = predict(coefficients, holdout_x)
    return {
        "columns": [FEATURE_SCHEMA[index]["name"] for index in columns],
        "shuffleTargets": shuffle_targets,
        "model": "ordinary_least_squares_with_intercept_and_ridge_1e-8_after_train_standardization",
        "coefficients": coefficients,
        "metrics": metrics(holdout_y, predictions),
        "holdoutPredictionCount": len(predictions),
    }


def load_runtime_evidence() -> tuple[dict[str, object] | None, str | None]:
    for path in (BUNDLE_RUNTIME_EVIDENCE_PATH, LEGACY_RUNTIME_EVIDENCE_PATH):
        payload = read_json_if_present(path)
        if payload is not None:
            return payload, package_relative(path)
    return None, None


def load_bundle_manifest() -> dict[str, object] | None:
    return read_json_if_present(BUNDLE_MANIFEST_PATH)


def load_product_runtime_spec() -> dict[str, object]:
    return json.loads(PRODUCT_RUNTIME_SPEC_PATH.read_text())


def product_runtime_scalar_replay(spec: dict[str, object]) -> dict[str, object]:
    ordinal = int(spec["ordinal"])
    born = ordinal <= 2
    if born:
        measured_outcome = 0.71 + ordinal / 100
        residual_magnitude = 0.22 - ordinal / 100
        baseline = 0.34
        control = 0.29
        null = 0.23
    else:
        measured_outcome = 0.48 + ordinal / 100
        residual_magnitude = 0.13 if ordinal == 8 else 0.07
        baseline = 0.48 + ordinal / 100
        control = 0.5
        null = 0.47
    return {
        "ordinal": ordinal,
        "born": born,
        "measured_outcome": round(measured_outcome, 12),
        "residual_magnitude": round(residual_magnitude, 12),
        "composition_formula_size_target_family_baseline": round(baseline, 12),
        "matched_negative_control": round(control, 12),
        "null_or_trivial_rule": round(null, 12),
    }


def nearly_equal(left: float, right: float, epsilon: float = 1e-12) -> bool:
    return abs(left - right) <= epsilon


def product_runtime_matches(recorded: dict[str, float], replay: dict[str, object]) -> bool:
    return all(nearly_equal(float(recorded[key]), float(replay[key])) for key in recorded)


def compute_reproduction(raw: bytes, source_ref: str) -> dict[str, object]:
    records = extract_records(raw)
    if not records:
        raise ValueError("No Matbench records could be extracted from raw source")
    source_hash = hashlib.sha256(raw).hexdigest()
    train_idx, holdout_idx = deterministic_split(records)
    features = [formula_features(record) for record in records]
    targets = [record.band_gap for record in records]
    train_set = set(train_idx)

    null_prediction = [statistics.mean(targets[i] for i in train_idx)] * len(holdout_idx)
    holdout_y = [targets[i] for i in holdout_idx]
    null_metrics = metrics(holdout_y, null_prediction)
    formula_size_model = run_linear_model(features, targets, train_idx, holdout_idx, columns=[0, 1])
    descriptor_proxy_model = run_linear_model(features, targets, train_idx, holdout_idx, columns=list(range(7)))
    matched_negative_model = run_linear_model(
        features,
        targets,
        train_idx,
        holdout_idx,
        columns=list(range(7)),
        shuffle_targets=True,
    )
    formula_size_metrics = formula_size_model["metrics"]
    descriptor_proxy_metrics = descriptor_proxy_model["metrics"]
    matched_negative_metrics = matched_negative_model["metrics"]
    residual_proxy = descriptor_proxy_metrics["r2"] - max(
        formula_size_metrics["r2"],
        matched_negative_metrics["r2"],
        null_metrics["r2"],
    )
    raw_data_reproducible_experiment = {
        "kind": "raw_data_reproducible_matbench_proxy_experiment",
        "status": "available_but_does_not_reproduce_product_scientific_claim",
        "claimScope": (
            "This is a public raw-data formula-descriptor proxy experiment. It is not the original Product "
            "descriptor-transfer computation and must not be used to restore discovery-scored status."
        ),
        "sourceRef": source_ref,
        "sourceHashSha256": source_hash,
        "featureSchema": FEATURE_SCHEMA,
        "splitRule": "sha256(formula)[0:8] modulo 5 equals 0 for holdout; all other buckets train",
        "model": "ordinary least squares with intercept, train-only standardization, and ridge 1e-8",
        "baselines": {
            "null_or_trivial_rule": {
                "definition": "predict train-target mean on deterministic holdout",
                "metrics": null_metrics,
            },
            "composition_formula_size": formula_size_model,
            "matched_negative_shuffled_target": matched_negative_model,
        },
        "candidateProxy": descriptor_proxy_model,
        "residualDefinition": "candidate_proxy_holdout_r2 - max(null_r2, formula_size_r2, shuffled_target_r2)",
        "residualProxyR2Delta": residual_proxy,
        "records": len(records),
        "trainRecords": len(train_idx),
        "holdoutRecords": len(holdout_idx),
        "reproducibilityDecision": (
            "The proxy experiment is exactly reproducible from public raw data and this script. "
            "It does not reproduce the Product descriptor-transfer scientific claim because the original "
            "descriptor matrix, model config, split manifest, target subset, residual formula, and baseline "
            "implementations were not present in Product artifacts."
        ),
    }
    raw_data_rows = [
        {
            "rowIndex": index,
            "formula": record.formula,
            "formulaHashSha256": hashlib.sha256(record.formula.encode("utf-8")).hexdigest(),
            "split": "train" if index in train_set else "holdout",
            "bandGap": record.band_gap,
            "features": feature_dict(features[index]),
        }
        for index, record in enumerate(records)
    ]

    runtime, runtime_path = load_runtime_evidence()
    bundle_manifest = load_bundle_manifest()
    bundle_source_cache = read_json_if_present(BUNDLE_SOURCE_CACHE_PATH)
    product_runtime_spec = load_product_runtime_spec()
    product_runtime_replay = product_runtime_scalar_replay(product_runtime_spec)
    exact_runtime_replay = product_runtime_matches(PRODUCT_RECORDED_VALUES, product_runtime_replay)
    raw_bundle_summary = {
        "path": "raw-reproduction-bundle/",
        "manifestPath": package_relative(BUNDLE_MANIFEST_PATH),
        "manifestLoaded": bundle_manifest is not None,
        "runtimeEvidencePathUsed": runtime_path,
        "sourceCachePath": package_relative(BUNDLE_SOURCE_CACHE_PATH) if bundle_source_cache is not None else None,
        "artifactCount": bundle_manifest.get("artifactCount") if bundle_manifest else None,
        "unsafeCopiedCount": bundle_manifest.get("unsafeCopiedCount") if bundle_manifest else None,
        "bundleDecision": bundle_manifest.get("bundleDecision") if bundle_manifest else "bundle_manifest_missing",
        "rawDataScientificReproductionSucceeded": (
            bundle_manifest.get("rawDataScientificReproductionSucceeded") if bundle_manifest else False
        ),
        "missingRawScientificInputs": bundle_manifest.get("missingRawScientificInputs") if bundle_manifest else [],
    }
    return {
        "status": "raw_scientific_reproduction_failed_product_values_runtime_derived",
        "publicReviewStatus": "not_external_review_ready_raw_scientific_reproduction_failed",
        "productValuesSourceClassification": "runtime_derived_deterministic_generator_scalars",
        "publicFundClass": "not_discovery_scored_raw_reproduction_failed",
        "publicDiscoveryScoreEligible": False,
        "publicExternalReviewReadinessScore": 0,
        "rawDataScientificReproductionAttempted": True,
        "source": {
            "sourceRef": source_ref,
            "sourceHashSha256": source_hash,
            "bytes": len(raw),
            "recordsExtracted": len(records),
            "trainRecords": len(train_idx),
            "holdoutRecords": len(holdout_idx),
            "targetMean": statistics.mean(targets),
            "targetMin": min(targets),
            "targetMax": max(targets),
        },
        "productRecordedValues": PRODUCT_RECORDED_VALUES,
        "productRuntimeReproductionSpec": {
            "path": "PRODUCT_RUNTIME_REPRODUCTION_SPEC.json",
            "status": product_runtime_spec["status"],
            "sourceProductCommit": product_runtime_spec["sourceProductCommit"],
            "productSourceRef": product_runtime_spec["productSourceRef"],
        },
        "rawReproductionBundle": raw_bundle_summary,
        "rawDataReproducibleExperiment": raw_data_reproducible_experiment,
        "rawDataFeatureMatrixRows": raw_data_rows,
        "productRuntimeReplayValues": product_runtime_replay,
        "standaloneProxyValues": {
            "descriptor_transfer_proxy_r2": descriptor_proxy_metrics["r2"],
            "residual_proxy_r2_delta": residual_proxy,
            "composition_formula_size_proxy_r2": formula_size_metrics["r2"],
            "matched_negative_control_proxy_r2": matched_negative_metrics["r2"],
            "null_or_trivial_rule_proxy_r2": null_metrics["r2"],
            "descriptor_transfer_proxy_mae": descriptor_proxy_metrics["mae"],
            "composition_formula_size_proxy_mae": formula_size_metrics["mae"],
            "matched_negative_control_proxy_mae": matched_negative_metrics["mae"],
            "null_or_trivial_rule_proxy_mae": null_metrics["mae"],
        },
        "exactProductRuntimeScalarsReproduced": exact_runtime_replay,
        "exactProductResidualReproduced": exact_runtime_replay,
        "exactProductBaselinesReproduced": exact_runtime_replay,
        "rawDataScientificResidualReproduced": False,
        "rawDataScientificBaselinesReproduced": False,
        "runtimeEvidenceLoaded": runtime is not None,
        "runtimeEvidencePathUsed": runtime_path,
        "missingInputs": MISSING_INPUTS,
        "interpretation": (
            "The Product runtime scalars were exactly replayed from the public-safe Product runtime reproduction spec. "
            "Inspection of the Product source shows those values are runtime-derived deterministic generator scalars, "
            "not recovered raw-data scientific outputs. "
            "The public Matbench raw JSON was also loaded and formula-only proxy checks were recomputed. "
            "The public-safe raw reproduction bundle was exported and searched, but it contains the same Product "
            "runtime evidence rather than the missing descriptor matrix, model, split, residual, and baseline inputs. "
            "The raw-data scientific descriptor-transfer residual failed exact reproduction because essential scientific "
            "inputs are not exposed in this public package."
        ),
    }


def fmt_number(value: object) -> str:
    if isinstance(value, (int, float)):
        return f"{value:.6g}"
    return str(value)


def write_result_table(result: dict[str, object], output_dir: Path) -> None:
    source = result["source"]
    bundle = result["rawReproductionBundle"]
    product = result["productRecordedValues"]
    runtime_replay = result["productRuntimeReplayValues"]
    proxy = result["standaloneProxyValues"]
    raw_experiment = result["rawDataReproducibleExperiment"]
    rows = [
        (
            "measured outcome",
            product["measured_outcome"],
            runtime_replay["measured_outcome"],
            proxy["descriptor_transfer_proxy_r2"],
            "Product runtime scalar reproduced; raw-data proxy is not scientific reproduction",
        ),
        (
            "residual magnitude",
            product["residual_magnitude"],
            runtime_replay["residual_magnitude"],
            proxy["residual_proxy_r2_delta"],
            "Product runtime scalar reproduced; raw-data proxy is not scientific reproduction",
        ),
        (
            "composition_formula_size_target_family_baseline",
            product["composition_formula_size_target_family_baseline"],
            runtime_replay["composition_formula_size_target_family_baseline"],
            proxy["composition_formula_size_proxy_r2"],
            "Product runtime scalar reproduced; formula-size proxy differs",
        ),
        (
            "matched_negative_control",
            product["matched_negative_control"],
            runtime_replay["matched_negative_control"],
            proxy["matched_negative_control_proxy_r2"],
            "Product runtime scalar reproduced; shuffled-target proxy differs",
        ),
        (
            "null_or_trivial_rule",
            product["null_or_trivial_rule"],
            runtime_replay["null_or_trivial_rule"],
            proxy["null_or_trivial_rule_proxy_r2"],
            "Product runtime scalar reproduced; train-mean proxy differs",
        ),
    ]
    lines = [
        "# Reproduction Result Table",
        "",
        "This table is generated by `reproduce_matbench_candidate.py`. It does not change the Product claim or Fund Gate result.",
        "",
        "## Standalone Status",
        "",
        f"- Status: `{result['status']}`",
        f"- Public review status: `{result['publicReviewStatus']}`",
        f"- Product values source classification: `{result['productValuesSourceClassification']}`",
        f"- Public FundClass: `{result['publicFundClass']}`",
        f"- Public discovery-score eligible: `{str(result['publicDiscoveryScoreEligible']).lower()}`",
        f"- Public external-review readiness score: `{result['publicExternalReviewReadinessScore']}`",
        f"- Product runtime scalars reproduced: `{str(result['exactProductRuntimeScalarsReproduced']).lower()}`",
        f"- Exact Product residual reproduced: `{str(result['exactProductResidualReproduced']).lower()}`",
        f"- Exact Product baselines reproduced: `{str(result['exactProductBaselinesReproduced']).lower()}`",
        f"- Raw-data scientific residual reproduced: `{str(result['rawDataScientificResidualReproduced']).lower()}`",
        f"- Raw-data scientific baselines reproduced: `{str(result['rawDataScientificBaselinesReproduced']).lower()}`",
        f"- Runtime evidence artifact loaded: `{str(result['runtimeEvidenceLoaded']).lower()}`",
        f"- Runtime evidence artifact used: `{result['runtimeEvidencePathUsed']}`",
        f"- Product runtime spec: `{result['productRuntimeReproductionSpec']['path']}`",
        f"- Public-safe raw reproduction bundle loaded: `{str(bundle['manifestLoaded']).lower()}`",
        f"- Public-safe bundle artifact count: `{bundle['artifactCount']}`",
        f"- Public-safe bundle decision: `{bundle['bundleDecision']}`",
        f"- Raw-data proxy experiment available: `{str(raw_experiment['status'] == 'available_but_does_not_reproduce_product_scientific_claim').lower()}`",
        "",
        "## Public Source Load",
        "",
        f"- Source ref: `{source['sourceRef']}`",
        f"- SHA-256: `{source['sourceHashSha256']}`",
        f"- Bytes loaded: `{source['bytes']}`",
        f"- Records extracted: `{source['recordsExtracted']}`",
        f"- Deterministic train records: `{source['trainRecords']}`",
        f"- Deterministic holdout records: `{source['holdoutRecords']}`",
        f"- Band-gap target mean: `{fmt_number(source['targetMean'])}`",
        f"- Band-gap target min/max: `{fmt_number(source['targetMin'])}` / `{fmt_number(source['targetMax'])}`",
        "",
        "## Product Values Versus Runtime Replay And Public Raw-Data Proxies",
        "",
        "| Quantity | Product-recorded value | Product runtime replay | Public raw-data proxy | Reproduction status |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for quantity, product_value, runtime_value, proxy_value, status in rows:
        lines.append(
            f"| {quantity} | {fmt_number(product_value)} | {fmt_number(runtime_value)} | {fmt_number(proxy_value)} | {status} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            str(result["interpretation"]),
            "",
            "The Product runtime replay verifies the copied Product scalars. The standalone proxy values are useful for checking public source access, formula parsing, deterministic splitting, and simple baseline behavior. They are not a replacement for the missing raw-data descriptor-transfer implementation.",
            "",
            "For a fully reproducible raw-data computation with explicit feature matrix, split manifest, baseline definitions, and result JSON, inspect `RAW_DATA_REPRODUCIBLE_EXPERIMENT_RESULTS.md` and `RAW_DATA_REPRODUCIBLE_EXPERIMENT_SPEC.md`.",
        ]
    )
    (output_dir / "REPRODUCTION_RESULT_TABLE.md").write_text("\n".join(lines) + "\n")


def write_raw_data_experiment_artifacts(result: dict[str, object], output_dir: Path) -> None:
    experiment = result["rawDataReproducibleExperiment"]
    rows = result["rawDataFeatureMatrixRows"]
    feature_matrix = {
        "kind": "raw_data_feature_matrix_manifest",
        "sourceRef": experiment["sourceRef"],
        "sourceHashSha256": experiment["sourceHashSha256"],
        "featureSchema": experiment["featureSchema"],
        "rows": rows,
    }
    split_manifest = {
        "kind": "raw_data_split_manifest",
        "splitRule": experiment["splitRule"],
        "sourceRef": experiment["sourceRef"],
        "sourceHashSha256": experiment["sourceHashSha256"],
        "trainRecords": experiment["trainRecords"],
        "holdoutRecords": experiment["holdoutRecords"],
        "rows": [
            {
                "rowIndex": row["rowIndex"],
                "formula": row["formula"],
                "formulaHashSha256": row["formulaHashSha256"],
                "split": row["split"],
            }
            for row in rows
        ],
    }
    spec = {
        "kind": "raw_data_reproducible_experiment_spec",
        "status": experiment["status"],
        "sourceRef": experiment["sourceRef"],
        "sourceHashSha256": experiment["sourceHashSha256"],
        "featureSchema": experiment["featureSchema"],
        "splitRule": experiment["splitRule"],
        "model": experiment["model"],
        "baselines": {
            "null_or_trivial_rule": experiment["baselines"]["null_or_trivial_rule"]["definition"],
            "composition_formula_size": "OLS using element_count and total_atoms",
            "matched_negative_shuffled_target": "OLS using all seven formula descriptors after deterministic train-target shuffle seed 1729",
        },
        "candidateProxy": "OLS using all seven formula descriptors",
        "residualDefinition": experiment["residualDefinition"],
        "claimScope": experiment["claimScope"],
    }
    result_payload = {
        "kind": "raw_data_reproducible_experiment_results",
        "status": experiment["status"],
        "sourceRef": experiment["sourceRef"],
        "sourceHashSha256": experiment["sourceHashSha256"],
        "records": experiment["records"],
        "trainRecords": experiment["trainRecords"],
        "holdoutRecords": experiment["holdoutRecords"],
        "baselines": experiment["baselines"],
        "candidateProxy": experiment["candidateProxy"],
        "residualDefinition": experiment["residualDefinition"],
        "residualProxyR2Delta": experiment["residualProxyR2Delta"],
        "reproducibilityDecision": experiment["reproducibilityDecision"],
        "productClaimReproduced": False,
        "discoveryScoreEligible": False,
    }
    (output_dir / "RAW_DATA_FEATURE_MATRIX.json").write_text(json.dumps(feature_matrix, indent=2, sort_keys=True) + "\n")
    (output_dir / "RAW_DATA_SPLIT_MANIFEST.json").write_text(json.dumps(split_manifest, indent=2, sort_keys=True) + "\n")
    (output_dir / "RAW_DATA_REPRODUCIBLE_EXPERIMENT_SPEC.json").write_text(
        json.dumps(spec, indent=2, sort_keys=True) + "\n"
    )
    (output_dir / "RAW_DATA_REPRODUCIBLE_EXPERIMENT_RESULTS.json").write_text(
        json.dumps(result_payload, indent=2, sort_keys=True) + "\n"
    )

    spec_lines = [
        "# Raw-Data Reproducible Experiment Spec",
        "",
        "This is a new public raw-data proxy experiment for inspectability. It does not reproduce or strengthen the Product descriptor-transfer claim.",
        "",
        "## Source",
        "",
        f"- Source ref: `{experiment['sourceRef']}`",
        f"- Source SHA-256: `{experiment['sourceHashSha256']}`",
        f"- Records: `{experiment['records']}`",
        "",
        "## Feature Schema",
        "",
        "| Feature | Definition |",
        "| --- | --- |",
    ]
    for schema in experiment["featureSchema"]:
        spec_lines.append(f"| `{schema['name']}` | {schema['description']} |")
    spec_lines.extend(
        [
            "",
            "## Split, Model, And Baselines",
            "",
            f"- Split rule: `{experiment['splitRule']}`",
            f"- Model: `{experiment['model']}`",
            "- Candidate proxy: OLS using all seven formula descriptors.",
            "- Null baseline: train-target mean on deterministic holdout.",
            "- Formula-size baseline: OLS using `element_count` and `total_atoms`.",
            "- Matched negative control: all-feature OLS after deterministic train-target shuffle with seed `1729`.",
            f"- Residual definition: `{experiment['residualDefinition']}`",
            "",
            "## Scope",
            "",
            str(experiment["claimScope"]),
        ]
    )
    (output_dir / "RAW_DATA_REPRODUCIBLE_EXPERIMENT_SPEC.md").write_text("\n".join(spec_lines) + "\n")

    baseline_rows = [
        ("null_or_trivial_rule", experiment["baselines"]["null_or_trivial_rule"]["metrics"]),
        ("composition_formula_size", experiment["baselines"]["composition_formula_size"]["metrics"]),
        ("matched_negative_shuffled_target", experiment["baselines"]["matched_negative_shuffled_target"]["metrics"]),
        ("candidate_formula_descriptor_proxy", experiment["candidateProxy"]["metrics"]),
    ]
    result_lines = [
        "# Raw-Data Reproducible Experiment Results",
        "",
        "These results are recomputed by `reproduce_matbench_candidate.py` from public Matbench raw data. They are not the original Product descriptor-transfer values.",
        "",
        "## Decision",
        "",
        f"- Status: `{experiment['status']}`",
        "- Product claim reproduced from raw data: `false`",
        "- Discovery-score eligible: `false`",
        f"- Reproducible proxy residual R2 delta: `{fmt_number(experiment['residualProxyR2Delta'])}`",
        "",
        "## Metrics",
        "",
        "| Check | R2 | MAE | RMSE |",
        "| --- | ---: | ---: | ---: |",
    ]
    for name, model_metrics in baseline_rows:
        result_lines.append(
            f"| `{name}` | {fmt_number(model_metrics['r2'])} | {fmt_number(model_metrics['mae'])} | {fmt_number(model_metrics['rmse'])} |"
        )
    result_lines.extend(
        [
            "",
            "## Interpretation",
            "",
            str(experiment["reproducibilityDecision"]),
        ]
    )
    (output_dir / "RAW_DATA_REPRODUCIBLE_EXPERIMENT_RESULTS.md").write_text("\n".join(result_lines) + "\n")

    baseline_lines = [
        "# Raw-Data Baseline Implementations",
        "",
        "The executable implementations are in `reproduce_matbench_candidate.py`. This document summarizes the exact public-data baselines used by the standalone raw-data proxy experiment.",
        "",
        "| Baseline | Implementation |",
        "| --- | --- |",
        "| `null_or_trivial_rule` | Predict the train-target mean for every deterministic holdout row. |",
        "| `composition_formula_size` | Fit OLS with intercept on train-standardized `element_count` and `total_atoms`; score on deterministic holdout. |",
        "| `matched_negative_shuffled_target` | Fit the same all-feature OLS after deterministic train-target shuffle with seed `1729`; score on deterministic holdout. |",
        "| `candidate_formula_descriptor_proxy` | Fit OLS with intercept on all seven formula descriptors; score on deterministic holdout. |",
        "",
        "All baselines are intentionally simple and dependency-free so an external reviewer can rerun them with only Python standard library.",
    ]
    (output_dir / "RAW_DATA_BASELINE_IMPLEMENTATIONS.md").write_text("\n".join(baseline_lines) + "\n")


def write_missing_inputs(result: dict[str, object], output_dir: Path) -> None:
    bundle = result["rawReproductionBundle"]
    lines = [
        "# Missing Reproduction Inputs",
        "",
        "Product runtime scalar replay is now exact. Exact independent raw-data scientific recomputation of the Matbench descriptor-transfer residual remains blocked by the following missing public inputs.",
        "",
        "## Resolved Product Runtime Inputs",
        "",
        "| Input | Status | Artifact |",
        "| --- | --- | --- |",
        "| generator id / output id / ordinal rule | resolved | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |",
        "| Product runtime formulas | resolved | `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json` |",
        f"| public-safe Product artifact bundle | exported/searched | `{bundle['manifestPath']}` |",
        "| measured outcome `0.72` | reproduced | `REPRODUCTION_RESULT_TABLE.md` |",
        "| residual magnitude `0.21` | reproduced | `REPRODUCTION_RESULT_TABLE.md` |",
        "| baseline scalars `0.34`, `0.29`, `0.23` | reproduced | `REPRODUCTION_RESULT_TABLE.md` |",
        "| public raw-data proxy experiment | reproducible but separate from Product claim | `RAW_DATA_REPRODUCIBLE_EXPERIMENT_RESULTS.md` |",
        "",
        "## Unresolved Raw-Data Scientific Inputs",
        "",
        "The public-safe raw reproduction bundle was exported and searched. It contains Product runtime evidence, source receipts, generated evidence packages, candidate drafts, and review handoff artifacts. It does not contain the scientific raw-data inputs below.",
        "",
        "| Missing input | Why it is required |",
        "| --- | --- |",
    ]
    for item in result["missingInputs"]:
        lines.append(f"| {item['input']} | {item['why_needed']} |")
    lines.extend(
        [
            "",
            "## Classification",
            "",
            "- Product runtime residual reproduced exactly: yes.",
            "- Product runtime baselines reproduced exactly: yes.",
            "- Raw-data scientific residual reproduced exactly: no.",
            "- Raw-data scientific baselines reproduced exactly: no.",
            "- Public raw Matbench source loaded: yes.",
            "- Public proxy checks produced: yes.",
            "- Public raw-data proxy experiment fully specified: yes.",
            "- Product values source classification: runtime_derived_deterministic_generator_scalars.",
            f"- Public-safe bundle decision: {bundle['bundleDecision']}.",
            "- Updated review readiness: not_external_review_ready_raw_scientific_reproduction_failed.",
            "- Public discovery-score eligibility: false.",
        ]
    )
    (output_dir / "MISSING_REPRODUCTION_INPUTS.md").write_text("\n".join(lines) + "\n")


def write_raw_scientific_repair_decision(result: dict[str, object], output_dir: Path) -> None:
    decision = {
        "kind": "raw_scientific_reproduction_repair_decision",
        "candidateId": "DISCOVERY-LIFT-INSIGHT-HARD-GEN-MATBENCH-DESCRIPTOR-TRANSFER-SIGNIFICAN-74933C45D6DB",
        "rawDataScientificReproductionSucceeded": False,
        "productRuntimeScalarsReproduced": result["exactProductRuntimeScalarsReproduced"],
        "productValuesSourceClassification": result["productValuesSourceClassification"],
        "publicReviewStatus": result["publicReviewStatus"],
        "publicFundClass": result["publicFundClass"],
        "publicDiscoveryScoreEligible": result["publicDiscoveryScoreEligible"],
        "publicExternalReviewReadinessScore": result["publicExternalReviewReadinessScore"],
        "rawReproductionBundle": result["rawReproductionBundle"],
        "reason": "Exact Product values are replayable from deterministic Product runtime formulas, but the public package does not contain raw-data descriptor-transfer inputs needed to recompute them scientifically from Matbench data.",
        "missingInputs": result["missingInputs"],
    }
    (output_dir / "RAW_SCIENTIFIC_REPRODUCTION_REPAIR.json").write_text(
        json.dumps(decision, indent=2, sort_keys=True) + "\n"
    )
    lines = [
        "# Raw Scientific Reproduction Repair Decision",
        "",
        "## Decision",
        "",
        "`not_external_review_ready_raw_scientific_reproduction_failed`",
        "",
        "The Product runtime scalars are exactly replayable, but exact raw-data scientific reproduction failed.",
        "",
        "## Product Values Source",
        "",
        "`runtime_derived_deterministic_generator_scalars`",
        "",
        "The Product values `0.72`, `0.21`, `0.34`, `0.29`, and `0.23` are generated by the public-safe runtime formula documented in `PRODUCT_RUNTIME_REPRODUCTION_SPEC.json`. They are not recovered from a public Matbench descriptor matrix, trained model, split manifest, residual formula, or executable baseline implementation.",
        "",
        "## Public-Safe Bundle Search",
        "",
        f"- Bundle path: `{result['rawReproductionBundle']['path']}`",
        f"- Bundle manifest loaded: `{str(result['rawReproductionBundle']['manifestLoaded']).lower()}`",
        f"- Bundle artifact count: `{result['rawReproductionBundle']['artifactCount']}`",
        f"- Bundle decision: `{result['rawReproductionBundle']['bundleDecision']}`",
        f"- Runtime evidence path used: `{result['rawReproductionBundle']['runtimeEvidencePathUsed']}`",
        "",
        "The exported bundle makes the Product evidence trail publicly inspectable. It does not supply the missing raw-data scientific reproduction inputs.",
        "",
        "## Public Scoring Impact",
        "",
        "- Public FundClass: `not_discovery_scored_raw_reproduction_failed`.",
        "- Public Einstein/Nobel discovery-score eligible: `false`.",
        "- Public external-review readiness score for the discovery claim: `0/100`.",
        "- Product Fund Gate artifacts remain preserved as historical Product state, not as public scientific validation.",
        "",
        "## Raw-Data Scientific Reproduction",
        "",
        "- Public Matbench JSON loaded: yes.",
        "- Formula-only proxy checks run: yes.",
        "- Separate raw-data proxy experiment fully reproducible: yes.",
        "- Exact raw-data descriptor-transfer residual reproduced: no.",
        "- Exact raw-data baselines reproduced: no.",
        "",
        "## No Overclaim",
        "",
        "This decision does not invalidate the existence of the Product runtime package. It does downgrade the public scientific status: the package must not be treated as an externally-review-ready discovery candidate unless the missing raw-data scientific inputs are later supplied and reproduced.",
    ]
    (output_dir / "RAW_SCIENTIFIC_REPRODUCTION_REPAIR.md").write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-url", default=DEFAULT_URL, help="Public Matbench JSON URL")
    parser.add_argument("--data-file", type=Path, default=None, help="Optional local Matbench JSON file")
    parser.add_argument("--output-dir", type=Path, default=PACKAGE_DIR, help="Directory for generated result artifacts")
    args = parser.parse_args()

    raw, source_ref = load_source(args.data_url, args.data_file)
    result = compute_reproduction(raw, source_ref)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "standalone_reproduction_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    write_result_table(result, args.output_dir)
    write_raw_data_experiment_artifacts(result, args.output_dir)
    write_missing_inputs(result, args.output_dir)
    write_raw_scientific_repair_decision(result, args.output_dir)
    print(json.dumps({"status": result["status"], "recordsExtracted": result["source"]["recordsExtracted"]}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
