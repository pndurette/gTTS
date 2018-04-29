# -*- coding: utf-8 -*-
import unittest
import re
from gtts.tokenizer.core import RegexBuilder, PreProcessorRegex, PreProcessorSub, Tokenizer

# Tests based on classes usage examples
# See class documentation for details


class TestRegexBuilder(unittest.TestCase):
    def test_regexbuilder(self):
        rb = RegexBuilder('abc', lambda x: "{}".format(x))
        self.assertEqual(rb.regex, re.compile('a|b|c'))


class TestPreProcessorRegex(unittest.TestCase):
    def test_preprocessorregex(self):
        pp = PreProcessorRegex('ab', lambda x: "{}".format(x), 'c')
        _out = "(re.compile('a'), repl='c'), (re.compile('b'), repl='c')"
        self.assertEqual(repr(pp), _out)


class TestPreProcessorSub(unittest.TestCase):
    def test_proprocessorsub(self):
        sub_pairs = [('Mac', 'PC'), ('Firefox', 'Chrome')]
        pp = PreProcessorSub(sub_pairs)
        _in = "I use firefox on my mac"
        _out = "I use Chrome on my PC"
        self.assertEqual(pp.run(_in), _out)


class TestTokenizer(unittest.TestCase):
    # tokenizer case 1
    def case1(self):
        return re.compile("\,")

    # tokenizer case 2
    def case2(self):
        return RegexBuilder('abc', lambda x: "{}\.".format(x)).regex

    def test_tokenizer(self):
        t = Tokenizer([self.case1, self.case2])
        _in = "Hello, my name is Linda a. Call me Lin, b. I'm your friend"
        _out = [
            'Hello',
            ' my name is Linda ',
            ' Call me Lin',
            ' ',
            " I'm your friend"]
        self.assertEqual(t.run(_in), _out)

    def test_bad_params_not_list(self):
        with self.assertRaises(TypeError):
            t = Tokenizer(self.case1)

    def test_bad_params_not_callable(self):
        with self.assertRaises(TypeError):
            t = Tokenizer([100])


if __name__ == '__main__':
    unittest.main()
