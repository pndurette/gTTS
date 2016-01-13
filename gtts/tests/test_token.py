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

if __name__ == '__main__':
    unittest.main()
