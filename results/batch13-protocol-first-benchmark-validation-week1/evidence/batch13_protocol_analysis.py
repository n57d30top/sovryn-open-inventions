#!/usr/bin/env python3
"""Batch 13 protocol-first benchmark validation evidence runner.

This is a target-specific research runner, not a Sovryn framework layer.
It downloads public UCI benchmark archives, compares source-described
train/test files against random stratified challengers, and emits compact
public-safe JSON evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import shutil
import sys
import urllib.request
import zipfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import sklearn
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


SEED = 42
REPLAY_SEED = 99


@dataclass(frozen=True)
class TargetSpec:
    slug: str
    name: str
    source_url: str
    documentation_url: str
    zip_name: str
    protocol_signal: str
    expected_risk: str


TARGETS = [
    TargetSpec(
        slug="uci-human-activity-recognition-smartphones",
        name="UCI Human Activity Recognition Using Smartphones",
        source_url="https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip",
        documentation_url="https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones",
        zip_name="har.zip",
        protocol_signal="source archive contains train/test files and subject_train/subject_test files",
        expected_risk="ordinary random split can mix subjects and weaken the source holdout question",
    ),
    TargetSpec(
        slug="uci-optical-recognition-handwritten-digits",
        name="UCI Optical Recognition of Handwritten Digits",
        source_url="https://archive.ics.uci.edu/static/public/80/optical+recognition+of+handwritten+digits.zip",
        documentation_url="https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits",
        zip_name="optdigits.zip",
        protocol_signal="source archive contains optdigits.tra and optdigits.tes files",
        expected_risk="random split may hide source train/test distribution differences",
    ),
    TargetSpec(
        slug="uci-pen-based-handwritten-digits",
        name="UCI Pen-Based Recognition of Handwritten Digits",
        source_url="https://archive.ics.uci.edu/static/public/81/pen+based+recognition+of+handwritten+digits.zip",
        documentation_url="https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits",
        zip_name="pendigits.zip",
        protocol_signal="source archive contains pendigits.tra and pendigits.tes files",
        expected_risk="random split may not test the same source-provided holdout distribution",
    ),
]


def rounded(value: Any) -> Any:
    if isinstance(value, bool):
        return value
    if isinstance(value, (np.floating, float)):
        return round(float(value), 6)
    if isinstance(value, (np.integer, int)):
        return int(value)
    if isinstance(value, dict):
        return {str(k): rounded(v) for k, v in value.items()}
    if isinstance(value, list):
        return [rounded(v) for v in value]
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(spec: TargetSpec, data_dir: Path) -> Path:
    data_dir.mkdir(parents=True, exist_ok=True)
    path = data_dir / spec.zip_name
    if path.exists() and path.stat().st_size > 0:
        return path
    request = urllib.request.Request(spec.source_url, headers={"User-Agent": "sovryn-batch13/1.0"})
    with urllib.request.urlopen(request, timeout=120) as response:
        path.write_bytes(response.read())
    return path


def extract(zip_path: Path, extract_dir: Path) -> Path:
    target = extract_dir / zip_path.stem
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as archive:
        archive.extractall(target)
    nested_zips = sorted(target.rglob("*.zip"))
    for nested_zip in nested_zips:
        nested_target = nested_zip.with_suffix("")
        nested_target.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(nested_zip) as archive:
            archive.extractall(nested_target)
    return target


def read_table(path: Path, sep: str = ",", header: int | None = None) -> pd.DataFrame:
    return pd.read_csv(path, sep=sep, header=header)


def find_file(root: Path, name: str) -> Path:
    matches = sorted(root.rglob(name))
    if not matches:
        raise FileNotFoundError(f"missing {name} below extracted archive")
    return matches[0]


def load_har(root: Path) -> dict[str, Any]:
    x_train = read_table(find_file(root, "X_train.txt"), sep=r"\s+")
    x_test = read_table(find_file(root, "X_test.txt"), sep=r"\s+")
    y_train = read_table(find_file(root, "y_train.txt"), sep=r"\s+").iloc[:, 0].astype(str)
    y_test = read_table(find_file(root, "y_test.txt"), sep=r"\s+").iloc[:, 0].astype(str)
    subject_train = read_table(find_file(root, "subject_train.txt"), sep=r"\s+").iloc[:, 0].astype(str)
    subject_test = read_table(find_file(root, "subject_test.txt"), sep=r"\s+").iloc[:, 0].astype(str)
    features_path = find_file(root, "features.txt")
    features = read_table(features_path, sep=r"\s+").iloc[:, 1].astype(str).tolist()
    x_train.columns = [f"f_{i}_{name}" for i, name in enumerate(features)]
    x_test.columns = x_train.columns
    return {
        "x_train": x_train,
        "x_test": x_test,
        "y_train": y_train,
        "y_test": y_test,
        "feature_names": list(x_train.columns),
        "protocol_metadata": {
            "officialTrainFile": "train/X_train.txt",
            "officialTestFile": "test/X_test.txt",
            "subjectTrainCount": int(subject_train.nunique()),
            "subjectTestCount": int(subject_test.nunique()),
            "subjectOverlapCount": int(len(set(subject_train) & set(subject_test))),
            "subjectGroupingAvailable": True,
        },
    }


def load_optdigits(root: Path) -> dict[str, Any]:
    train = read_table(find_file(root, "optdigits.tra"))
    test = read_table(find_file(root, "optdigits.tes"))
    feature_names = [f"pixel_{i}" for i in range(train.shape[1] - 1)]
    x_train = train.iloc[:, :-1].copy()
    x_test = test.iloc[:, :-1].copy()
    x_train.columns = feature_names
    x_test.columns = feature_names
    y_train = train.iloc[:, -1].astype(str)
    y_test = test.iloc[:, -1].astype(str)
    return {
        "x_train": x_train,
        "x_test": x_test,
        "y_train": y_train,
        "y_test": y_test,
        "feature_names": feature_names,
        "protocol_metadata": {
            "officialTrainFile": "optdigits.tra",
            "officialTestFile": "optdigits.tes",
            "sourceSplitFilesAvailable": True,
            "groupingAvailable": False,
        },
    }


def load_pendigits(root: Path) -> dict[str, Any]:
    train = read_table(find_file(root, "pendigits.tra"))
    test = read_table(find_file(root, "pendigits.tes"))
    feature_names = [f"coordinate_{i}" for i in range(train.shape[1] - 1)]
    x_train = train.iloc[:, :-1].copy()
    x_test = test.iloc[:, :-1].copy()
    x_train.columns = feature_names
    x_test.columns = feature_names
    y_train = train.iloc[:, -1].astype(str)
    y_test = test.iloc[:, -1].astype(str)
    return {
        "x_train": x_train,
        "x_test": x_test,
        "y_train": y_train,
        "y_test": y_test,
        "feature_names": feature_names,
        "protocol_metadata": {
            "officialTrainFile": "pendigits.tra",
            "officialTestFile": "pendigits.tes",
            "sourceSplitFilesAvailable": True,
            "groupingAvailable": False,
        },
    }


LOADERS = {
    "uci-human-activity-recognition-smartphones": load_har,
    "uci-optical-recognition-handwritten-digits": load_optdigits,
    "uci-pen-based-handwritten-digits": load_pendigits,
}


def schema_package(spec: TargetSpec, zip_path: Path, loaded: dict[str, Any]) -> dict[str, Any]:
    x_all = pd.concat([loaded["x_train"], loaded["x_test"]], axis=0, ignore_index=True)
    y_all = pd.concat([loaded["y_train"], loaded["y_test"]], axis=0, ignore_index=True)
    class_counts = Counter(y_all)
    source_hash = sha256_file(zip_path)
    combined = x_all.copy()
    combined["target"] = y_all.to_numpy()
    missing_cells = int(combined.isna().sum().sum())
    duplicate_full_rows = int(combined.duplicated().sum())
    duplicate_feature_rows = int(x_all.duplicated().sum())
    numeric_ranges: dict[str, dict[str, float]] = {}
    for column in list(x_all.columns[: min(10, x_all.shape[1])]):
        series = pd.to_numeric(x_all[column], errors="coerce")
        numeric_ranges[column] = {
            "min": float(series.min()),
            "max": float(series.max()),
            "mean": float(series.mean()),
        }
    return rounded(
        {
            "tool": "schema_provenance_auditor",
            "toolRole": "packaging_only",
            "sourceBinding": {"zipFile": spec.zip_name, "sha256": source_hash},
            "rows": int(combined.shape[0]),
            "trainRows": int(loaded["x_train"].shape[0]),
            "testRows": int(loaded["x_test"].shape[0]),
            "featureCount": int(x_all.shape[1]),
            "classCount": int(len(class_counts)),
            "classDistribution": dict(sorted(class_counts.items())),
            "missingCells": missing_cells,
            "duplicateFullRows": duplicate_full_rows,
            "duplicateFeatureRows": duplicate_feature_rows,
            "numericRangeSample": numeric_ranges,
            "protocolMetadata": loaded["protocol_metadata"],
            "pandasBaseline": {
                "isnaSum": missing_cells,
                "duplicatedFullRows": duplicate_full_rows,
                "valueCountsAvailable": True,
            },
            "addedValueBeyondPandas": "source-hash-bound evidence packaging and explicit protocol metadata, not raw discovery",
            "limitations": [
                "Does not prove semantic correctness of the source split.",
                "Duplicate feature rows may be legitimate repeated observations.",
            ],
        }
    )


def classifier(name: str) -> Any:
    if name == "dummy_most_frequent":
        return DummyClassifier(strategy="most_frequent")
    if name == "dummy_stratified":
        return DummyClassifier(strategy="stratified", random_state=SEED)
    if name == "logistic_regression":
        return make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=1200, random_state=SEED),
        )
    if name == "random_forest":
        return RandomForestClassifier(n_estimators=80, random_state=SEED, n_jobs=-1)
    raise ValueError(name)


def evaluate_model(model: Any, x_train: pd.DataFrame, y_train: pd.Series, x_test: pd.DataFrame, y_test: pd.Series) -> dict[str, Any]:
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    labels = sorted(pd.unique(pd.concat([y_train, y_test], ignore_index=True)))
    report = classification_report(y_test, predictions, labels=labels, output_dict=True, zero_division=0)
    class_f1 = {label: report[label]["f1-score"] for label in labels}
    matrix = confusion_matrix(y_test, predictions, labels=labels)
    row_sums = matrix.sum(axis=1)
    confused = []
    for idx, label in enumerate(labels):
        row = matrix[idx].copy()
        correct = int(row[idx])
        row[idx] = 0
        worst_idx = int(row.argmax()) if row.size else 0
        confused.append(
            {
                "class": str(label),
                "support": int(row_sums[idx]),
                "correct": correct,
                "worstConfusedAs": str(labels[worst_idx]),
                "worstConfusionCount": int(row[worst_idx]),
            }
        )
    return rounded(
        {
            "accuracy": accuracy_score(y_test, predictions),
            "macroF1": f1_score(y_test, predictions, average="macro", zero_division=0),
            "perClassF1": class_f1,
            "confusionSummary": confused,
        }
    )


def run_baselines(x_train: pd.DataFrame, y_train: pd.Series, x_test: pd.DataFrame, y_test: pd.Series) -> dict[str, Any]:
    output = {}
    for model_name in ["dummy_most_frequent", "dummy_stratified", "logistic_regression", "random_forest"]:
        output[model_name] = evaluate_model(classifier(model_name), x_train, y_train, x_test, y_test)
    return output


def random_challenger(loaded: dict[str, Any], seed: int = SEED) -> dict[str, Any]:
    x_all = pd.concat([loaded["x_train"], loaded["x_test"]], axis=0, ignore_index=True)
    y_all = pd.concat([loaded["y_train"], loaded["y_test"]], axis=0, ignore_index=True)
    test_size = len(loaded["y_test"]) / len(y_all)
    x_train, x_test, y_train, y_test = train_test_split(
        x_all,
        y_all,
        test_size=test_size,
        random_state=seed,
        stratify=y_all,
    )
    return {
        "split": {
            "type": "stratified_random_challenger",
            "seed": seed,
            "testSizeFraction": float(test_size),
            "trainRows": int(len(y_train)),
            "testRows": int(len(y_test)),
        },
        "baselines": run_baselines(x_train, y_train, x_test, y_test),
    }


def metric_stress(
    loaded: dict[str, Any],
    protocol_baselines: dict[str, Any],
    random_baselines: dict[str, Any],
) -> dict[str, Any]:
    x_train = loaded["x_train"]
    y_train = loaded["y_train"]
    x_test = loaded["x_test"]
    y_test = loaded["y_test"]
    rng = np.random.default_rng(SEED)
    shuffled_y = pd.Series(rng.permutation(y_train.to_numpy()), index=y_train.index).astype(str)
    shuffled = evaluate_model(classifier("logistic_regression"), x_train, shuffled_y, x_test, y_test)
    seed_runs = []
    for seed in [7, 42, 99]:
        challenge = random_challenger(loaded, seed)
        seed_runs.append(
            {
                "seed": seed,
                "logisticAccuracy": challenge["baselines"]["logistic_regression"]["accuracy"],
                "logisticMacroF1": challenge["baselines"]["logistic_regression"]["macroF1"],
            }
        )
    protocol_logistic = protocol_baselines["logistic_regression"]
    random_logistic = random_baselines["logistic_regression"]
    per_class_values = list(protocol_logistic["perClassF1"].values())
    min_class = min(protocol_logistic["perClassF1"], key=protocol_logistic["perClassF1"].get)
    return rounded(
        {
            "tool": "metric_stress_validator",
            "toolRole": "reusable_support_tool",
            "shuffledLabelControl": shuffled,
            "macroVsAccuracy": {
                "protocolAccuracy": protocol_logistic["accuracy"],
                "protocolMacroF1": protocol_logistic["macroF1"],
                "protocolAccuracyMinusMacroF1": protocol_logistic["accuracy"] - protocol_logistic["macroF1"],
                "randomAccuracy": random_logistic["accuracy"],
                "randomMacroF1": random_logistic["macroF1"],
                "randomAccuracyMinusMacroF1": random_logistic["accuracy"] - random_logistic["macroF1"],
            },
            "classRisk": {
                "minProtocolClassF1": min(per_class_values),
                "maxProtocolClassF1": max(per_class_values),
                "weakestProtocolClass": str(min_class),
            },
            "seedSplitSensitivity": seed_runs,
            "flags": {
                "shuffledControlSuspicious": shuffled["macroF1"] > 0.35,
                "accuracyCouldHideClassFailure": (protocol_logistic["accuracy"] - protocol_logistic["macroF1"]) > 0.03,
                "randomSplitMateriallyDifferent": abs(random_logistic["macroF1"] - protocol_logistic["macroF1"]) > 0.02,
            },
            "addedValueBeyondSklearn": "binds normal sklearn metrics to shuffled-label, class-risk, and seed/split controls",
            "limitations": [
                "Does not prove the source protocol is the official published benchmark protocol.",
                "Does not prove absence of leakage; it only exposes stress symptoms.",
            ],
        }
    )


def analyze_target(spec: TargetSpec, data_dir: Path, extract_dir: Path) -> dict[str, Any]:
    zip_path = download(spec, data_dir)
    extracted = extract(zip_path, extract_dir)
    loaded = LOADERS[spec.slug](extracted)
    schema = schema_package(spec, zip_path, loaded)
    protocol_baselines = run_baselines(loaded["x_train"], loaded["y_train"], loaded["x_test"], loaded["y_test"])
    random = random_challenger(loaded, SEED)
    stress = metric_stress(loaded, protocol_baselines, random["baselines"])
    protocol_delta = {
        "logisticMacroF1DeltaRandomMinusProtocol": random["baselines"]["logistic_regression"]["macroF1"]
        - protocol_baselines["logistic_regression"]["macroF1"],
        "randomForestMacroF1DeltaRandomMinusProtocol": random["baselines"]["random_forest"]["macroF1"]
        - protocol_baselines["random_forest"]["macroF1"],
        "logisticAccuracyDeltaRandomMinusProtocol": random["baselines"]["logistic_regression"]["accuracy"]
        - protocol_baselines["logistic_regression"]["accuracy"],
    }
    return rounded(
        {
            "slug": spec.slug,
            "name": spec.name,
            "sourceUrl": spec.source_url,
            "documentationUrl": spec.documentation_url,
            "protocolSignal": spec.protocol_signal,
            "expectedRisk": spec.expected_risk,
            "loaded": True,
            "protocolStatus": "protocol_reproduced",
            "officialSplit": {
                "trainRows": int(loaded["x_train"].shape[0]),
                "testRows": int(loaded["x_test"].shape[0]),
                "featureCount": int(loaded["x_train"].shape[1]),
                "classCount": int(pd.concat([loaded["y_train"], loaded["y_test"]]).nunique()),
                "protocolMetadata": loaded["protocol_metadata"],
                "baselines": protocol_baselines,
            },
            "randomChallenger": random,
            "protocolVsRandom": protocol_delta,
            "schemaProvenance": schema,
            "metricStress": stress,
            "splitRiskFinding": split_risk_finding(spec.slug, protocol_delta, stress),
        }
    )


def split_risk_finding(slug: str, delta: dict[str, float], stress: dict[str, Any]) -> dict[str, Any]:
    logistic_delta = delta["logisticMacroF1DeltaRandomMinusProtocol"]
    random_diff = abs(logistic_delta)
    if random_diff > 0.02:
        status = "material_protocol_difference"
    elif random_diff > 0.005:
        status = "small_protocol_difference"
    else:
        status = "no_material_protocol_difference_detected"
    notes = []
    if stress["flags"]["shuffledControlSuspicious"]:
        notes.append("shuffled-label control was higher than expected; interpret with caution")
    if stress["flags"]["accuracyCouldHideClassFailure"]:
        notes.append("accuracy and macro-F1 diverge enough to require class-risk reporting")
    if slug == "uci-human-activity-recognition-smartphones":
        notes.append("source split preserves subject holdout; random split mixes the source subject boundary")
    return rounded({"status": status, "logisticMacroF1RandomMinusProtocol": logistic_delta, "notes": notes})


def run_analysis(output_dir: Path, data_dir: Path, extract_dir: Path, replay_only: bool = False) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    targets = []
    failures = []
    for spec in TARGETS:
        try:
            target = analyze_target(spec, data_dir, extract_dir)
            targets.append(target)
            (output_dir / f"{spec.slug}-analysis.json").write_text(json.dumps(target, indent=2, sort_keys=True) + "\n")
            (output_dir / f"{spec.slug}-schema-tool.json").write_text(
                json.dumps(target["schemaProvenance"], indent=2, sort_keys=True) + "\n"
            )
            (output_dir / f"{spec.slug}-metric-tool.json").write_text(
                json.dumps(target["metricStress"], indent=2, sort_keys=True) + "\n"
            )
        except Exception as exc:  # noqa: BLE001 - failure evidence is part of the research result.
            failures.append({"slug": spec.slug, "errorType": type(exc).__name__, "error": str(exc)})
    if replay_only:
        summary = {
            "mode": "replay_only",
            "networkReachability": network_reachability_probe(),
            "targetsLoaded": len(targets),
            "targetReplaySummary": [
                {
                    "slug": target["slug"],
                    "protocolLogisticMacroF1": target["officialSplit"]["baselines"]["logistic_regression"]["macroF1"],
                    "randomLogisticMacroF1": target["randomChallenger"]["baselines"]["logistic_regression"]["macroF1"],
                    "splitRiskStatus": target["splitRiskFinding"]["status"],
                }
                for target in targets
            ],
            "failures": failures,
        }
        (output_dir / "replay-output.json").write_text(json.dumps(rounded(summary), indent=2, sort_keys=True) + "\n")
        return rounded(summary)
    aggregate = {
        "program": "Protocol-First Benchmark Validation and Split-Risk Program",
        "batch": "Batch 13 / Week 1",
        "resultKind": "protocol_first_benchmark_validation_week1",
        "selectedTargets": [target["slug"] for target in targets],
        "loadedTargetCount": len(targets),
        "failedTargetCount": len(failures),
        "protocolAttempts": [
            {
                "slug": target["slug"],
                "status": target["protocolStatus"],
                "signal": target["protocolSignal"],
            }
            for target in targets
        ],
        "randomChallengerCount": len(targets),
        "baselineComparisonCount": len(targets),
        "metricStressValidationCount": len(targets),
        "schemaPackagingCount": len(targets),
        "splitRiskFindings": {target["slug"]: target["splitRiskFinding"] for target in targets},
        "negativeOrPartialFindings": negative_findings(targets, failures),
        "freshSeedReplay": fresh_seed_replay(targets),
        "packageVersions": package_versions(),
        "failures": failures,
        "hardQuestionAnswer": hard_question_answer(targets),
    }
    (output_dir / "batch13-analysis.json").write_text(json.dumps(rounded(aggregate), indent=2, sort_keys=True) + "\n")
    return rounded(aggregate)


def network_reachability_probe() -> dict[str, Any]:
    try:
        urllib.request.urlopen("https://archive.ics.uci.edu/", timeout=2).close()
        return {"externalNetworkReachable": True}
    except Exception as exc:  # noqa: BLE001
        return {"externalNetworkReachable": False, "errorType": type(exc).__name__}


def fresh_seed_replay(targets: list[dict[str, Any]]) -> dict[str, Any]:
    replay = []
    for target in targets:
        seed_runs = target["metricStress"]["seedSplitSensitivity"]
        seed_42 = next(row for row in seed_runs if row["seed"] == 42)
        seed_99 = next(row for row in seed_runs if row["seed"] == 99)
        replay.append(
            {
                "slug": target["slug"],
                "replayType": "fresh_seed_stratified_random_split",
                "baselineSeed": 42,
                "freshSeed": 99,
                "baselineLogisticMacroF1": seed_42["logisticMacroF1"],
                "freshSeedLogisticMacroF1": seed_99["logisticMacroF1"],
                "macroF1DeltaFreshMinusBaseline": seed_99["logisticMacroF1"] - seed_42["logisticMacroF1"],
            }
        )
    return rounded({"attempted": bool(replay), "count": len(replay), "results": replay})


def negative_findings(targets: list[dict[str, Any]], failures: list[dict[str, Any]]) -> list[str]:
    findings = []
    if failures:
        findings.append("At least one target failed to load or execute and must not be hidden.")
    if targets:
        findings.append("No benchmark-win claim is supported; this batch only compares source split behavior against random challengers.")
    if any(target["splitRiskFinding"]["status"] == "no_material_protocol_difference_detected" for target in targets):
        findings.append("At least one source train/test protocol did not materially change the main logistic conclusion.")
    if any(target["splitRiskFinding"]["status"] == "small_protocol_difference" for target in targets):
        findings.append("At least one source train/test protocol changed the metric slightly but not enough for a strong split-risk claim.")
    if any(target["metricStress"]["flags"]["accuracyCouldHideClassFailure"] for target in targets):
        findings.append("Accuracy alone hides enough class-level variation to require macro-F1 and per-class reporting.")
    findings.append("schema_provenance_auditor remained evidence packaging; pandas exposed the same raw missingness and duplicate checks.")
    return findings


def hard_question_answer(targets: list[dict[str, Any]]) -> str:
    material = [target for target in targets if target["splitRiskFinding"]["status"] == "material_protocol_difference"]
    small = [target for target in targets if target["splitRiskFinding"]["status"] == "small_protocol_difference"]
    if material:
        return (
            "Yes, at least one source-described protocol changed Sovryn's conclusion materially versus a random "
            "challenger, so Batch 13 supports protocol-first benchmark validation."
        )
    if small:
        return (
            "Partially. The source-described train/test files changed some metrics, but Week 1 mostly found "
            "small deltas; protocol-first work is still valuable because it prevents unsupported official-reproduction claims."
        )
    return (
        "For these Week 1 targets, source-described train/test files did not materially change the main baseline "
        "conclusions, but they did convert random-split scoring into explicit protocol-risk evidence."
    )


def package_versions() -> dict[str, str]:
    return {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "scikit_learn": sklearn.__version__,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--extract-dir", type=Path, required=True)
    parser.add_argument("--replay-only", action="store_true")
    args = parser.parse_args()
    result = run_analysis(args.output_dir, args.data_dir, args.extract_dir, replay_only=args.replay_only)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
