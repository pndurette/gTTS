# -*- coding: utf-8 -*-
from collections import namedtuple
import re


PreProcessorRule = namedtuple(
    'PreProcessorRule',
    'chars pattern_func repl')

TokenizerRule = namedtuple(
    'TokenizerRule',
    'chars pattern_func')


PRE_PROCESSOR_RULES = [
    # Because the tokenizer will split after a tone-modidfying
    # punctuation mark, make sure there's whitespace after.
    PreProcessorRule(
        chars=u'?!？！',
        pattern_func=lambda x: u"(?<={})".format(x),
        repl=' '),

    # Re-form words cut by end-of-line hyphens (remove "<hyphen><newline>").
    PreProcessorRule(
        chars=u'-',
        pattern_func=lambda x: u"{}\n".format(x),
        repl='')
]

TOKENIZER_RULES = [
    # Keep tone-modifying punctuation. Match following character.
    TokenizerRule(
        chars=u'?!？！',
        pattern_func=lambda c: u"(?<={}).".format(c)),

    # Don't cut numbers. Match except if followed by digit.
    TokenizerRule(
        chars=u'.,',
        pattern_func=lambda c: u"{}(?!\d)".format(c)),

    # Match other punctuation.
    TokenizerRule(
        chars=u'¡()[]¿…‥،;:—。，、：\n',
        pattern_func=lambda c: u"{}".format(c))
]


def _tokenize(text, max_size):
    """Pre-process and tokenize <text>.
    Returns list of tokens.
    """

    # Apply each pre-processor rule on <text>
    for pp in PRE_PROCESSOR_RULES:
        for c in pp.chars:
            c = re.escape(c)
            text = re.sub(pp.pattern_func(c), pp.repl, text)

    # Build regex alternations
    alts = []
    for t in TOKENIZER_RULES:
        for c in t.chars:
            c = re.escape(c)
            alts.append(t.pattern_func(c))

    # Build pattern and tokenize
    pattern = '|'.join(alts)
    tokens = re.split(pattern, text)

    # Clean (strip out whitespace and empty tokens)
    tokens = [t.strip() for t in tokens if t.strip()]

    # Don't minimize when <max_size> is False
    if not max_size:
        return tokens

    # Minimize tokens to ensure they're of max <max_size>
    min_tokens = []
    for t in tokens:
        min_tokens += _minimize(t, ' ', max_size)
    return min_tokens


def _minimize(the_string, delim, max_size):
    """ Recursive function that splits `the_string` in chunks
    of maximum `max_size` chars delimited by `delim`. Returns list.
    """

    # Remove <delim> from start of <the_string>
    if the_string.startswith(delim):
        the_string = the_string[len(delim):]

    if _len(the_string) > max_size:
        try:
            idx = the_string.rindex(delim, 0, max_size)
        except ValueError:
            idx = max_size
        return [the_string[:idx]] + \
            _minimize(the_string[idx:], delim, max_size)
    else:
        return [the_string]


def _len(text):
    """Get real char len of <text>, via unicode() if Python 2"""
    try:
        # Python 2
        return len(unicode(text))
    except NameError:
        # Python 3
        return len(text)
