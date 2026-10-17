"""Protect published citation data when retrieval is incomplete or unavailable."""
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

spec = importlib.util.spec_from_file_location("scholar", Path(__file__).resolve().parents[1] / "google_scholar_crawler/main.py")
scholar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scholar)


class CitationRefreshTests(unittest.TestCase):
    def test_zero_is_valid_and_other_metrics_are_not_published(self):
        result = scholar.citation_record({"citedby": 0, "hindex": 10})
        self.assertEqual(result["citations"], 0)
        self.assertNotIn("hindex", result)

    def test_invalid_counts_are_rejected(self):
        for count in (None, "123", -1, True, 1.5):
            with self.subTest(count=count), self.assertRaises(ValueError):
                scholar.citation_record({"citedby": count})

    def test_failed_request_preserves_existing_data(self):
        with TemporaryDirectory() as directory:
            out = Path(directory) / "gs_data.json"
            original = '{"citations": 100, "updated": "2026-10-16"}'
            out.write_text(original)
            def fail():
                raise RuntimeError("blocked")
            self.assertFalse(scholar.refresh(fail, out))
            self.assertEqual(out.read_text(), original)

    def test_large_drop_does_not_replace_previous_count(self):
        with TemporaryDirectory() as directory:
            out = Path(directory) / "gs_data.json"
            out.write_text('{"citations": 100}')
            self.assertFalse(scholar.refresh(lambda: {"citedby": 1}, out))
            self.assertEqual(json.loads(out.read_text())["citations"], 100)

    def test_successful_refresh_records_count_and_profile(self):
        with TemporaryDirectory() as directory:
            out = Path(directory) / "results/gs_data.json"
            self.assertTrue(scholar.refresh(lambda: {"citedby": 123}, out))
            data = json.loads(out.read_text())
            self.assertEqual(data["citations"], 123)
            self.assertEqual(data["scholar_id"], "ZTuS-yUAAAAJ")
            self.assertRegex(data["updated"], r"^\d{4}-\d{2}-\d{2}$")
            self.assertFalse(out.with_suffix('.tmp').exists())


if __name__ == '__main__':
    unittest.main()
