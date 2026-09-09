import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import generate_index as generator


class SampleTests(unittest.TestCase):
    def test_title_description_sorting_and_thumbnail_selection(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            sample = root / 'sample'
            sample.mkdir()
            (sample / 'b.html').touch()
            (sample / 'a.html').touch()
            (sample / 'preview.PNG').touch()
            (sample / 'design.md').write_text('# Project — Alpha (draft)\n\nSource: ref\n**Description**\nnext line\n\nignored', encoding='utf-8')
            (root / '.hidden').mkdir()
            (root / '.hidden' / 'index.html').touch()
            with patch.object(generator, 'ROOT', root):
                result = generator.find_samples()
            self.assertEqual(result, [{'slug': 'sample', 'title': 'Alpha', 'description': 'Description next line', 'html': 'a.html', 'thumbnail': 'preview.PNG', 'hasSpec': True}])

    def test_empty_root(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(generator, 'ROOT', Path(folder)):
            self.assertEqual(generator.find_samples(), [])

    def test_optional_metadata_failures_fall_back_and_log(self):
        for error in [PermissionError(), UnicodeError()]:
            with self.subTest(error=type(error).__name__), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                sample = root / 'my_sample'
                sample.mkdir()
                (sample / 'index.html').touch()
                (sample / 'design.md').touch()
                with patch.object(generator, 'ROOT', root), patch.object(generator, 'parse_design_md', side_effect=error), self.assertLogs(level='WARNING'):
                    result = generator.find_samples()[0]
                self.assertEqual(result['title'], 'My Sample')
                self.assertEqual(result['description'], '')
                self.assertIsNone(result['thumbnail'])

    def test_no_heading_and_empty_metadata(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'design.md'
            for content in ['', 'plain paragraph']:
                path.write_text(content, encoding='utf-8')
                self.assertEqual(generator.parse_design_md(path), (None, ''))


if __name__ == '__main__':
    unittest.main()
