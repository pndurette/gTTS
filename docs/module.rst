Module (:mod:`gtts`)
====================

gTTS
----

.. autoclass:: gtts.gTTS
   :members: save, write_to_fp
   :undoc-members:

Languages
---------

.. automodule:: gtts.lang
   :members:

Logging
-------

:mod:`gtts` does logging using the standard Python logging module. The following loggers are available:

``gtts.tts``
  Logger used for the :class:`gTTS` class

``gtts.lang``
  Logger used for the :mod:`lang` module (language fetching)

``gtts``
  Upstream logger for all of the above.

Examples
--------

Advanced
--------

See ``gtts.tokenizer`` module.

Pre-processing
~~~~~~~~~~~~~~

Tokenizing
~~~~~~~~~~

