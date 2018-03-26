# -*- coding: utf-8 -*-
from collections import namedtuple
import re

""" PreProcessors: prepare text for tokenizing.

For each PreProcessor in PRE_PROCESSORS, tokenize() will run a
text substitution <pattern(c)> for each <c> in <chars>, replacing with <repl>.
"""
PreProcessor = namedtuple('PreProcessor', 'chars pattern repl')
PRE_PROCESSORS = [
    # Add space after either of <chars> to ensure their proper tokenization.
    PreProcessor(chars=u'?!？！', pattern=lambda x: u"(?<={})".format(x), repl=' ')
]

""" Tokenizers: build one main regex pattern to tokenize text with.

For each Tokenizer in TOKENIZERS, tokenize() will build a
regex alternation string <pattern(c)> for each <c> in <chars>.

Every alternation from TOKENIZERS are then joined together with '|'
into one pattern used to tokenize (with re.split).
"""
Tokenizer = namedtuple('Tokenizer', 'chars pattern')
TOKENIZERS = [
    # Keep tone-modifying punctuation. Match following character.
    Tokenizer(chars=u'?!？！', pattern=lambda c: u"(?<={}).".format(c)),

    # Don't cut numbers. Match except if followed by digit.
    Tokenizer(chars=u'.,', pattern=lambda c: u"{}(?!\d)".format(c)),

    # Match other punctuation.
    Tokenizer(chars=u'¡()[]¿…‥،;:—。，、：\n', pattern=lambda c: u"{}".format(c))
]

"""
# Add custom Pre-Processor (or Tokenizer)
from gtts.string import PreProcessor, PRE_PROCESSORS
pp1 = PreProcessor(chars=u'?!？！', pattern=lambda x: "(?<={})".format(x), repl=' ')
PRE_PROCESSORS.append(pp1)
"""

def tokenize(text, max_size):
    """Pre-process and tokenize <text>.
    Returns list of tokens.
    """

    # Apply each pre-processor on <text>
    for pp in PRE_PROCESSORS:
        for c in pp.chars:
            c = re.escape(c)
            text = re.sub(pp.pattern(c), pp.repl, text)

    # Build regex alternations
    alts = []
    for t in TOKENIZERS:
        for c in t.chars:
            c = re.escape(c)
            alts.append(t.pattern(c))

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

