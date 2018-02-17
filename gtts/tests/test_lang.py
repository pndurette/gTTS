# -*- coding: utf-8 -*-
import unittest

from gtts import Languages, LanguagesFetchError

class TestLanguages(unittest.TestCase):
    """Test language list downloading"""
    
    def setUp(self):
        pass

    def test_fetch_langs(self):
        languages = Languages()

        # Downloaded Languages
        # Safe to assume 'en' (english) will always be there
        scraped_langs = languages._fetch_langs()
        self.assertTrue('en' in scraped_langs)
        
        # Scraping garbage 
        self.assertFalse('Detect language' in scraped_langs)
        self.assertFalse('—' in scraped_langs)
        
        # Add-in Languages
        all_langs = languages.get()
        special_langs = Languages.SPECIAL_LANGS
        self.assertEqual(len(all_langs), len(scraped_langs) + len(special_langs))

    def test_fetch_langs_exception(self):
        languages = Languages()
        languages.URL_BASE = 'http://abc.def.hij.biz'
        with self.assertRaises(LanguagesFetchError):
            languages.get()

if __name__ == '__main__':
    unittest.main()
