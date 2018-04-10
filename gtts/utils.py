# -*- coding: utf-8 -*-
from string import punctuation as punc, whitespace as ws
import re

_ALL_PUNC_OR_SPACE = re.compile(u"^[{}]*$".format(re.escape(punc + ws)))


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


def _clean_tokens(tokens):
    """Filter out tokens that are all punctuation and/or whitespace.
    Strip whitespace from the rest of the tokens"""
    return [t.strip() for t in tokens if not _ALL_PUNC_OR_SPACE.match(t)]
