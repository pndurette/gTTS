.. module:: gtts.tokenizer

Pre-processing and tokenizing
=============================

The :mod:`gtts.tokenizer` module powers the default pre-processing and tokenizing features of ``gTTS`` and provides tools to easily expand them. :class:`gtts.tts.gTTS` takes two arguments ``pre_processor_funcs`` (list of functions) and ``tokenizer_func`` (function). See: `Pre-processing`_, `Tokenizing`_.

.. contents:: :local:
   :depth: 2

Definitions
-----------

Pre-processor:
    Function that takes text and returns text. Its goal is to modify text (for example correcting pronounciation), and/or to prepare text for proper tokenization (for example enuring spacing after certain characters).

Tokenizer:
    Function that takes text and returns it split into a list of `tokens` (strings).
    In the ``gTTS`` context, its goal is to cut the text into smaller segments that do not exceed the maximum character size allowed for each TTS API request, while making the speech sound natural and continuous.
    It does so by splitting text where speech would naturaly pause (for example on ".") while handling where it should not (for example on "10.5" or "U.S.A."). Such rules are called `tokenizer cases`, which it takes a list of.

Tokenizer case:
    Function that defines one of the specific cases used by :class:`gtts.tokenizer.core.Tokenizer`. More specefically, it returns a ``regex`` object that describes what to look for for a particular case. :class:`gtts.tokenizer.core.Tokenizer` then creates its main `regex` pattern by joining all `tokenizer cases` with "|".


Pre-processing
--------------

You can pass a list of any function to :class:`gtts.tts.gTTS`'s ``pre_processor_funcs`` attribute to act as pre-processor (as long as it takes a string and returns a string).

By default, :class:`gtts.tts.gTTS` takes a list of the following pre-processors, applied in order::

    [
        pre_processors.tone_marks,
        pre_processors.end_of_line,
        pre_processors.abbreviations,
        pre_processors.word_sub
    ]

.. automodule:: gtts.tokenizer.pre_processors
   :members:

Customizing & Examples
~~~~~~~~~~~~~~~~~~~~~~

This module provides two classes to help build pre-processors:

* :class:`gtts.tokenizer.core.PreProcessorRegex` (for `regex`-based replacing, as would ``re.sub`` use)
* :class:`gtts.tokenizer.core.PreProcessorSub` (for word-for-word replacements).

The ``run(text)`` method of those objects returns the processed text.

Speech corrections (word substitution)
______________________________________

The default substitutions are defined by the :attr:`gtts.tokenizer.symbols.SUB_PAIRS` list. Add a custom one by appending to it:

::

    >>> from gtts.tokenizer import pre_processors
    >>> import gtts.tokenizer.symbols
    >>>
    >>> gtts.tokenizer.symbols.SUB_PAIRS.append(
    ...     ('sub.', 'submarine')
    ... )
    >>> test_text = "Have you seen the Queen's new sub.?"
    >>> pre_processors.word_sub(test_text)
    "Have you seen the Queen's new submarine?"

Abbreviations
_____________

The default abbreviations are defined by the :attr:`gtts.tokenizer.symbols.ABBREVIATIONS` list. Add a custom one to it to add a new abbreviation to remove the period from. *Note: the default list already includes an extensive list of English abbreviations that Google Translate will read even without the period.*

See :mod:`gtts.tokenizer.pre_processors` for more examples.

Tokenizing
----------

You can pass any function to :class:`gtts.tts.gTTS`'s ``tokenizer_func`` attribute to act as tokenizer (as long as it takes a string and returns a list of strings).

By default, :class:`gTTS` takes the :class:`gtts.tokenizer.core.Tokenizer`'s :func:`gtts.tokenizer.core.Tokenizer.run()`, initialized with default `tokenizer cases`::

    Tokenizer([
        tokenizer_cases.tone_marks,
        tokenizer_cases.period_comma,
        tokenizer_cases.other_punctuation
    ]).run

The available `tokenizer cases` are as follows:

.. automodule:: gtts.tokenizer.tokenizer_cases
   :members:

Customizing & Examples
~~~~~~~~~~~~~~~~~~~~~~

A `tokenizer case` is a function that returns a compiled `regex` object to be used in a ``re.split()`` context.

:class:`gtts.tokenizer.core.Tokenizer` takes a list of `tokenizer cases` and joins their pattern with "|" in one single pattern.

This module provides a class to help build tokenizer cases: :class:`gtts.tokenizer.core.RegexBuilder`. See :class:`gtts.tokenizer.core.RegexBuilder` and :mod:`gtts.tokenizer.tokenizer_cases` for examples.

Using a 3rd-party tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even though :class:`gtts.tokenizer.core.Tokenizer` works well in this context, there are way more advanced tokenizers and tokenzing techniques. As long as you can restrict the lenght of output tokens, you can use any tokenizer you'd like, such as the ones in `NLTK <http://www.nltk.org>`_.

Minimizing
----------

The Google Translate text-to-speech API accepts a maximum of **100 characters**.

If after tokenization any of the tokens is larger than 100 characters, it will be split in two:

* On the last space character that is closest to, but before the 100th character;
* Between the 100th and 101st characters if there's no space.

gtts.tokenizer module reference (:mod:`gtts.tokenizer`)
-------------------------------------------------------

.. autoclass:: gtts.tokenizer.core.RegexBuilder
   :members:
   :undoc-members:

.. autoclass:: gtts.tokenizer.core.PreProcessorRegex
   :members:
   :undoc-members:

.. autoclass:: gtts.tokenizer.core.PreProcessorSub
   :members:
   :undoc-members:

.. autoclass:: gtts.tokenizer.core.Tokenizer
   :members:
   :undoc-members:

.. autoattribute:: gtts.tokenizer.symbols.ABBREVIATIONS
.. autoattribute:: gtts.tokenizer.symbols.SUB_PAIRS
.. autoattribute:: gtts.tokenizer.symbols.ALL_PUNC
.. autoattribute:: gtts.tokenizer.symbols.TONE_MARKS
