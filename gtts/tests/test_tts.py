import os
import tempfile
import unittest

from gtts import gTTS

LANGS = [lang for lang in gTTS.LANGUAGES.keys()]

class TestLanguages(unittest.TestCase):
    """Test all supported languages and file save"""

    def setUp(self):
        self.text = "This is a test"

    def check_lang(self, lang):
        """Create mp3 file"""
        (f, path) = tempfile.mkstemp(suffix='.mp3', prefix='test_%s_' % lang) 
        
        # Create gTTS and save
        tts = gTTS(self.text, lang)
        tts.save(path)
        
        # Check if file created is > 0
        filesize = os.path.getsize(path)
        self.assertTrue(filesize > 0)
        
        # Cleanup
        os.remove(path)

# Generate TestLanguages.check_lang tests (as TestLanguages.test_lang_<lang>) for each language
# Based on: http://stackoverflow.com/a/1194012
for l in LANGS:
    def ch(l):
        return lambda self: self.check_lang(l)
    setattr(TestLanguages, "test_lang_%s" % l, ch(l)) 

class TestInit(unittest.TestCase):
    """Test gTTS init"""

    def test_unsupported_language(self):
        """Raise Exception on unsupported language"""
        lang = 'xx'
        text = "Lorem ipsum"
        self.assertRaises(Exception, gTTS, text, lang)

    def test_empty_string(self):
        """Raise Exception on empty string"""
        lang = 'en'
        text = ""
        self.assertRaises(Exception, gTTS, text, lang)

class TestTokenizer(unittest.TestCase):
    """Tokenization when text is longer than what is allowed (MAX_CHARS)"""

    def setUp(self):
        self.lang = 'en'
        self.text_punctuated = "Hello, are you there? Bacon ipsum dolor sit amet flank corned beef shankle bacon beef belly turducken!"
        self.text_long_no_punctuation = "Bacon ipsum dolor sit amet flank corned beef shankle bacon beef ribs biltong ribeye short ribs brisket ham turducken beef tongue landjaeger porchetta sirloin brisket turkey landjaeger turducken pancetta meatloaf pastrami venison shank strip steak ham porchetta ground round ham hock hamburger"

    def test_punctuation_tokenization(self):
        """Tokenization on punctuation"""
        tts = gTTS(self.text_punctuated, self.lang)
        self.assertEqual(len(tts.text_parts), 3)

    def test_minimize_tokenization(self):
        """Tokenization on spaces"""
        tts = gTTS(self.text_long_no_punctuation, self.lang)
        self.assertEqual(len(tts.text_parts), 3)

if __name__ == '__main__':
    unittest.main()
