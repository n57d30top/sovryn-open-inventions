#!/usr/bin/env python3
"""Standalone public-data reproduction check for the Matbench candidate.

This script intentionally does not depend on private Product `.sovryn` state.
It downloads or reads the public Matbench experimental band-gap JSON, computes
transparent composition-only proxy checks, and compares those proxies with the
Product-recorded candidate scalars.

The Product descriptor-transfer residual cannot be exactly recomputed from this
public package because the descriptor matrix, model configuration, exact split,
and residual formula are not exposed. The script reports that gap explicitly.
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
RUNTIME_EVIDENCE_PATH = PACKAGE_DIR / "copied-product-evidence" / "runtime-evidence-output-01.json"

PRODUCT_RECORDED_VALUES = {
    "measured_outcome": 0.72,
    "residual_magnitude": 0.21,
    "composition_formula_size_target_family_baseline": 0.34,
    "matched_negative_control": 0.29,
    "null_or_trivial_rule": 0.23,
}

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


def load_runtime_evidence() -> dict[str, object] | None:
    if not RUNTIME_EVIDENCE_PATH.exists():
        return None
    return json.loads(RUNTIME_EVIDENCE_PATH.read_text())


def compute_reproduction(raw: bytes, source_ref: str) -> dict[str, object]:
    records = extract_records(raw)
    if not records:
        raise ValueError("No Matbench records could be extracted from raw source")
    source_hash = hashlib.sha256(raw).hexdigest()
    train_idx, holdout_idx = deterministic_split(records)
    features = [formula_features(record) for record in records]
    targets = [record.band_gap for record in records]

    null_prediction = [statistics.mean(targets[i] for i in train_idx)] * len(holdout_idx)
    holdout_y = [targets[i] for i in holdout_idx]
    null_metrics = metrics(holdout_y, null_prediction)
    formula_size_metrics = run_linear_proxy(features, targets, train_idx, holdout_idx, columns=[0, 1])
    descriptor_proxy_metrics = run_linear_proxy(features, targets, train_idx, holdout_idx, columns=list(range(7)))
    matched_negative_metrics = run_linear_proxy(
        features,
        targets,
        train_idx,
        holdout_idx,
        columns=list(range(7)),
        shuffle_targets=True,
    )
    residual_proxy = descriptor_proxy_metrics["r2"] - max(
        formula_size_metrics["r2"],
        matched_negative_metrics["r2"],
        null_metrics["r2"],
    )

    runtime = load_runtime_evidence()
    return {
        "status": "incomplete_exact_reproduction_public_proxy_checks_only",
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
        "exactProductResidualReproduced": False,
        "exactProductBaselinesReproduced": False,
        "runtimeEvidenceLoaded": runtime is not None,
        "missingInputs": MISSING_INPUTS,
        "interpretation": (
            "The public Matbench raw JSON was loaded and formula-only proxy checks were recomputed. "
            "The Product-recorded descriptor-transfer measured outcome, residual magnitude, and baseline scalars "
            "were not exactly reproduced because essential Product inputs are not exposed in this public package."
        ),
    }


def fmt_number(value: object) -> str:
    if isinstance(value, (int, float)):
        return f"{value:.6g}"
    return str(value)


def write_result_table(result: dict[str, object], output_dir: Path) -> None:
    source = result["source"]
    product = result["productRecordedValues"]
    proxy = result["standaloneProxyValues"]
    rows = [
        (
            "measured outcome",
            product["measured_outcome"],
            proxy["descriptor_transfer_proxy_r2"],
            "not exactly reproduced; public descriptor proxy only",
        ),
        (
            "residual magnitude",
            product["residual_magnitude"],
            proxy["residual_proxy_r2_delta"],
            "not exactly reproduced; proxy R2 delta only",
        ),
        (
            "composition_formula_size_target_family_baseline",
            product["composition_formula_size_target_family_baseline"],
            proxy["composition_formula_size_proxy_r2"],
            "not exactly reproduced; formula-size proxy only",
        ),
        (
            "matched_negative_control",
            product["matched_negative_control"],
            proxy["matched_negative_control_proxy_r2"],
            "not exactly reproduced; deterministic shuffled-target proxy only",
        ),
        (
            "null_or_trivial_rule",
            product["null_or_trivial_rule"],
            proxy["null_or_trivial_rule_proxy_r2"],
            "not exactly reproduced; train-mean holdout proxy only",
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
        f"- Exact Product residual reproduced: `{str(result['exactProductResidualReproduced']).lower()}`",
        f"- Exact Product baselines reproduced: `{str(result['exactProductBaselinesReproduced']).lower()}`",
        f"- Runtime evidence artifact loaded: `{str(result['runtimeEvidenceLoaded']).lower()}`",
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
        "## Product Values Versus Standalone Public Proxies",
        "",
        "| Quantity | Product-recorded value | Standalone public proxy | Reproduction status |",
        "| --- | ---: | ---: | --- |",
    ]
    for quantity, product_value, proxy_value, status in rows:
        lines.append(f"| {quantity} | {fmt_number(product_value)} | {fmt_number(proxy_value)} | {status} |")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            str(result["interpretation"]),
            "",
            "The standalone proxy values are useful for checking public source access, formula parsing, deterministic splitting, and simple baseline behavior. They are not a replacement for the missing Product descriptor-transfer implementation.",
        ]
    )
    (output_dir / "REPRODUCTION_RESULT_TABLE.md").write_text("\n".join(lines) + "\n")


def write_missing_inputs(result: dict[str, object], output_dir: Path) -> None:
    lines = [
        "# Missing Reproduction Inputs",
        "",
        "Exact independent recomputation of the Product-recorded Matbench descriptor-transfer residual is blocked by the following missing public inputs.",
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
            "- Residual reproduced exactly: no.",
            "- Baselines reproduced exactly: no.",
            "- Public raw Matbench source loaded: yes.",
            "- Public proxy checks produced: yes.",
            "- Updated review readiness: external_review_ready_with_major_caveats; exact standalone scientific reproduction remains incomplete.",
        ]
    )
    (output_dir / "MISSING_REPRODUCTION_INPUTS.md").write_text("\n".join(lines) + "\n")


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
    write_missing_inputs(result, args.output_dir)
    print(json.dumps({"status": result["status"], "recordsExtracted": result["source"]["recordsExtracted"]}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
