import json
import unittest
from pathlib import Path

from src.energy_record_auditor import audit, validate


class EnergyRecordAuditorTests(unittest.TestCase):
    def load_output(self):
        return json.loads(Path("sample-output.json").read_text())

    def test_timestamp_validation(self):
        with self.assertRaises(ValueError):
            validate([{"timestamp": "", "kwh": 1, "outdoorTemperatureC": 1, "season": "winter", "householdId": "toy", "source": "x"}])

    def test_duplicate_timestamp_detection(self):
        output = self.load_output()
        self.assertTrue(any(item["issueType"] == "duplicate_timestamp" for item in output["datasetIssues"]))

    def test_missing_interval_detection(self):
        output = self.load_output()
        self.assertTrue(any(item["issueType"] == "missing_interval" for item in output["datasetIssues"]))

    def test_high_usage_spike_detection(self):
        output = self.load_output()
        self.assertTrue(any(item["issueType"] == "high_usage_spike" for item in output["datasetIssues"]))

    def test_weather_normalized_anomaly_detection(self):
        output = self.load_output()
        self.assertTrue(any(item["issueType"] == "weather_normalized_anomaly" for item in output["datasetIssues"]))

    def test_weak_provenance_flag(self):
        output = self.load_output()
        self.assertTrue(any(item["issueType"] == "weak_provenance" for item in output["datasetIssues"]))

    def test_external_package_usage_recorded(self):
        output = self.load_output()
        self.assertEqual(output["externalToolEvidence"]["package"], "pandas")
        self.assertTrue(output["externalToolEvidence"]["usedForTabularValidation"])

    def test_deterministic_output_shape(self):
        output = self.load_output()
        self.assertEqual(output["kind"], "energy_record_auditor_output")
        self.assertIn("datasetReliabilityScore", output)


if __name__ == "__main__":
    unittest.main()
