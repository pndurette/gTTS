# -*- coding: utf-8 -*-
import unittest
from gtts import gTTS


class TestLen(unittest.TestCase):
    """Python2/3 _len()"""

    def setUp(self):
        self.text = "Bacon ipsum dolor sit amet flank corned beef."

    def testLen(self):
        """Python2/3 _len() function"""
        tts = gTTS(text='lorem ipsum')
        self.assertEqual(tts._len(self.text), 45)


class TestLenUnicode(unittest.TestCase):
    """Python2/3 _len() with Unicode"""

    def setUp(self):
        self.text = u"但在一个重要的任务上，"

    def testLen(self):
        """Python2/3 _len() function (Unicode)"""
        tts = gTTS(text='lorem ipsum')
        self.assertEqual(tts._len(self.text), 11)


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

    def test_minimize_tokenization_len(self):
        """Same number of chars from input to output (minus spaces)"""
        tts = gTTS(self.text_long_no_punctuation, self.lang)

        input_len = tts._len(self.text_long_no_punctuation)

        output_total_len = 0
        for p in tts.text_parts:
            output_total_len += tts._len(p)
        output_total_len += (len(tts.text_parts) - 1)  # spaces between parts

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
        tts = gTTS(self.text_punctuated, self.lang)
        self.assertEqual(len(tts.text_parts), 8)

    def test_minimize_tokenization(self):
        """Tokenization on no punctuation or spaces (Unicode)"""
        tts = gTTS(self.text_long_no_punctuation_no_spaces, self.lang)
        self.assertEqual(len(tts.text_parts), 6)

    def test_minimize_tokenization_len(self):
        """Same number of Unicode chars from input to output (no punctuation or spaces)"""
        tts = gTTS(self.text_long_no_punctuation_no_spaces, self.lang)

        input_len = tts._len(self.text_long_no_punctuation_no_spaces)

        output_total_len = 0
        for p in tts.text_parts:
            output_total_len += tts._len(p)

        self.assertEqual(input_len, output_total_len)


if __name__ == '__main__':
    unittest.main()
