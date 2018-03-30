Module (:mod:`gtts`)
====================

gTTS
----

.. autoclass:: gtts.gTTS
   :members: save, write_to_fp
   :undoc-members:

Languages
---------

.. autoclass:: gtts.Languages
   :members: get
   :undoc-members:

Logging
-------

:mod:`gtts` does logging using the standard Python logging module. The following loggers are available:

``gtts.tts``
  Logger used for the :class:`gTTS` class

``gtts.string``
  Logger used for the :mod:`string` submodule (string and tokenizing utils)

``gtts``
  Logger for all of the above.

Advanced
--------

Pre-processing rules
~~~~~~~~~~~~~~~~~~~~

Tokenizer rules
~~~~~~~~~~~~~~~
