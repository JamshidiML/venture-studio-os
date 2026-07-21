from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import parse_front_matter, validate_internal_links


class FrontMatterTests(unittest.TestCase):
    def test_parses_required_fields(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "artifact.md"
            path.write_text(
                "---\nstatus: draft\nversion: 0.1.0\n"
                "owner_role: Strategy Agent\nlast_reviewed: 2026-07-22\n---\n# Title\n",
                encoding="utf-8",
            )
            fields, error = parse_front_matter(path)

        self.assertIsNone(error)
        self.assertEqual(fields["status"], "draft")
        self.assertEqual(fields["owner_role"], "Strategy Agent")

    def test_reports_missing_delimiter(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "artifact.md"
            path.write_text("# Title\n", encoding="utf-8")
            fields, error = parse_front_matter(path)

        self.assertEqual(fields, {})
        self.assertEqual(error, "missing opening front-matter delimiter")


class InternalLinkTests(unittest.TestCase):
    def test_accepts_existing_and_reports_missing_relative_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            (docs / "target.md").write_text("# Target\n", encoding="utf-8")
            source = root / "source.md"
            source.write_text(
                "[Good](docs/target.md) [Bad](docs/missing.md) [Web](https://example.com)\n",
                encoding="utf-8",
            )

            errors = validate_internal_links(root)

        self.assertEqual(errors, ["source.md: broken internal link: docs/missing.md"])


if __name__ == "__main__":
    unittest.main()
