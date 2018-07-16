# -*- coding: utf-8 -*-
import os
import tempfile
import unittest
from mock import Mock

from gtts.tts import gTTS, gTTSError
from gtts.lang import _fetch_langs, _extra_langs

# Testing all languages takes some time.
# Set TEST_LANGS envvar to choose languages to test.
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
        for slow in (False, True):
            with tempfile.SpooledTemporaryFile(suffix='.mp3', prefix='test_{}_'.format(lang)) as f:
                # Create gTTS and save
                tts = gTTS(self.text, lang, slow=slow)
                tts.write_to_fp(f)

                # Check if files created is > 2k
                self.assertTrue(os.fstat(f.fileno()).st_size > 2000)


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
        langs['fetch'] = _fetch_langs()
        langs['extra'] = _extra_langs()
    elif env == 'fetch':
        langs['fetch'] = _fetch_langs()
    elif env == 'extra':
        langs['extra'] = _extra_langs()
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
            gTTS(text=text, lang=lang, lang_check=check)

    def test_empty_string(self):
        """Raise AssertionError on empty string"""
        text = ""
        with self.assertRaises(AssertionError):
            gTTS(text=text)

    def test_no_text_parts(self):
        """Raises AssertionError on no content to send to API (no text_parts)"""
        text = "                                                                                                          ..,\n"
        with self.assertRaises(AssertionError):
            with tempfile.SpooledTemporaryFile() as f:
                tts = gTTS(text=text)
                tts.write_to_fp(f)


class TestWrite(unittest.TestCase):
    """Test write_to_fp()/save() cases not covered elsewhere in this file"""

    def test_bad_fp_type(self):
        """Raise TypeError if fp is not a file-like object (no .write())"""
        # Create gTTS and save
        tts = gTTS(text='test')
        with self.assertRaises(TypeError):
            tts.write_to_fp(5)

    def test_save(self):
        """Save .mp3 file successfully"""
        (_, save_file_path) = tempfile.mkstemp(suffix='.mp3')

        # Create gTTS and save
        tts = gTTS(text='test')
        tts.save(save_file_path)

        # Check if file created is > 2k
        self.assertTrue(os.stat(save_file_path).st_size > 2000)


class TestgTTSError(unittest.TestCase):
    """Test gTTsError internal exception handling"""

    def test_msg(self):
        """Set exception message successfully"""
        error1 = gTTSError('test')
        self.assertEqual('test', error1.msg)

        error2 = gTTSError()
        self.assertIsNone(error2.msg)

    def test_infer_msg(self):
        """Infer message sucessfully based on context"""

        # 403
        tts403 = Mock()
        response403 = Mock(status_code=403, reason='aaa')
        error403 = gTTSError(tts=tts403, response=response403)
        self.assertEqual(
            error403.msg,
            "403 (aaa) from TTS API. Probable cause: Bad token or upstream API changes")

        # 404 (and not lang_check)
        tts404 = Mock(lang='xx', lang_check=False)
        response404 = Mock(status_code=404, reason='bbb')
        error404 = gTTSError(tts=tts404, response=response404)
        self.assertEqual(
            error404.msg,
            "404 (bbb) from TTS API. Probable cause: Unsupported language 'xx'")

        # >= 500
        tts500 = Mock()
        response500 = Mock(status_code=500, reason='ccc')
        error500 = gTTSError(tts=tts500, response=response500)
        self.assertEqual(
            error500.msg,
            "500 (ccc) from TTS API. Probable cause: Uptream API error. Try again later.")

        # Unknown (ex. 100)
        tts100 = Mock()
        response100 = Mock(status_code=100, reason='ddd')
        error100 = gTTSError(tts=tts100, response=response100)
        self.assertEqual(
            error100.msg,
            "100 (ddd) from TTS API. Probable cause: Unknown")


class TestWebRequest(unittest.TestCase):
    """Test Web Requests"""

    def setUp(self):
        self.text = "Lorem ipsum"

    def test_unsupported_language_no_check(self):
        """Raise gTTSError on unsupported language (without language check)"""
        lang = 'xx'
        check = False
        with self.assertRaises(gTTSError):
            with tempfile.SpooledTemporaryFile() as f:
                # Create gTTS
                tts = gTTS(text=self.text, lang=lang, lang_check=check)
                tts.write_to_fp(f)


if __name__ == '__main__':
    unittest.main()
