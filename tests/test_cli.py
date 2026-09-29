import contextlib
import io
import unittest

from distribution_metadata_review.cli import main


class CliTests(unittest.TestCase):
    def test_summary_output(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main()
        self.assertEqual(status, 0)
        self.assertIn("name=distribution-metadata-review", output.getvalue())
        self.assertIn("scripts=dist-meta-review", output.getvalue())


if __name__ == "__main__":
    unittest.main()
