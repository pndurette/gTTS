# coding=UTF-8

import unittest

from gtts import gToken

class TestToken(unittest.TestCase):
    """Test gToken"""

    def setUp(self):
        self.tokenizer = gToken()

    def test_token(self):
        lang = 'en'
        text = 'Hello person'
        self.assertEqual('654469.1039188', self.tokenizer.calculate_token(text, seed=403409))

    def test_work_token(self):
        lang = 'en'
        token_key = 403404
        text = 'Hello person'
        seed = '+-a^+6'
        self.assertEqual(415744659, self.tokenizer._work_token(token_key, seed))

    def test_token_accentuated(self):
        lang = 'en'
        text = u'Hé'
        self.assertEqual('63792.446860', self.tokenizer.calculate_token(text, seed=403644))

    def test_token_special_char(self):
        lang = 'en'
        text = u'€Hé'
        self.assertEqual('535990.918794', self.tokenizer.calculate_token(text, seed=403644))

    def test_token_very_special_char(self):
        lang = 'en'
        text = u"◐"
        self.assertEqual('457487.54195', self.tokenizer.calculate_token(text, seed=403644))

if __name__ == '__main__':
    unittest.main()
