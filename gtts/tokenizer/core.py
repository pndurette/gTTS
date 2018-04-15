# -*- coding: utf-8 -*-
import re


class RegexBuilder():
    """Repetitive alternation groups regex builder.

    A compiled regex built from the alternations (`|`) of similar groups,
    created from elements each passed into a template.

    Args:
        pattern_args (iteratable): Elements to be each passed to `pattern_func`
            to create a regex group. Each element is `re.escape`'d before being
            passed.
        pattern_func (callable): A 'template' function that should take a string
            and return a string. Each `pattern_args` will be passed down to it,
            and put together as a regex seperated by `|`.
        flags: `re` flags compiled with the regex.

    Example:
        To create a simple regex that matches on the characters `a`, `b`,
        or `c`, followed by a period::

            rb = RegexBuilder('abc', lambda x: "{}\.".format(x))

        Looking at `rb.regex` we get the following compiled regex::

            'a\.|b\.|c\.'

        The above is fairly simple, but this class can help in writing more
        complex repetitive regex, making them more readable and easier to
        create with using existing data structures.

    Example:
        To match the character following the words `lorem`, `ipsum`, `bacon`
        or `koda`::

            words = ['lorem', 'ipsum', 'bacon', 'koda']
            rb = RegexBuilder(words, lambda x: "(?<={}).".format(x))

        Looking at `rb.regex` we get the following compiled regex::

            '(?<=lorem).|(?<=ipsum).|(?<=bacon).|(?<=koda).'

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

    def __repr__(self):
        return self.regex


class PreProcessorRegex():
    """Regex-based substitution text pre-processor.

    A series of similar regex-based substitutions that share the same
    replacement. Similarly to :ref:`RegexBuiler`, each substitution is generated
    by passing elements in a template.

    Args:
        search_args (iteratable): Elements to be each passed to `search_func`
            to create a regex sub, along with replacement `repl`. Each element
            is `re.escape`'d before being passed.
        search_func (callable): A 'template' function that should take a string
            and return a string. Each `search_args` will be passed down to it,
            and along with replacement `repl`, used for `re.sub`.
        repl: the common replacement for each of the `re.sub`s.
        flags: `re` flags compiled with each substitution regex.

    Example:
        Add `!` after each the words `lorem` or `ipsum`, while ignoring case::

            import re
            words = ['lorem', 'ipsum']
            pp = PreProcessorRegex(words, lambda x: "({}).".format(x), r'\1!',
                                   re.IGNORECASE)

        In this case, the regex is a group and the replacement uses its
        backreference `\1`. Looking at `pp` we get the following list of
        regex/replacement pairs::

            (re.compile('(lorem)', re.IGNORECASE), repl='\1!'),
            (re.compile('(ipsum)', re.IGNORECASE), repl='\1!')

        It can then be run on any string of text::

            pp.run("LOREM ipSuM")
            "LOREM! ipSuM!"

    """

    def __init__(self, search_args, search_func, repl, flags=0):
        self.repl = repl

        # Create regex list
        self.regexes = []
        for arg in search_args:
            rb = RegexBuilder([arg], search_func, flags)
            self.regexes.append(rb.regex)

    def run(self, text):
        """Run each regex substitution on `text`.

        Args:
            text (string): the input text.

        Returns:
            string: the text after all of the substitution have been applied,
                one at a time.

        """
        for regex in self.regexes:
            text = regex.sub(self.repl, text)
        return text

    def __repr__(self):
        subs_strs = []
        for r in self.regexes:
            subs_strs.append("({}, repl='{}')".format(r, self.repl))
        return ", ".join(subs_strs)


class PreProcessorSub():
    """Simple substitution text pre-processor.

    Performs string-for-string substitution from list a search/replace pairs.
    It abstracts :ref:`PreProcessorRegex` for simple substitution.

    Args:
        sub_pairs (list): A list of truples of the style `(<search>, <replace>)`
        ignore_case (bool): Ignore case during search. Default is True.

    Example:
        Replace all occurences of `Mac` to `PC` and 'Firefox` to 'Chrome`::

            sub_pairs = [('Mac', 'PC'), ('Firefox', 'Chrome')]
            pp = PreProcessorSub(sub_pairs)

        Looking at the `pp`, we get the following list of
        search/replacement pairs::

            (re.compile('Mac', re.IGNORECASE), repl='PC'),
            (re.compile('Firefox', re.IGNORECASE), repl='Chrome')

        It can then be run on any string of text::

            pp.run("I use firefox on my mac")
            "I use Chrome on my PC"

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
        """Run each substitution on `text`.

        Args:
            text (string): the input text.

        Returns:
            string: the text after all of the substitution have been applied,
                one at a time.

        """
        for pp in self.pre_processors:
            text = pp.run(text)
        return text

    def __repr__(self):
        return ", ".join([str(pp) for pp in self.pre_processors])


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
