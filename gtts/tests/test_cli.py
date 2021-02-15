# -*- coding: utf-8 -*-
import pytest
import re
import os
from click.testing import CliRunner
from gtts.cli import tts_cli


"""Test options and arguments"""


def runner(args, input=None):
    return CliRunner().invoke(tts_cli, args, input)


def runner_debug(args, input=None):
    return CliRunner().invoke(tts_cli, args + ['--debug'], input)


# <text> tests
def test_text_no_text_or_file():
    """One of <test> (arg) and <file> <opt> should be set"""
    result = runner_debug([])

    assert "<file> required" in result.output
    assert result.exit_code != 0


def test_text_text_and_file(tmp_path):
    """<test> (arg) and <file> <opt> should not be set together"""
    filename = tmp_path / 'test_and_file.txt'
    filename.touch()

    result = runner_debug(['--file', str(filename), 'test'])

    assert "<file> can't be used together" in result.output
    assert result.exit_code != 0


def test_text_empty(tmp_path):
    """Exit on no text to speak (via <file>)"""
    filename = tmp_path / 'text_empty.txt'
    filename.touch()

    result = runner_debug(['--file', str(filename)])

    assert "No text to speak" in result.output
    assert result.exit_code != 0


# <file> tests
def test_file_not_exists():
    """<file> should exist"""
    result = runner_debug(['--file', 'notexist.txt', 'test'])

    assert "No such file or directory" in result.output
    assert result.exit_code != 0


# <all> tests
@pytest.mark.net
def test_all():
    """Option <all> should return a list of languages"""
    result = runner(['--all'])

    # One or more of "  xy: name" (\n optional to match the last)
    # Ex. "<start>  xx: xxxxx\n  xx-yy: xxxxx\n  xx: xxxxx<end>"

    assert re.match(r"^(?:\s{2}(\w{2}|\w{2}-\w{2}): .+\n?)+$", result.output)
    assert result.exit_code == 0


# <lang> tests
@pytest.mark.net
def test_lang_not_valid():
    """Invalid <lang> should display an error"""
    result = runner(['--lang', 'xx', 'test'])

    assert "xx' not in list of supported languages" in result.output
    assert result.exit_code != 0


@pytest.mark.net
def test_lang_nocheck(caplog):
    """Invalid <lang> (with <nocheck>) should display an error message from gtts"""
    result = runner_debug(['--lang', 'xx', '--nocheck', 'test'])

    assert 'lang: xx' in caplog.text
    assert 'lang_check: False' in caplog.text
    assert "Unsupported language 'xx'" in result.output
    assert result.exit_code != 0


# Param set tests
@pytest.mark.net
def test_params_set(caplog):
    """Options should set gTTS instance arguments (read from debug log)"""
    result = runner_debug(['--lang', 'fr', '--tld', 'es', '--slow', '--nocheck', 'test'])

    assert 'lang: fr' in caplog.text
    assert 'tld: es' in caplog.text
    assert 'lang_check: False' in caplog.text
    assert 'slow: True' in caplog.text
    assert 'text: test' in caplog.text
    assert result.exit_code == 0


# Test all input methods
pwd = os.path.dirname(__file__)

# Text for stdin ('-' for <text> or <file>)
textstdin = """stdin
test
123"""

# Text for stdin ('-' for <text> or <file>) (Unicode)
textstdin_unicode = """你吃饭了吗？
你最喜欢哪部电影？
我饿了，我要去做饭了。"""

# Text for <text> and <file>
text = """Can you make pink a little more pinkish can you make pink a little more pinkish, nor can you make the font bigger?
How much will it cost the website doesn't have the theme i was going for."""

textfile_ascii = os.path.join(pwd, 'input_files', 'test_cli_test_ascii.txt')

# Text for <text> and <file> (Unicode)
text_unicode = """这是一个三岁的小孩
在讲述她从一系列照片里看到的东西。
对这个世界， 她也许还有很多要学的东西，
但在一个重要的任务上， 她已经是专家了：
去理解她所看到的东西。"""

textfile_utf8 = os.path.join(pwd, 'input_files', 'test_cli_test_utf8.txt')


@pytest.mark.net
def test_stdin_text(caplog):
    result = runner_debug(['-'], textstdin)

    assert 'text: %s' % textstdin in caplog.text
    assert result.exit_code == 0


@pytest.mark.net
def test_stdin_text_unicode(caplog):
    result = runner_debug(['-'], textstdin_unicode)

    assert u'text: %s' % textstdin_unicode in caplog.text
    assert result.exit_code == 0


@pytest.mark.net
def test_stdin_file(caplog):
    result = runner_debug(['--file', '-'], textstdin)

    assert 'text: %s' % textstdin in caplog.text
    assert result.exit_code == 0


@pytest.mark.net
def test_stdin_file_unicode(caplog):
    result = runner_debug(['--file', '-'], textstdin_unicode)

    assert 'text: %s' % textstdin_unicode in caplog.text
    assert result.exit_code == 0


@pytest.mark.net
def test_text(caplog):
    result = runner_debug([text])

    assert "text: %s" % text in caplog.text
    assert result.exit_code == 0


@pytest.mark.net
def test_text_unicode(caplog):
    result = runner_debug([text_unicode])

    assert "text: %s" % text_unicode in caplog.text
    assert result.exit_code == 0


@pytest.mark.net
def test_file_ascii(caplog):
    result = runner_debug(['--file', textfile_ascii])

    assert "text: %s" % text in caplog.text
    assert result.exit_code == 0


@pytest.mark.net
def test_file_utf8(caplog):
    result = runner_debug(['--file', textfile_utf8])

    assert "text: %s" % text_unicode in caplog.text
    assert result.exit_code == 0


@pytest.mark.net
def test_file(tmp_path):
    filename = tmp_path / 'out.mp3'

    result = runner(['test', '--output', str(filename)])

    # Check if files created is > 2k
    assert filename.stat().st_size > 2000
    assert result.exit_code == 0


if __name__ == '__main__':
    pytest.main(['-x', __file__])
