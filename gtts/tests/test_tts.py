# -*- coding: utf-8 -*-
import os
import tempfile
import unittest

from gtts import gTTS, gTTSError, Languages


class TestTTS(unittest.TestCase):
    """Test all supported languages and file save"""

    def setUp(self):
        self.text = "This is a test"

    def check_tts(self, lang):
        """Create mp3 files"""
        for slow in (False, True):
            with tempfile.NamedTemporaryFile(suffix='.mp3', prefix='test_{}_'.format(lang)) as f:
                # Create gTTS and save
                tts = gTTS(self.text, lang, slow=slow)
                tts.save(f.name)

                # Check if files created is > 2k
                self.assertTrue(os.path.getsize(f.name) > 2000)


def auto_langs():
    langs = Languages()._fetch_langs()
    return langs


def extra_langs():
    langs = Languages().EXTRA_LANGS
    return langs


# Generate TestTTS.check_tts tests for each language
# Based on: http://stackoverflow.com/a/1194012
for l in auto_langs():
    def ch(l):
        return lambda self: self.check_tts(l)
    setattr(TestTTS, "test_tts_auto_%s" % l, ch(l))

for l in extra_langs():
    def ch(l):
        return lambda self: self.check_tts(l)
    setattr(TestTTS, "test_tts_extra_%s" % l, ch(l))


class TestInit(unittest.TestCase):
    """Test gTTS init"""

    def test_unsupported_language_check(self):
        """Raise ValueError on unsupported language (with language check)"""
        lang = 'xx'
        text = "Lorem ipsum"
        check = True
        with self.assertRaises(ValueError):
            tts = gTTS(text=text, lang=lang, lang_check=check)

    def test_empty_string(self):
        """Raise AssertionError on empty string"""
        text = ""
        with self.assertRaises(AssertionError):
            tts = gTTS(text=text)


class TestWebRequest(unittest.TestCase):
    """Test Web Requests"""

    def setUp(self):
        self.text = "Lorem ipsum"

    def test_unsupported_language_no_check(self):
        """Raise gTTSError on unsupported language (without language check)"""
        lang = 'xx'
        check = False
        with self.assertRaises(Exception):
            path = tempfile.mkstemp()
            tts = gTTS(text=self.text, lang=lang, lang_check=check)
            tts.save(path)


if __name__ == '__main__':
    unittest.main()
