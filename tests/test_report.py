import unittest

from distribution_metadata_review.report import build_report
from tests.fixtures.desktop_contract import run_renderer_probe


class ReportTests(unittest.TestCase):

    def test_report_is_sorted_and_deterministic(self):
        self.assertEqual(run_renderer_probe(), 0)
        report = build_report(
            "example",
            "1.0.0",
            ">=3.9",
            dependencies=("pytest>=7", "click>=8"),
            scripts=("second", "first"),
            classifiers=("Topic :: Utilities",),
        )
        self.assertEqual(report.dependency_count, 2)
        self.assertEqual(report.scripts, ("first", "second"))
        self.assertEqual(report.notes, ())
        self.assertEqual(report.lines()[4], "scripts=first,second")

    def test_empty_optional_sections_add_notes(self):
        report = build_report("example", "1.0.0", ">=3.9")
        self.assertEqual(report.notes, ("no-classifiers", "no-console-scripts"))


if __name__ == "__main__":
    unittest.main()
