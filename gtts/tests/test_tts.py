# -*- coding: utf-8 -*-
import os
import tempfile
import unittest

from gtts import gTTS, gTTSError, Languages

# Testing all languages takes some time.
# Set TEST_LANGS to choose with languages to test.
#  * 'fetch': Languages fetched from the Web
#  * 'extra': Languagee set in Languages.EXTRA_LANGS
#  * 'all': All of the above
#  * <csv>: Languages tags list to test
# Unset TEST_LANGS to test everything ('all')
# See: test_langs_dict()


class TestTTS(unittest.TestCase):
    """Test all supported languages and file save"""

    def setUp(self):
        self.text = "This is a test"

    def check_tts(self, lang):
        """Create output .mp3 file successfully"""
        (f, path) = tempfile.mkstemp(suffix='.mp3', prefix='test_{}_'.format(lang))
        (f_slow, path_slow) = tempfile.mkstemp(
            suffix='.mp3', prefix='test_{}_slow'.format(lang))

        # Create gTTS (normal) and save
        tts = gTTS(self.text, lang)
        tts.save(path)

        # Create gTTS (slow) and save
        tts = gTTS(self.text, lang, slow=True)
        tts.save(path_slow)

        # Check if files created is > 2k
        filesize = os.path.getsize(path)
        filesize_slow = os.path.getsize(path_slow)
        self.assertTrue(filesize > 2000)
        self.assertTrue(filesize_slow > 2000)

        # Cleanup
        os.remove(path)
        os.remove(path_slow)


def test_langs_dict():
    """Construct a dict of suites of languages to test.
    { '<suite name>' : <list or dict of language tags> }

    ex.: { 'fetch' : {'en': 'English', 'fr': 'French'},
           'extra' : {'en': 'English', 'fr': 'French'} }
    ex.: { 'environ' : ['en', 'fr'] }
    """
    langs = dict()
    env = os.environ.get('TEST_LANGS', '')
    if env == '' or env == 'all':
        langs['fetch'] = Languages()._fetch_langs()
        langs['extra'] = Languages().EXTRA_LANGS
    elif env == 'fetch':
        langs['fetch'] = Languages()._fetch_langs()
    elif env == 'extra':
        langs['extra'] = Languages().EXTRA_LANGS
    else:
        env_langs = env.split(',')
        env_langs = [l for l in env_langs if l]
        langs['environ'] = env_langs
    return langs


# Generate TestTTS.check_tts tests for each language
# Based on: http://stackoverflow.com/a/1194012
for suite, langs in test_langs_dict().items():
    for l in langs:
        def ch(l):
            return lambda self: self.check_tts(l)
        setattr(TestTTS, "test_tts_%s_%s" % (suite, l), ch(l))


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
        """Raise ValueError on empty string"""
        text = ""
        with self.assertRaises(ValueError):
            tts = gTTS(text=text)


class TestWebRequest(unittest.TestCase):
    """Test Web Requests"""

    def setUp(self):
        self.text = "Lorem ipsum"

    def test_unsupported_language_no_check(self):
        """Raise gTTSError on unsupported language (without language check)"""
        lang = 'xx'
        check = False
        with self.assertRaises(gTTSError):
            (f, path) = tempfile.mkstemp()
            tts = gTTS(text=self.text, lang=lang, lang_check=check)
            tts.save(path)

            # Cleanup
            os.remove(path)


if __name__ == '__main__':
    unittest.main()
