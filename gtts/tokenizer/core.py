# -*- coding: utf-8 -*-
import re


class RegexBuilder():
    """
    A RegexBuilder
    """

    def __init__(self, pattern_args, pattern_func, flags=0):
        self.pattern_args = pattern_args
        self.pattern_func = pattern_func
        self.flags = flags

        # Compile
        self.regex = self._compile()

    def _compile(self):
        alts = []
        for arg in self.pattern_args:
            arg = re.escape(arg)
            alt = self.pattern_func(arg)
            alts.append(alt)

        pattern = '|'.join(alts)
        return re.compile(pattern, self.flags)


class PreProcessorRegex():
    """
    A PreProcessor
    """

    def __init__(self, search_args, search_func, repl, flags=0):
        self.repl = repl

        # Create regex list
        self.regexes = []
        for arg in search_args:
            rb = RegexBuilder([arg], search_func, flags)
            self.regexes.append(rb.regex)

    def run(self, text):
        for regex in self.regexes:
            text = regex.sub(self.repl, text)
        return text


class PreProcessorSub():
    """
    A PreProcessorSub
    """

    def __init__(self, sub_pairs, ignore_case=True):
        def search_func(x): return u"{}".format(x)
        flags = re.I if ignore_case else 0

        # Create pre-processor list
        self.pre_processors = []
        for sub_pair in sub_pairs:
            pattern, repl = sub_pair
            pp = PreProcessorRegex([pattern], search_func, repl, flags)
            self.pre_processors.append(pp)

    def run(self, text):
        for pp in self.pre_processors:
            text = pp.run(text)
        return text


class Tokenizer():
    """
    A Tokenizer
    """

    def __init__(self, regex_funcs, flags=re.IGNORECASE):
        self.regex_funcs = regex_funcs
        self.flags = flags

        try:
            # Combine
            self.total_regex = self._combine_regex()
        except (TypeError, AttributeError) as e:
            raise TypeError(
                "Tokenizer() expects a list of functions returning "
                "regular expression objects (i.e. re.compile). " +
                str(e))

    def _combine_regex(self):
        alts = []
        for func in self.regex_funcs:
            alts.append(func())

        pattern = '|'.join(alt.pattern for alt in alts)
        return re.compile(pattern, self.flags)

    def run(self, text):
        return self.total_regex.split(text)
