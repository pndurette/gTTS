# -*- coding: utf-8 -*-
import unittest
from mock import patch

from gtts.lang import tts_langs, _fetch_langs, _extra_langs


class TestLanguages(unittest.TestCase):
    """Test language list downloading"""

    def test_fetch_langs(self):
        """Fetch languages successfully"""
        # Downloaded Languages
        # Safe to assume 'en' (english) will always be there
        scraped_langs = _fetch_langs()
        self.assertTrue('en' in scraped_langs)

        # Scraping garbage
        self.assertFalse('Detect language' in scraped_langs)
        self.assertFalse('—' in scraped_langs)

        # Add-in Languages
        all_langs = tts_langs()
        extra_langs = _extra_langs()
        self.assertEqual(
            len(all_langs),
            len(scraped_langs) +
            len(extra_langs))

    @patch("gtts.lang.URL_BASE", "http://abc.def.hij.dghj")
    def test_fetch_langs_exception(self):
        """Raise RuntimeError on language fetch exception"""
        with self.assertRaises(RuntimeError):
            tts_langs()


if __name__ == '__main__':
    unittest.main()
