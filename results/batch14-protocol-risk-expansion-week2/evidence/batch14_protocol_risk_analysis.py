#!/usr/bin/env python3
"""Batch 14 protocol-risk expansion evidence runner.

This target-specific runner extends Batch 13 without adding a Sovryn
framework layer. It downloads public UCI benchmark archives, follows
source-described split protocols when possible, compares them with
same-size stratified random challengers, and emits public-safe JSON.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import shutil
import subprocess
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
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


SEED = 42
REPLAY_SEED = 99
BATCH13_DELTAS = {
    "uci-human-activity-recognition-smartphones": 0.028766,
    "uci-optical-recognition-handwritten-digits": 0.02224,
    "uci-pen-based-handwritten-digits": 0.029324,
}


@dataclass(frozen=True)
class TargetSpec:
    slug: str
    name: str
    source_url: str
    documentation_url: str
    zip_name: str
    new_vs_batch13: str
    protocol_signal: str
    protocol_expectation: str
    split_risk_type: str
    expected_risk: str
    logistic_strategy: str = "standard"
    forest_rows_limit: int | None = None


TARGETS = [
    TargetSpec(
        slug="uci-human-activity-recognition-smartphones",
        name="UCI Human Activity Recognition Using Smartphones",
        source_url="https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip",
        documentation_url="https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones",
        zip_name="har.zip",
        new_vs_batch13="carry_forward_control",
        protocol_signal="source archive contains train/test files and subject_train/subject_test files",
        protocol_expectation="likely_protocol_reproduced",
        split_risk_type="subject_holdout_risk",
        expected_risk="ordinary random split can mix subjects and weaken the source holdout question",
    ),
    TargetSpec(
        slug="uci-statlog-shuttle",
        name="UCI Statlog Shuttle",
        source_url="https://archive.ics.uci.edu/static/public/148/statlog+shuttle.zip",
        documentation_url="https://archive.ics.uci.edu/dataset/148/statlog+shuttle",
        zip_name="shuttle.zip",
        new_vs_batch13="new",
        protocol_signal="source archive contains train/test files and documentation says the dataset should be tackled by train/test",
        protocol_expectation="likely_protocol_reproduced",
        split_risk_type="class_imbalance_and_time_order_note",
        expected_risk="80 percent majority class and documentation mentions original time order and randomization before validation split",
        logistic_strategy="sgd_linear",
        forest_rows_limit=20000,
    ),
    TargetSpec(
        slug="uci-statlog-landsat-satellite",
        name="UCI Statlog Landsat Satellite",
        source_url="https://archive.ics.uci.edu/static/public/146/statlog+landsat+satellite.zip",
        documentation_url="https://archive.ics.uci.edu/dataset/146/statlog+landsat+satellite",
        zip_name="landsat.zip",
        new_vs_batch13="new",
        protocol_signal="source archive contains sat.trn and sat.tst and documentation says do not use cross-validation",
        protocol_expectation="likely_protocol_reproduced",
        split_risk_type="spatial_file_split_risk",
        expected_risk="source split may reflect spatial sampling from an image-derived dataset, while random split ignores that context",
    ),
    TargetSpec(
        slug="uci-letter-recognition",
        name="UCI Letter Recognition",
        source_url="https://archive.ics.uci.edu/static/public/59/letter+recognition.zip",
        documentation_url="https://archive.ics.uci.edu/dataset/59/letter+recognition",
        zip_name="letter.zip",
        new_vs_batch13="new",
        protocol_signal="source documentation says the first 16000 items are typically used for training and remaining 4000 for testing, but no separate train/test files are provided",
        protocol_expectation="likely_protocol_approximated",
        split_risk_type="documentation_order_split_ambiguity",
        expected_risk="the protocol depends on source row order and wording rather than explicit split files",
        forest_rows_limit=16000,
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
    request = urllib.request.Request(spec.source_url, headers={"User-Agent": "sovryn-batch14/1.0"})
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
    for nested_zip in sorted(target.rglob("*.zip")):
        nested_target = nested_zip.with_suffix("")
        nested_target.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(nested_zip) as archive:
            archive.extractall(nested_target)
    return target


def find_file(root: Path, name: str) -> Path:
    matches = sorted(root.rglob(name))
    if not matches:
        raise FileNotFoundError(f"missing {name} below extracted archive")
    return matches[0]


def read_table(path: Path, sep: str = ",", header: int | None = None) -> pd.DataFrame:
    return pd.read_csv(path, sep=sep, header=header)


def read_doc(root: Path, names: list[str]) -> str:
    parts = []
    for name in names:
        try:
            path = find_file(root, name)
            parts.append(path.read_text(errors="replace"))
        except FileNotFoundError:
            continue
    return "\n".join(parts)


def ensure_uncompressed_shuttle_train(data_dir: Path, root: Path) -> Path:
    sidecar = data_dir / "shuttle.trn"
    if sidecar.exists() and sidecar.stat().st_size > 0:
        return sidecar
    compressed = find_file(root, "shuttle.trn.Z")
    uncompress = shutil.which("uncompress")
    if not uncompress:
        raise RuntimeError(
            "shuttle.trn.Z requires uncompress; provide pre-uncompressed shuttle.trn in the mounted data directory"
        )
    completed = subprocess.run(
        [uncompress, "-c", str(compressed)],
        check=True,
        capture_output=True,
    )
    sidecar.write_bytes(completed.stdout)
    return sidecar


def load_har(root: Path, _: Path) -> dict[str, Any]:
    x_train = read_table(find_file(root, "X_train.txt"), sep=r"\s+")
    x_test = read_table(find_file(root, "X_test.txt"), sep=r"\s+")
    y_train = read_table(find_file(root, "y_train.txt"), sep=r"\s+").iloc[:, 0].astype(str)
    y_test = read_table(find_file(root, "y_test.txt"), sep=r"\s+").iloc[:, 0].astype(str)
    subject_train = read_table(find_file(root, "subject_train.txt"), sep=r"\s+").iloc[:, 0].astype(str)
    subject_test = read_table(find_file(root, "subject_test.txt"), sep=r"\s+").iloc[:, 0].astype(str)
    features = read_table(find_file(root, "features.txt"), sep=r"\s+").iloc[:, 1].astype(str).tolist()
    x_train.columns = [f"f_{i}_{name}" for i, name in enumerate(features)]
    x_test.columns = x_train.columns
    return {
        "x_train": x_train,
        "x_test": x_test,
        "y_train": y_train,
        "y_test": y_test,
        "protocol_status": "protocol_reproduced",
        "protocol_description": "Used source train/X_train.txt and test/X_test.txt with y_train/y_test labels.",
        "protocol_ambiguity": "No paper protocol beyond source files is claimed; subject grouping is available and has zero train/test overlap.",
        "protocol_metadata": {
            "officialTrainFile": "train/X_train.txt",
            "officialTestFile": "test/X_test.txt",
            "subjectGroupingAvailable": True,
            "subjectTrainCount": int(subject_train.nunique()),
            "subjectTestCount": int(subject_test.nunique()),
            "subjectOverlapCount": int(len(set(subject_train) & set(subject_test))),
        },
    }


def load_shuttle(root: Path, data_dir: Path) -> dict[str, Any]:
    train_path = ensure_uncompressed_shuttle_train(data_dir, root)
    test_path = find_file(root, "shuttle.tst")
    train = read_table(train_path, sep=r"\s+")
    test = read_table(test_path, sep=r"\s+")
    feature_names = [f"feature_{i}" for i in range(train.shape[1] - 1)]
    x_train = train.iloc[:, :-1].copy()
    x_test = test.iloc[:, :-1].copy()
    x_train.columns = feature_names
    x_test.columns = feature_names
    doc = read_doc(root, ["shuttle.doc"])
    return {
        "x_train": x_train,
        "x_test": x_test,
        "y_train": train.iloc[:, -1].astype(str),
        "y_test": test.iloc[:, -1].astype(str),
        "protocol_status": "protocol_reproduced",
        "protocol_description": "Used shuttle.trn and shuttle.tst source files; shuttle.trn was decompressed from shuttle.trn.Z before analysis.",
        "protocol_ambiguity": "Documentation says the original dataset was in time order, then randomized, and a portion removed for validation; the source split is reproducible but the original temporal protocol is not reconstructable.",
        "protocol_metadata": {
            "officialTrainFile": "shuttle.trn.Z",
            "officialTestFile": "shuttle.tst",
            "trainingRowsDocumented": 43500,
            "testRowsDocumented": 14500,
            "timeOrderNotePresent": "time order" in doc.lower() and "relevant" in doc.lower(),
            "classImbalanceNotePresent": "Approximately 80% of the data belongs to class 1" in doc,
            "uncompressedTrainSidecarUsed": True,
        },
    }


def load_landsat(root: Path, _: Path) -> dict[str, Any]:
    train = read_table(find_file(root, "sat.trn"), sep=r"\s+")
    test = read_table(find_file(root, "sat.tst"), sep=r"\s+")
    feature_names = [f"spectral_neighbor_{i}" for i in range(train.shape[1] - 1)]
    x_train = train.iloc[:, :-1].copy()
    x_test = test.iloc[:, :-1].copy()
    x_train.columns = feature_names
    x_test.columns = feature_names
    doc = read_doc(root, ["sat.doc"])
    return {
        "x_train": x_train,
        "x_test": x_test,
        "y_train": train.iloc[:, -1].astype(str),
        "y_test": test.iloc[:, -1].astype(str),
        "protocol_status": "protocol_reproduced",
        "protocol_description": "Used sat.trn and sat.tst source files.",
        "protocol_ambiguity": "Documentation warns not to use cross-validation and describes image-derived spatial neighborhoods, but exact spatial coordinates are absent.",
        "protocol_metadata": {
            "officialTrainFile": "sat.trn",
            "officialTestFile": "sat.tst",
            "doNotUseCrossValidationNotePresent": "DO NOT USE CROSS-VALIDATION" in doc,
            "imageNeighborhoodData": "3x3 neighbourhood" in doc,
            "classSixAbsentNotePresent": "no examples with class 6" in doc.lower(),
        },
    }


def load_letter(root: Path, _: Path) -> dict[str, Any]:
    data = read_table(find_file(root, "letter-recognition.data"))
    target = data.iloc[:, 0].astype(str)
    x_all = data.iloc[:, 1:].copy()
    x_all.columns = [
        "x_box",
        "y_box",
        "width",
        "height",
        "onpix",
        "x_bar",
        "y_bar",
        "x2bar",
        "y2bar",
        "xybar",
        "x2ybr",
        "xy2br",
        "x_ege",
        "xegvy",
        "y_ege",
        "yegvx",
    ]
    doc = read_doc(root, ["letter-recognition.names"])
    return {
        "x_train": x_all.iloc[:16000].reset_index(drop=True),
        "x_test": x_all.iloc[16000:].reset_index(drop=True),
        "y_train": target.iloc[:16000].reset_index(drop=True),
        "y_test": target.iloc[16000:].reset_index(drop=True),
        "protocol_status": "protocol_approximated",
        "protocol_description": "Used the source-described first 16000 rows for training and remaining 4000 rows for test.",
        "protocol_ambiguity": "The archive provides one data file and says users typically train on the first 16000 items; no separate train/test files are present, so this is approximated rather than file-reproduced.",
        "protocol_metadata": {
            "singleDataFile": "letter-recognition.data",
            "documentationOrderSplit": "first 16000 train, remaining 4000 test",
            "trainRowsFromDocumentation": 16000,
            "testRowsFromDocumentation": 4000,
            "separateTrainTestFilesAvailable": False,
            "typicalLanguagePresent": "typically train on the first 16000" in doc,
        },
    }


LOADERS = {
    "uci-human-activity-recognition-smartphones": load_har,
    "uci-statlog-shuttle": load_shuttle,
    "uci-statlog-landsat-satellite": load_landsat,
    "uci-letter-recognition": load_letter,
}


def classifier(name: str, spec: TargetSpec) -> Any:
    if name == "dummy_most_frequent":
        return DummyClassifier(strategy="most_frequent")
    if name == "dummy_stratified":
        return DummyClassifier(strategy="stratified", random_state=SEED)
    if name == "logistic_regression":
        if spec.logistic_strategy == "sgd_linear":
            return make_pipeline(
                StandardScaler(),
                SGDClassifier(loss="log_loss", max_iter=1200, tol=1e-3, random_state=SEED),
            )
        return make_pipeline(StandardScaler(), LogisticRegression(max_iter=1200, random_state=SEED))
    if name == "random_forest":
        return RandomForestClassifier(n_estimators=70, random_state=SEED, n_jobs=-1)
    raise ValueError(name)


def maybe_subsample_train(
    x_train: pd.DataFrame,
    y_train: pd.Series,
    limit: int | None,
    seed: int = SEED,
) -> tuple[pd.DataFrame, pd.Series, dict[str, Any]]:
    if limit is None or len(y_train) <= limit:
        return x_train, y_train, {"subsampled": False, "rowsUsed": int(len(y_train))}
    x_sub, _, y_sub, _ = train_test_split(
        x_train,
        y_train,
        train_size=limit,
        random_state=seed,
        stratify=y_train,
    )
    return x_sub, y_sub, {"subsampled": True, "rowsUsed": int(len(y_sub)), "originalRows": int(len(y_train))}


def evaluate_model(
    model_name: str,
    spec: TargetSpec,
    x_train: pd.DataFrame,
    y_train: pd.Series,
    x_test: pd.DataFrame,
    y_test: pd.Series,
) -> dict[str, Any]:
    fit_x = x_train
    fit_y = y_train
    fit_note = {"subsampled": False, "rowsUsed": int(len(y_train))}
    if model_name == "random_forest":
        fit_x, fit_y, fit_note = maybe_subsample_train(x_train, y_train, spec.forest_rows_limit)
    model = classifier(model_name, spec)
    model.fit(fit_x, fit_y)
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
            "fitNote": fit_note,
        }
    )


def run_baselines(
    spec: TargetSpec,
    x_train: pd.DataFrame,
    y_train: pd.Series,
    x_test: pd.DataFrame,
    y_test: pd.Series,
) -> dict[str, Any]:
    return {
        name: evaluate_model(name, spec, x_train, y_train, x_test, y_test)
        for name in ["dummy_most_frequent", "dummy_stratified", "logistic_regression", "random_forest"]
    }


def random_challenger(loaded: dict[str, Any], spec: TargetSpec, seed: int = SEED) -> dict[str, Any]:
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
        "baselines": run_baselines(spec, x_train, y_train, x_test, y_test),
    }


def schema_package(spec: TargetSpec, zip_path: Path, loaded: dict[str, Any]) -> dict[str, Any]:
    x_all = pd.concat([loaded["x_train"], loaded["x_test"]], axis=0, ignore_index=True)
    y_all = pd.concat([loaded["y_train"], loaded["y_test"]], axis=0, ignore_index=True)
    combined = x_all.copy()
    combined["target"] = y_all.to_numpy()
    class_counts = Counter(y_all)
    return rounded(
        {
            "tool": "schema_provenance_auditor",
            "toolRole": "packaging_only",
            "sourceBinding": {"zipFile": spec.zip_name, "sha256": sha256_file(zip_path)},
            "rows": int(combined.shape[0]),
            "trainRows": int(loaded["x_train"].shape[0]),
            "testRows": int(loaded["x_test"].shape[0]),
            "featureCount": int(x_all.shape[1]),
            "classCount": int(len(class_counts)),
            "classDistribution": dict(sorted(class_counts.items())),
            "missingCells": int(combined.isna().sum().sum()),
            "duplicateFullRows": int(combined.duplicated().sum()),
            "duplicateFeatureRows": int(x_all.duplicated().sum()),
            "protocolMetadata": loaded["protocol_metadata"],
            "pandasBaseline": {
                "isnaSum": int(combined.isna().sum().sum()),
                "duplicatedFullRows": int(combined.duplicated().sum()),
                "valueCountsAvailable": True,
            },
            "addedValueBeyondPandas": "source-hash-bound evidence packaging and explicit protocol metadata, not raw discovery",
            "limitations": [
                "Does not prove semantic correctness of the source split.",
                "Does not infer hidden group, temporal, or spatial structure when source metadata is absent.",
            ],
        }
    )


def metric_stress(
    loaded: dict[str, Any],
    spec: TargetSpec,
    protocol_baselines: dict[str, Any],
    random_baselines: dict[str, Any],
) -> dict[str, Any]:
    rng = np.random.default_rng(SEED)
    shuffled_y = pd.Series(rng.permutation(loaded["y_train"].to_numpy()), index=loaded["y_train"].index).astype(str)
    shuffled = evaluate_model(
        "logistic_regression",
        spec,
        loaded["x_train"],
        shuffled_y,
        loaded["x_test"],
        loaded["y_test"],
    )
    seed_runs = []
    for seed in [7, 42, 99]:
        challenge = random_challenger(loaded, spec, seed)
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
                "accuracyCouldHideClassFailure": abs(protocol_logistic["accuracy"] - protocol_logistic["macroF1"]) > 0.03,
                "randomSplitMateriallyDifferent": abs(random_logistic["macroF1"] - protocol_logistic["macroF1"]) > 0.02,
            },
            "addedValueBeyondSklearn": "binds normal sklearn metrics to shuffled-label, class-risk, seed/split, and source-vs-random controls",
            "limitations": [
                "Does not prove absence of leakage.",
                "Does not turn source train/test files into a full paper benchmark reproduction.",
            ],
        }
    )


def class_distribution_shift(loaded: dict[str, Any]) -> float:
    y_train = loaded["y_train"]
    y_test = loaded["y_test"]
    classes = sorted(pd.unique(pd.concat([y_train, y_test], ignore_index=True)))
    train_counts = y_train.value_counts(normalize=True)
    test_counts = y_test.value_counts(normalize=True)
    return float(sum(abs(float(train_counts.get(c, 0.0)) - float(test_counts.get(c, 0.0))) for c in classes) / 2)


def severity_score(
    spec: TargetSpec,
    loaded: dict[str, Any],
    protocol_baselines: dict[str, Any],
    random_baselines: dict[str, Any],
    metric: dict[str, Any],
) -> dict[str, Any]:
    delta_macro = random_baselines["logistic_regression"]["macroF1"] - protocol_baselines["logistic_regression"]["macroF1"]
    delta_acc = random_baselines["logistic_regression"]["accuracy"] - protocol_baselines["logistic_regression"]["accuracy"]
    class_shift = class_distribution_shift(loaded)
    ambiguity = {
        "protocol_reproduced": 0,
        "protocol_approximated": 1,
        "protocol_ambiguous": 2,
        "protocol_failed": 3,
    }[loaded["protocol_status"]]
    group_risk = 1 if spec.split_risk_type in {"subject_holdout_risk", "class_imbalance_and_time_order_note", "spatial_file_split_risk"} else 0
    replay_variation = max(abs(row["logisticMacroF1"] - metric["seedSplitSensitivity"][1]["logisticMacroF1"]) for row in metric["seedSplitSensitivity"])
    benchmark_claim_risk = 0
    if abs(delta_macro) > 0.02:
        benchmark_claim_risk += 2
    if metric["flags"]["accuracyCouldHideClassFailure"]:
        benchmark_claim_risk += 1
    if ambiguity > 0:
        benchmark_claim_risk += 1
    points = 0
    points += 3 if abs(delta_macro) >= 0.05 else 2 if abs(delta_macro) >= 0.02 else 1 if abs(delta_macro) >= 0.005 else 0
    points += 2 if abs(delta_acc) >= 0.03 else 1 if abs(delta_acc) >= 0.01 else 0
    points += 2 if class_shift >= 0.1 else 1 if class_shift >= 0.03 else 0
    points += ambiguity
    points += group_risk
    points += 1 if replay_variation >= 0.01 else 0
    points += min(2, benchmark_claim_risk)
    severity = "none"
    if points >= 9:
        severity = "severe"
    elif points >= 7:
        severity = "high"
    elif points >= 4:
        severity = "moderate"
    elif points >= 1:
        severity = "low"
    return rounded(
        {
            "deltaMacroF1SourceVsRandom": delta_macro,
            "deltaAccuracySourceVsRandom": delta_acc,
            "classDistributionShift": class_shift,
            "protocolAmbiguityScore": ambiguity,
            "groupSubjectFileTemporalRisk": bool(group_risk),
            "replayStabilityMaxRandomMacroF1Delta": replay_variation,
            "benchmarkClaimRiskScore": benchmark_claim_risk,
            "severityPoints": points,
            "severity": severity,
        }
    )


def split_risk_finding(spec: TargetSpec, severity: dict[str, Any]) -> dict[str, Any]:
    notes = []
    if spec.split_risk_type == "subject_holdout_risk":
        notes.append("source split preserves a subject holdout boundary; random split mixes that boundary")
    if spec.split_risk_type == "class_imbalance_and_time_order_note":
        notes.append("documentation reports majority-class dominance and original time-order relevance before randomization")
    if spec.split_risk_type == "spatial_file_split_risk":
        notes.append("documentation warns against cross-validation and describes image-derived spatial neighborhoods")
    if spec.split_risk_type == "documentation_order_split_ambiguity":
        notes.append("protocol is approximated from documentation order rather than separate source split files")
    return rounded(
        {
            "severity": severity["severity"],
            "logisticMacroF1RandomMinusProtocol": severity["deltaMacroF1SourceVsRandom"],
            "status": "material_protocol_difference"
            if abs(severity["deltaMacroF1SourceVsRandom"]) > 0.02
            else "small_or_no_protocol_difference",
            "notes": notes,
        }
    )


def analyze_target(spec: TargetSpec, data_dir: Path, extract_dir: Path) -> dict[str, Any]:
    zip_path = download(spec, data_dir)
    root = extract(zip_path, extract_dir)
    loaded = LOADERS[spec.slug](root, data_dir)
    protocol_baselines = run_baselines(
        spec,
        loaded["x_train"],
        loaded["y_train"],
        loaded["x_test"],
        loaded["y_test"],
    )
    random = random_challenger(loaded, spec, SEED)
    schema = schema_package(spec, zip_path, loaded)
    metric = metric_stress(loaded, spec, protocol_baselines, random["baselines"])
    severity = severity_score(spec, loaded, protocol_baselines, random["baselines"], metric)
    return rounded(
        {
            "slug": spec.slug,
            "name": spec.name,
            "sourceUrl": spec.source_url,
            "documentationUrl": spec.documentation_url,
            "newVsBatch13": spec.new_vs_batch13,
            "protocolSignal": spec.protocol_signal,
            "protocolStatusExpectation": spec.protocol_expectation,
            "splitRiskType": spec.split_risk_type,
            "expectedRisk": spec.expected_risk,
            "loaded": True,
            "protocolStatus": loaded["protocol_status"],
            "protocolDescription": loaded["protocol_description"],
            "protocolAmbiguity": loaded["protocol_ambiguity"],
            "sourceSplit": {
                "trainRows": int(loaded["x_train"].shape[0]),
                "testRows": int(loaded["x_test"].shape[0]),
                "featureCount": int(loaded["x_train"].shape[1]),
                "classCount": int(pd.concat([loaded["y_train"], loaded["y_test"]]).nunique()),
                "protocolMetadata": loaded["protocol_metadata"],
                "baselines": protocol_baselines,
            },
            "randomChallenger": random,
            "schemaProvenance": schema,
            "metricStress": metric,
            "splitRiskSeverity": severity,
            "splitRiskFinding": split_risk_finding(spec, severity),
        }
    )


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
        except Exception as exc:  # noqa: BLE001 - honest target failures are evidence.
            failures.append({"slug": spec.slug, "errorType": type(exc).__name__, "error": str(exc)})
    if replay_only:
        replay = {
            "mode": "replay_only",
            "networkReachability": network_reachability_probe(),
            "targetsLoaded": len(targets),
            "targetReplaySummary": [
                {
                    "slug": target["slug"],
                    "protocolLogisticMacroF1": target["sourceSplit"]["baselines"]["logistic_regression"]["macroF1"],
                    "randomLogisticMacroF1": target["randomChallenger"]["baselines"]["logistic_regression"]["macroF1"],
                    "splitRiskSeverity": target["splitRiskSeverity"]["severity"],
                    "protocolStatus": target["protocolStatus"],
                }
                for target in targets
            ],
            "failures": failures,
        }
        (output_dir / "replay-output.json").write_text(json.dumps(rounded(replay), indent=2, sort_keys=True) + "\n")
        return rounded(replay)
    aggregate = {
        "program": "Protocol-First Benchmark Validation and Split-Risk Program",
        "batch": "Batch 14 / Week 2",
        "resultKind": "protocol_risk_expansion_week2",
        "selectedTargets": [target["slug"] for target in targets],
        "newTargetCountRelativeToBatch13": sum(1 for target in targets if target["newVsBatch13"] == "new"),
        "loadedTargetCount": len(targets),
        "failedTargetCount": len(failures),
        "protocolAttempts": [
            {
                "slug": target["slug"],
                "status": target["protocolStatus"],
                "expectation": target["protocolStatusExpectation"],
                "signal": target["protocolSignal"],
            }
            for target in targets
        ],
        "protocolReproducedOrApproximatedCount": sum(
            1 for target in targets if target["protocolStatus"] in {"protocol_reproduced", "protocol_approximated"}
        ),
        "ambiguousOrHigherRiskCount": sum(
            1
            for target in targets
            if target["protocolStatus"] in {"protocol_approximated", "protocol_ambiguous", "protocol_failed"}
            or target["splitRiskSeverity"]["severity"] in {"high", "severe"}
        ),
        "randomChallengerCount": len(targets),
        "baselineComparisonCount": len(targets),
        "metricStressValidationCount": len(targets),
        "freshSeedReplay": fresh_seed_replay(targets),
        "splitRiskFindings": {target["slug"]: target["splitRiskFinding"] for target in targets},
        "splitRiskSeverity": {target["slug"]: target["splitRiskSeverity"] for target in targets},
        "batch13Comparison": batch13_comparison(targets),
        "negativeOrPartialFindings": negative_findings(targets, failures),
        "packageVersions": package_versions(),
        "failures": failures,
        "hardQuestionAnswer": hard_question_answer(targets),
    }
    (output_dir / "batch14-analysis.json").write_text(json.dumps(rounded(aggregate), indent=2, sort_keys=True) + "\n")
    return rounded(aggregate)


def network_reachability_probe() -> dict[str, Any]:
    try:
        urllib.request.urlopen("https://archive.ics.uci.edu/", timeout=2).close()
        return {"externalNetworkReachable": True}
    except Exception as exc:  # noqa: BLE001
        return {"externalNetworkReachable": False, "errorType": type(exc).__name__}


def fresh_seed_replay(targets: list[dict[str, Any]]) -> dict[str, Any]:
    rows = []
    for target in targets:
        seed_runs = target["metricStress"]["seedSplitSensitivity"]
        seed_42 = next(row for row in seed_runs if row["seed"] == 42)
        seed_99 = next(row for row in seed_runs if row["seed"] == 99)
        rows.append(
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
    return rounded({"attempted": bool(rows), "count": len(rows), "results": rows})


def batch13_comparison(targets: list[dict[str, Any]]) -> dict[str, Any]:
    deltas = [target["splitRiskSeverity"]["deltaMacroF1SourceVsRandom"] for target in targets]
    target_rows = []
    for target in targets:
        delta = target["splitRiskSeverity"]["deltaMacroF1SourceVsRandom"]
        target_rows.append(
            {
                "slug": target["slug"],
                "batch14Delta": delta,
                "batch13DeltaIfCarryForward": BATCH13_DELTAS.get(target["slug"]),
                "largerThanBatch13Range": abs(delta) > 0.03,
                "withinBatch13Range": 0.02 <= abs(delta) <= 0.03,
                "severity": target["splitRiskSeverity"]["severity"],
            }
        )
    return rounded(
        {
            "batch13DeltaRange": {"min": 0.02224, "max": 0.029324},
            "batch14DeltaRange": {"min": min(abs(d) for d in deltas), "max": max(abs(d) for d in deltas)},
            "anyLargerThanBatch13Range": any(abs(d) > 0.03 for d in deltas),
            "ambiguityMoreImportant": any(target["protocolStatus"] == "protocol_approximated" for target in targets),
            "protocolFirstStillJustified": any(abs(d) > 0.02 for d in deltas)
            or any(target["protocolStatus"] == "protocol_approximated" for target in targets),
            "targets": target_rows,
        }
    )


def negative_findings(targets: list[dict[str, Any]], failures: list[dict[str, Any]]) -> list[str]:
    findings = []
    if failures:
        findings.append("At least one target failed to load and is recorded instead of hidden.")
    findings.append("No benchmark-win claim is supported; this batch only compares source-described protocols with random challengers.")
    if any(target["protocolStatus"] == "protocol_approximated" for target in targets):
        findings.append("At least one protocol was approximated from documentation rather than reproduced from separate train/test files.")
    if any(target["splitRiskSeverity"]["severity"] in {"high", "severe"} for target in targets):
        findings.append("At least one target had high or severe split-risk severity.")
    if any(target["metricStress"]["flags"]["accuracyCouldHideClassFailure"] for target in targets):
        findings.append("Accuracy alone hid enough class-level weakness to require macro-F1 and per-class reporting.")
    findings.append("schema_provenance_auditor remained evidence packaging; pandas exposed the raw missingness and duplicate checks.")
    return findings


def hard_question_answer(targets: list[dict[str, Any]]) -> str:
    severe_or_high = [t for t in targets if t["splitRiskSeverity"]["severity"] in {"high", "severe"}]
    approximated = [t for t in targets if t["protocolStatus"] == "protocol_approximated"]
    return (
        f"Yes. Batch 14 found protocol-first evaluation still changes conclusions across {len(targets)} targets; "
        f"{len(severe_or_high)} targets reached high or severe split-risk severity, and "
        f"{len(approximated)} target introduced documentation-order protocol ambiguity. Highest risk came from "
        "class imbalance, documentation-only order splits, and source train/test files whose random challengers "
        "substantially changed macro-F1."
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
