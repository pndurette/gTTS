# -*- coding: utf-8 -*-
import tempfile
import unittest
import click
import sys
import os
from click.testing import CliRunner
from gtts.cli import tts_cli

# Need to look into gTTS' log output to test proper instanciation
# - Use testfixtures.LogCapture() b/c TestCase.assertLogs() needs py3.4+
# - Clear 'gtts' logger handlers (set in gtts.cli) to reduce test noise
import logging
from testfixtures import LogCapture
logger = logging.getLogger('gtts')
logger.handlers = []

# X <text> (arg) and <file> (opt) should be mutually exclusive
# X --all should print languages and exit
# X --slow calls with slow true
# X --debug calls with debug true
# X --nocheck calls with lang_check false
# X file doesn't exist
# X no text to speak
# in: stdin ('-')
# in: stdin ('-') (unicode)
# in: <text> (arg)
# in: <text> (arg) (Unicode)
# in: <file> (opt)
# in: <file> (opt) (Unicode)
# out: stdout
# out: -o (--output) file


class TestParams(unittest.TestCase):
    """Test options and arguments"""

    @classmethod
    def setUpClass(self):
        self.runner = CliRunner()
        (f, self.empty_file) = tempfile.mkstemp(suffix='.txt')

    @classmethod
    def tearDownClass(self):
        os.remove(self.empty_file)

    def invoke(self, args):
        return self.runner.invoke(tts_cli, args)

    def invoke_debug(self, args):
        all_args = args + ['--debug']
        return self.invoke(all_args)

    # <text> tests
    def test_text_no_text_or_file(self):
        """One of <test> (arg) and <file> <opt> should be set"""
        result = self.invoke_debug([])
        self.assertIn("FILENAME required", result.output)
        self.assertNotEqual(result.exit_code, 0)

    def test_text_text_and_file(self):
        """<test> (arg) and <file> <opt> should not be set together"""
        result = self.invoke_debug(['--file', self.empty_file, 'test'])
        self.assertIn("FILENAME can't be used together", result.output)
        self.assertNotEqual(result.exit_code, 0)

    def test_text_empty(self):
        """Exit on no text to speak (via <file>)"""
        result = self.invoke_debug(['--file', self.empty_file])
        self.assertIn("No text to speak", result.output)
        self.assertNotEqual(result.exit_code, 0)

    # <file> tests
    def test_file_not_exists(self):
        """<file> should exist"""
        result = self.invoke_debug(['--file', 'notexist.txt', 'test'])
        self.assertIn("No such file or directory", result.output)
        self.assertNotEqual(result.exit_code, 0)

    # <all> tests
    def test_all(self):
        """Option <all> should return a list of languages"""
        result = self.invoke(['--all'])
        # One or more of "  xy: name" (\n optional to match the last)
        # Ex. "<start>  xx: xxxxx\n  xx-yy: xxxxx\n  xx: xxxxx<end>"
        self.assertRegex(
            result.output,
            "^(?:\s{2}(\w{2}|\w{2}-\w{2}): .+\n?)+$")
        self.assertEqual(result.exit_code, 0)

    def test_lang_not_valid(self):
        """"""
        result = self.invoke(['--lang', 'xx', 'test'])
        self.assertIn("xx' not in list of supported languages", result.output)

    def test_lang_nocheck(self):
        """"""
        with LogCapture() as lc:
            result = self.invoke_debug(
                ['--lang', 'xx', '--nocheck', 'test'])

            log = str(lc)
            self.assertIn('lang: xx', log)
            self.assertIn('lang_check: False', log)

        self.assertIn("Probable cause: Unsupported language 'xx'", result.output)
        self.assertNotEqual(result.exit_code, 0)

    def test_params_set(self):
        """Options should set gTTS instance arguments (read from debug log)"""
        with LogCapture() as lc:
            result = self.invoke_debug(
                ['--lang', 'fr', '--slow', '--nocheck', '--output', '/dev/null', 'test'])

            log = str(lc)
            self.assertIn('lang: fr', log)
            self.assertIn('lang_check: False', log)
            self.assertIn('slow: True', log)
            self.assertIn('text: test', log)

        self.assertEqual(result.exit_code, 0)


class TestInputs(unittest.TestCase):
    """Test all input methods"""
    # TODO test-in

    def setUp(self):
        pass


class TestOutputs(unittest.TestCase):
    """Test all ouput methods"""
    # TODO test-out

    def setUp(self):
        pass

    def test_stdout(self):
        pass

    def test_file(self):
        pass


if __name__ == '__main__':
    unittest.main()
