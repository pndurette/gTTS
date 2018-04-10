# -*- coding: utf-8 -*-
from gtts.tokenizer import PreProcessorRegex, PreProcessorSub, symbols
import re


def tone_marks(text):
    """
    Because the tokenizer will split after a tone-modidfying
    punctuation mark, make sure there's whitespace after.
    """
    return PreProcessorRegex(
        search_args=symbols.TONE_MARKS,
        search_func=lambda x: u"(?<={})".format(x),
        repl=' ').run(text)


def end_of_line(text):
    """
    Re-form words cut by end-of-line hyphens (remove "<hyphen><newline>").
    """
    return PreProcessorRegex(
        search_args=u'-',
        search_func=lambda x: u"{}\n".format(x),
        repl='').run(text)


def abbreviations(text):
    """
    Remove periods after abbrevations that can be read without.
    TODO Caveat: Could potentially remove the ending period of a sentence.
    """
    return PreProcessorRegex(
        search_args=symbols.ABBREVIATIONS,
        search_func=lambda x: u"(?<={})(?=\.).".format(x),
        repl='', flags=re.IGNORECASE).run(text)


def word_sub(text):
    """
    Word-for-word substitutions.
    """
    return PreProcessorSub(
        sub_pairs=symbols.SUB_PAIRS).run(text)
