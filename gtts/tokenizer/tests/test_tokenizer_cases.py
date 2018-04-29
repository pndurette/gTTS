# -*- coding: utf-8 -*-
import unittest
import re
from gtts.tokenizer.tokenizer_cases import tone_marks, period_comma, other_punctuation, legacy_all_punctuation
from gtts.tokenizer import symbols


class TestPreTokenizerCases(unittest.TestCase):
    def test_tone_marks(self):
        _out = re.compile('(?<=\?).|(?<=\!).|(?<=\？).|(?<=\！).')
        self.assertEqual(tone_marks(), _out)

    def test_period_comma(self):
        _out = re.compile('(?<!\.[a-z])\. |(?<!\.[a-z])\, ')
        self.assertEqual(period_comma(), _out)

    def test_other_punctuation(self):
        # String of the unique 'other punctuations'
        other_punc_str = ''.join(
            set(symbols.ALL_PUNC) -
            set(symbols.TONE_MARKS) -
            set(symbols.PERIOD_COMMA))

        # Regex pattern of the other_punctuation()'s regex
        pattern = other_punctuation().pattern

        # Assert that the pattern given by other_punctuation()
        # can split other_punc_str and they're equal in length
        # (number of tokens, number of punctuation marks + 1)
        self.assertEqual(len(re.split(pattern, other_punc_str)),
                         len(other_punc_str) + 1)

    def test_legacy_all_punctuation(self):
        # Regex pattern of the legacy_all_punctuation()'s regex
        pattern = legacy_all_punctuation().pattern

        # Assert that the pattern given by legacy_all_punctuation()
        # can split symbols.ALL_PUNC and they're equal in length
        # (number of tokens, number of punctuation marks + 1)
        self.assertEqual(len(re.split(pattern, symbols.ALL_PUNC)),
                         len(symbols.ALL_PUNC) + 1)


if __name__ == '__main__':
    unittest.main()
