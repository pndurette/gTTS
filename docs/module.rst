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

.. note:: The easiest way to get a list of available languages is to print them
    with ``gtts-cli --all``

.. automodule:: gtts.lang
   :members:

Localized 'accents'
-------------------

For a given language, Google Translate text-to-speech can speak in different
local 'accents' depending on the Google domain (``google.<tld>``) of the request,
with some examples shown in the table below.

.. note:: This is an **incomplete** list. Try different combinaisons of language codes and
    `known localized Google domains <https://www.google.com/supported_domains>`_. Feel
    free to add new combinaisons to this list via a Pull Request!

+---------------------------+--------------------------+----------------------------+
|       Local accent        | Language code (``lang``) | Top-level domain (``tld``) |
+===========================+==========================+============================+
| English (Australia)       | ``en``                   | ``com.au``                 |
+---------------------------+--------------------------+----------------------------+
| English (United Kingdom)  | ``en``                   | ``co.uk``                  |
+---------------------------+--------------------------+----------------------------+
| English (United States)   | ``en``                   | ``com`` (default)          |
+---------------------------+--------------------------+----------------------------+
| English (Canada)          | ``en``                   | ``ca``                     |
+---------------------------+--------------------------+----------------------------+
| English (India)           | ``en``                   | ``co.in``                  |
+---------------------------+--------------------------+----------------------------+
| English (Ireland)         | ``en``                   | ``ie``                     |
+---------------------------+--------------------------+----------------------------+
| English (South Africa)    | ``en``                   | ``co.za``                  |
+---------------------------+--------------------------+----------------------------+
| French (Canada)           | ``fr``                   | ``ca``                     |
+---------------------------+--------------------------+----------------------------+
| French (France)           | ``fr``                   | ``fr``                     |
+---------------------------+--------------------------+----------------------------+
| Mandarin (China Mainland) | ``zh-CN``                | any                        |
+---------------------------+--------------------------+----------------------------+
| Mandarin (Taiwan)         | ``zh-TW``                | any                        |
+---------------------------+--------------------------+----------------------------+
| Portuguese (Brazil)       | ``pt``                   | ``com.br``                 |
+---------------------------+--------------------------+----------------------------+
| Portuguese (Portugal)     | ``pt``                   | ``pt``                     |
+---------------------------+--------------------------+----------------------------+
| Spanish (Mexico)          | ``es``                   | ``com.mx``                 |
+---------------------------+--------------------------+----------------------------+
| Spanish (Spain)           | ``es``                   | ``es``                     |
+---------------------------+--------------------------+----------------------------+
| Spanish (United States)   | ``es``                   | ``com`` (default)          |
+---------------------------+--------------------------+----------------------------+


Examples
--------

Write 'hello' in English to ``hello.mp3``::

    >>> from gtts import gTTS
    >>> tts = gTTS('hello', lang='en')
    >>> tts.save('hello.mp3')

Write 'hello' in Australian English to ``hello.mp3``::

    >>> from gtts import gTTS
    >>> tts = gTTS('hello', lang='en', tld='com.au')
    >>> tts.save('hello.mp3')

Write 'hello bonjour' in English then French to ``hello_bonjour.mp3``::

    >>> from gtts import gTTS
    >>> tts_en = gTTS('hello', lang='en')
    >>> tts_fr = gTTS('bonjour', lang='fr')
    >>>
    >>> with open('hello_bonjour.mp3', 'wb') as f:
    ...     tts_en.write_to_fp(f)
    ...     tts_fr.write_to_fp(f)

Playing sound directly
----------------------

There's quite a few libraries that do this. Write 'hello' to a file-like object
to do further manipulation:::

    >>> from gtts import gTTS
    >>> from io import BytesIO
    >>>
    >>> mp3_fp = BytesIO()
    >>> tts = gTTS('hello', lang='en')
    >>> tts.write_to_fp(mp3_fp)
    >>>
    >>> # Load `mp3_fp` as an mp3 file in
    >>> # the audio library of your choice

.. note:: See `Issue #26 <https://github.com/pndurette/gTTS/issues/26>`_ for
    a discussion and examples of direct playback using various methods.


Logging
-------

:mod:`gtts` does logging using the standard Python logging module. The following loggers are available:

``gtts.tts``
  Logger used for the :class:`gTTS` class

``gtts.lang``
  Logger used for the :mod:`lang` module (language fetching)

``gtts``
  Upstream logger for all of the above

