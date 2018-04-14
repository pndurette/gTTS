# -*- coding: utf-8 -*-
import unittest
from gtts.utils import _minimize, _len, _clean_tokens


class TestMinimize(unittest.TestCase):
    def setUp(self):
        self.delim = ' '
        self.max = 10

    def test_ascii(self):
        _in = "Bacon ipsum dolor sit amet"
        _out = ["Bacon", "ipsum", "dolor sit", "amet"]
        self.assertEqual(_minimize(_in, self.delim, self.max), _out)

    def test_ascii_no_delim(self):
        _in = "Baconipsumdolorsitametflankcornedbee"
        _out = ["Baconipsum", "dolorsitam", "etflankcor", "nedbee"]
        self.assertEqual(_minimize(_in, self.delim, self.max), _out)

    def test_unicode(self):
        _in = u"这是一个三岁的小孩在讲述他从一系列照片里看到的东西。"
        _out = [u"这是一个三岁的小孩在", u"讲述他从一系列照片里", u"看到的东西。"]
        self.assertEqual(_minimize(_in, self.delim, self.max), _out)

    def test_startwith_delim(self):
        _in = self.delim + "test"
        _out = ["test"]
        self.assertEqual(_minimize(_in, self.delim, self.max), _out)


class TestLen(unittest.TestCase):
    def test_ascii(self):
        text = "Bacon ipsum dolor sit amet flank corned beef."
        self.assertEqual(_len(text), 45)

    def test_unicode(self):
        text = u"但在一个重要的任务上"
        self.assertEqual(_len(text), 10)


class TestCleanToken(unittest.TestCase):
    def test_only_space_and_punc(self):
        _in = [",(:)?", "\t    ", "\n"]
        _out = []
        self.assertEqual(_clean_tokens(_in), _out)

    def test_strip(self):
        _in = [" Bacon  ", "& ", "ipsum\r", "."]
        _out = ["Bacon", "&", "ipsum"]
        self.assertEqual(_clean_tokens(_in), _out)


if __name__ == '__main__':
    unittest.main()
