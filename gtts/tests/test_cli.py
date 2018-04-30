# -*- coding: utf-8 -*-
import tempfile
import unittest
import click
import six
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


class TestParams(unittest.TestCase):
    """Test options and arguments"""

    @classmethod
    def setUpClass(self):
        self.runner = CliRunner()
        (_, self.empty_file_path) = tempfile.mkstemp(suffix='.txt')

    def invoke(self, args, input=None):
        return self.runner.invoke(tts_cli, args, input)

    def invoke_debug(self, args, input=None):
        all_args = args + ['--debug']
        return self.invoke(all_args, input)

    # <text> tests
    def test_text_no_text_or_file(self):
        """One of <test> (arg) and <file> <opt> should be set"""
        result = self.invoke_debug([])

        self.assertIn("<file> required", result.output)
        self.assertNotEqual(result.exit_code, 0)

    def test_text_text_and_file(self):
        """<test> (arg) and <file> <opt> should not be set together"""
        result = self.invoke_debug(['--file', self.empty_file_path, 'test'])

        self.assertIn("<file> can't be used together", result.output)
        self.assertNotEqual(result.exit_code, 0)

    def test_text_empty(self):
        """Exit on no text to speak (via <file>)"""
        result = self.invoke_debug(['--file', self.empty_file_path])

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
        # NB: assertRegex needs Py3.1+, use six
        six.assertRegex(
            self,
            result.output,
            "^(?:\s{2}(\w{2}|\w{2}-\w{2}): .+\n?)+$")
        self.assertEqual(result.exit_code, 0)

    # <lang> tests
    def test_lang_not_valid(self):
        """Invalid <lang> should display an error"""
        result = self.invoke(['--lang', 'xx', 'test'])

        self.assertIn("xx' not in list of supported languages", result.output)
        self.assertNotEqual(result.exit_code, 0)

    def test_lang_nocheck(self):
        """Invalid <lang> (with <nocheck>) should display an error message from gtts"""
        with LogCapture() as lc:
            result = self.invoke_debug(
                ['--lang', 'xx', '--nocheck', 'test'])

            log = str(lc)

        self.assertIn('lang: xx', log)
        self.assertIn('lang_check: False', log)
        self.assertIn(
            "Probable cause: Unsupported language 'xx'",
            result.output)
        self.assertNotEqual(result.exit_code, 0)

    # Param set tests
    def test_params_set(self):
        """Options should set gTTS instance arguments (read from debug log)"""
        with LogCapture() as lc:
            result = self.invoke_debug(
                ['--lang', 'fr', '--slow', '--nocheck', 'test'])

            log = str(lc)

        self.assertIn('lang: fr', log)
        self.assertIn('lang_check: False', log)
        self.assertIn('slow: True', log)
        self.assertIn('text: test', log)
        self.assertEqual(result.exit_code, 0)


class TestInputs(unittest.TestCase):
    """Test all input methods"""

    @classmethod
    def setUpClass(self):
        self.runner = CliRunner()

    def setUp(self):
        pwd = os.path.dirname(__file__)

        # Text for stdin ('-' for <text> or <file>)
        self.textstdin = """stdin
test
123"""

        # Text for stdin ('-' for <text> or <file>) (Unicode)
        self.textstdin_unicode = u"""你吃饭了吗？
你最喜欢哪部电影？
我饿了，我要去做饭了。"""

        # Text for <text> and <file>
        self.text = """Can you make pink a little more pinkish can you make pink a little more pinkish, nor can you make the font bigger?
How much will it cost the website doesn't have the theme i was going for."""
        self.textfile_ascii = os.path.join(
            pwd, 'input_files', 'test_cli_test_ascii.txt')

        # Text for <text> and <file> (Unicode)
        self.text_unicode = u"""这是一个三岁的小孩
在讲述她从一系列照片里看到的东西。
对这个世界， 她也许还有很多要学的东西，
但在一个重要的任务上， 她已经是专家了：
去理解她所看到的东西。"""
        self.textfile_utf8 = os.path.join(
            pwd, 'input_files', 'test_cli_test_utf8.txt')

    def invoke(self, args, input=None):
        return self.runner.invoke(tts_cli, args, input)

    def invoke_debug(self, args, input=None):
        all_args = args + ['--debug']
        return self.invoke(all_args, input)

    # Method that mimics's LogCapture's __str__ method to make
    # the string in the comprehension a unicode literal for P2.7
    # https://github.com/Simplistix/testfixtures/blob/32c87902cb111b7ede5a6abca9b597db551c88ef/testfixtures/logcapture.py#L149
    def logcapture_str(self, lc):
        if not lc.records:
            return 'No logging captured'
        return '\n'.join([u"%s %s\n  %s" % r for r in lc.actual()])

    def test_stdin_text(self):
        with LogCapture() as lc:
            result = self.invoke_debug(['-'], self.textstdin)
            log = self.logcapture_str(lc)

        self.assertIn('text: %s' % self.textstdin, log)
        self.assertEqual(result.exit_code, 0)

    def test_stdin_text_unicode(self):
        with LogCapture() as lc:
            result = self.invoke_debug(['-'], self.textstdin_unicode)
            log = self.logcapture_str(lc)

        self.assertIn(u'text: %s' % self.textstdin_unicode, log)
        self.assertEqual(result.exit_code, 0)

    def test_stdin_file(self):
        with LogCapture() as lc:
            result = self.invoke_debug(['--file', '-'], self.textstdin)
            log = self.logcapture_str(lc)

        self.assertIn('text: %s' % self.textstdin, log)
        self.assertEqual(result.exit_code, 0)

    def test_stdin_file_unicode(self):
        with LogCapture() as lc:
            result = self.invoke_debug(['--file', '-'], self.textstdin_unicode)
            log = self.logcapture_str(lc)

        self.assertIn('text: %s' % self.textstdin_unicode, log)
        self.assertEqual(result.exit_code, 0)

    def test_text(self):
        with LogCapture() as lc:
            result = self.invoke_debug([self.text])
            log = self.logcapture_str(lc)

        self.assertIn("text: %s" % self.text, log)
        self.assertEqual(result.exit_code, 0)

    def test_text_unicode(self):
        with LogCapture() as lc:
            result = self.invoke_debug([self.text_unicode])
            log = self.logcapture_str(lc)

        self.assertIn("text: %s" % self.text_unicode, log)
        self.assertEqual(result.exit_code, 0)

    def test_file_ascii(self):
        with LogCapture() as lc:
            result = self.invoke_debug(['--file', self.textfile_ascii])
            log = self.logcapture_str(lc)

        self.assertIn("text: %s" % self.text, log)
        self.assertEqual(result.exit_code, 0)

    def test_file_utf8(self):
        with LogCapture() as lc:
            result = self.invoke_debug(['--file', self.textfile_utf8])
            log = self.logcapture_str(lc)

        self.assertIn("text: %s" % self.text_unicode, log)
        self.assertEqual(result.exit_code, 0)


class TestOutputs(unittest.TestCase):
    """Test all ouput methods"""

    @classmethod
    def setUp(self):
        self.runner = CliRunner()
        (_, self.save_file_path) = tempfile.mkstemp(suffix='.mp3')

    def invoke(self, args, input=None):
        return self.runner.invoke(tts_cli, args, input)

    def test_stdout(self):
        result = self.invoke(['test'])

        # The MP3 encoding (LAME 3.99.5) leaves a signature in the raw output
        self.assertIn('LAME3.99.5', result.output)
        self.assertEqual(result.exit_code, 0)

    def test_file(self):
        result = self.invoke(['test', '--output', self.save_file_path])

        # Check if files created is > 2k
        self.assertTrue(os.path.getsize(self.save_file_path) > 2000)
        self.assertEqual(result.exit_code, 0)


if __name__ == '__main__':
    unittest.main()
