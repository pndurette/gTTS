# -*- coding: utf-8 -*-
import unittest
from gtts.string import _len, tokenize

from gtts.tts import gTTS
MAX_CHARS = gTTS.MAX_CHARS
del gTTS

class TestLen(unittest.TestCase):
    """Python2/3 _len()"""

    def setUp(self):
        self.text = "Bacon ipsum dolor sit amet flank corned beef."

    def testLen(self):
        """Python2/3 _len() function"""
        self.assertEqual(_len(self.text), 45)


class TestLenUnicode(unittest.TestCase):
    """Python2/3 _len() with Unicode"""

    def setUp(self):
        self.text = u"但在一个重要的任务上，"

    def testLen(self):
        """Python2/3 _len() function (Unicode)"""
        self.assertEqual(_len(self.text), 11)


class TestTokenizer(unittest.TestCase):
    """Tokenization when text is longer than what is allowed (MAX_CHARS)"""

    def setUp(self):
        self.text_punctuated = "Hello, are you there? Bacon ipsum dolor sit amet flank corned beef shankle bacon beef belly turducken!"
        self.text_long_no_punctuation = "Bacon ipsum dolor sit amet flank corned beef shankle bacon beef ribs biltong ribeye short ribs brisket ham turducken beef tongue landjaeger porchetta sirloin brisket turkey landjaeger turducken pancetta meatloaf pastrami venison shank strip steak ham porchetta ground round ham hock hamburger"
        self.text_long_decimals = "1.2.3. 00.00. 1,2,3. Hello, are you there? Bacon ipsum dolor sit amet flank corned beef shankle bacon beef belly turducken!"

    def test_punctuation_tokenization(self):
        """Tokenization on punctuation"""
        tokens = tokenize(self.text_punctuated, MAX_CHARS)
        self.assertEqual(len(tokens), 3)

    def test_tone_marks(self):
        # TODO
        pass

    def test_decimals_tokenization(self):
        """Decimal numbers should not be tokenized"""
        tokens = tokenize(self.text_long_decimals, MAX_CHARS)
        self.assertEqual(len(tokens), 6)

    def test_minimize_tokenization(self):
        """Tokenization on spaces"""
        tokens = tokenize(self.text_long_no_punctuation, MAX_CHARS)
        self.assertEqual(len(tokens), 3)

    def test_minimize_tokenization_len(self):
        """Same number of chars from input to output (minus spaces)"""
        input_len = _len(self.text_long_no_punctuation)
        tokens = tokenize(self.text_long_no_punctuation, MAX_CHARS)

        output_total_len = 0
        for t in tokens:
            output_total_len += _len(t)
        output_total_len += (len(tokens) - 1)  # spaces between parts

        self.assertEqual(input_len, output_total_len)


class TestTokenizerUnicode(unittest.TestCase):
    """Tokenization of Unicode when text is longer than what is allowed (MAX_CHARS)"""

    def setUp(self):
        self.lang = 'zh-cn'
        self.text_punctuated = u"""
这是一个三岁的小孩
在讲述她从一系列照片里看到的东西。
对这个世界， 她也许还有很多要学的东西，
但在一个重要的任务上， 她已经是专家了：
去理解她所看到的东西。
我们的社会已经在科技上取得了前所未有的进步。
"""
        self.text_long_no_punctuation_no_spaces = u"""了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了她已经是专家了"""

    def test_punctuation_tokenization(self):
        """Tokenization on punctuation (Unicode)"""
        tokens = tokenize(self.text_punctuated, MAX_CHARS)
        self.assertEqual(len(tokens), 8)


    def test_minimize_tokenization(self):
        """Tokenization on no punctuation or spaces (Unicode)"""
        tokens = tokenize(self.text_long_no_punctuation_no_spaces, MAX_CHARS)
        self.assertEqual(len(tokens), 6)

    def test_minimize_tokenization_len(self):
        """Same number of Unicode chars from input to output (no punctuation or spaces)"""
        input_len = _len(self.text_long_no_punctuation_no_spaces)
        tokens = tokenize(self.text_long_no_punctuation_no_spaces, MAX_CHARS)

        output_total_len = 0
        for t in tokens:
            output_total_len += _len(t)

        self.assertEqual(input_len, output_total_len)


if __name__ == '__main__':
    unittest.main()
