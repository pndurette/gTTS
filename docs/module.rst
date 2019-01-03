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

.. note:: The easiest way to get a list of available language is to print them with ``gtts-cli --all``

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

Playing sound directly
----------------------

There's quite a few libraries that do this. Write 'hello' to a file-like object do further manipulation:::

    >>> from gtts import gTTS
    >>> from io import BytesIO
    >>>
    >>> mp3_fp = BytesIO()
    >>> tts = gTTS('hello', 'en')
    >>> tts.write_to_fp(mp3_fp)
    >>>
    >>> # Load `mp3_fp` as an mp3 file in
    >>> # the audio library of your choice

Logging
-------

:mod:`gtts` does logging using the standard Python logging module. The following loggers are available:

``gtts.tts``
  Logger used for the :class:`gTTS` class

``gtts.lang``
  Logger used for the :mod:`lang` module (language fetching)

``gtts``
  Upstream logger for all of the above

