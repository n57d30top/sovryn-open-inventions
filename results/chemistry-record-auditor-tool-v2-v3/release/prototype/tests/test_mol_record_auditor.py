import json
import unittest
from pathlib import Path

from src.mol_record_auditor import AuditError, audit_records, normalize_temperature


class MolRecordAuditorTests(unittest.TestCase):
    def load_records(self):
        return json.loads(Path("sample-input.json").read_text(encoding="utf8"))

    def test_validates_required_fields(self):
        records = self.load_records()
        output = audit_records(records)
        self.assertEqual(output["malformedRecords"], [])

    def test_rejects_missing_molecule_identifier(self):
        records = self.load_records() + [{"name": "bad", "smiles": "", "property": "boiling_point", "value": 1, "unit": "C", "source": "toy_reference_bad"}]
        output = audit_records(records)
        self.assertTrue(any("missing molecule identifier" in item["reason"] for item in output["malformedRecords"]))

    def test_rejects_invalid_unit(self):
        records = self.load_records() + [{"name": "bad", "smiles": "X", "property": "boiling_point", "value": 1, "unit": "Celsius", "source": "toy_reference_bad"}]
        output = audit_records(records)
        self.assertTrue(any("invalid unit" in item["reason"] for item in output["malformedRecords"]))

    def test_converts_celsius_to_kelvin(self):
        value, used = normalize_temperature(100, "C", "K")
        self.assertEqual(value, 373.15)
        self.assertTrue(used)

    def test_converts_kelvin_to_celsius(self):
        value, used = normalize_temperature(373.15, "K", "C")
        self.assertEqual(value, 100.0)
        self.assertTrue(used)

    def test_uses_external_package_for_unit_normalization(self):
        output = audit_records(self.load_records())
        self.assertTrue(output["externalToolEvidence"]["usedForUnitNormalization"])
        self.assertEqual(output["externalToolEvidence"]["package"], "pint")

    def compound(self, output, name):
        return next(item for item in output["compounds"] if item["compound"] == name)

    def test_groups_ethanol_equivalence_map(self):
        output = audit_records(self.load_records())
        self.assertEqual(self.compound(output, "ethanol")["recordCount"], 2)

    def test_groups_acetone_equivalence_map(self):
        output = audit_records(self.load_records())
        self.assertEqual(self.compound(output, "acetone")["recordCount"], 2)

    def test_groups_benzene_equivalence_map(self):
        output = audit_records(self.load_records())
        self.assertEqual(self.compound(output, "benzene")["recordCount"], 2)

    def test_flags_acetone_outlier(self):
        output = audit_records(self.load_records())
        self.assertTrue(any(item["compound"] == "acetone" and item["issueType"] == "suspicious_property_outlier" for item in output["datasetIssues"]))

    def test_water_consistent_after_unit_normalization(self):
        output = audit_records(self.load_records())
        self.assertTrue(self.compound(output, "water")["consistentAfterUnitNormalization"])

    def test_equivalence_map_is_low_confidence(self):
        output = audit_records(self.load_records())
        self.assertIn("equivalence_map_low_confidence", self.compound(output, "ethanol")["canonicalizationConfidence"])

    def test_writes_deterministic_output_report_and_limitations(self):
        from src.mol_record_auditor import main
        main(["sample-input.json", "sample-output.json"])
        first = Path("sample-output.json").read_text(encoding="utf8")
        main(["sample-input.json", "sample-output.json"])
        second = Path("sample-output.json").read_text(encoding="utf8")
        self.assertEqual(first, second)
        self.assertTrue(Path("AUDIT_REPORT.md").exists())
        self.assertTrue(Path("TOOL_LIMITATIONS.md").exists())


if __name__ == "__main__":
    unittest.main()
