Module (:mod:`gtts`)
====================

.. contents:: :local:
   :depth: 2

gTTS (:class:`gtts.gTTS`)
-------------------------

.. automodule:: gtts.tts
   :members:

Languages (:mod:`gtts.lang`)
----------------------------

.. note:: The easiest way to get a list of available language is to print them
    with ``gtts-cli --all``

.. automodule:: gtts.lang
   :members:

Examples
--------

Write 'hello' in English to ``hello.mp3``::

    >>> from gtts import gTTS
    >>> tts = gTTS('hello', lang='en')
    >>> tts.save('hello.mp3')

Write 'hello bonjour' in English then French to ``hello_bonjour.mp3``::

    >>> from gtts import gTTS
    >>> tts_en = gTTS('hello', lang='en')
    >>> tts_fr = gTTS('bonjour', lang='fr')
    >>>
    >>> with open('hello_bonjour.mp3', 'wb') as f:
    ...     tts_en.write_to_fp(f)
    ...     tts_fr.write_to_fp(p)

Instead of writing to disk, get URL for 'hello' in English::

    >>> from gtts import gTTS
    >>> tts = gTTS('hello', lang='en')
    >>> tts.get_urls()
    ['https://translate.google.com/translate_tts?ie=UTF-8&q=hello&tl=en&ttsspeed=1&total=1&idx=0&client=tw-ob&textlen=5&tk=316070.156329']

Playing sound directly
----------------------

There's quite a few libraries that do this. Write 'hello' to a file-like object
to do further manipulation:::

    >>> from gtts import gTTS
    >>> from io import BytesIO
    >>>
    >>> mp3_fp = BytesIO()
    >>> tts = gTTS('hello', 'en')
    >>> tts.write_to_fp(mp3_fp)
    >>>
    >>> # Load `mp3_fp` as an mp3 file in
    >>> # the audio library of your choice

.. note:: See `Issue #26 <https://github.com/pndurette/gTTS/issues/26>`_ for
    a discussion and examples of direct playback using various methods.

.. note:: Starting with ``gTTS`` :doc:`2.1.0 <changelog>`, the
    :class:`gtts.tts.gTTS.get_urls` method can be used to obtain the list of
    generated URLs requests (whithout fullfilling them) which could be used
    for playback in another program. See `Examples`_ above.


Logging
-------

:mod:`gtts` does logging using the standard Python logging module. The following loggers are available:

``gtts.tts``
  Logger used for the :class:`gTTS` class

``gtts.lang``
  Logger used for the :mod:`lang` module (language fetching)

``gtts``
  Upstream logger for all of the above

