gTTS 
====

**gTTS** (*Google Text-to-Speech*), a Python module and CLI tool to interface with Google Translate's text-to-speech API. Writes spoken ``mp3`` data to a file, a file-like object (bytestring) for further audio manipulation, or ``stdout``.

|PyPI version| |Build Status| |AppVeyor| |Coveralls| |Commits Since|

Features
--------

* Customizable speech-specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;
* Customizable text pre-processors which can, for example, provide pronunciation corrections;
* Automatic retrieval of supported languages.

Installation
------------

::

    pip install gTTS

Quickstart
----------


.. |Build Status| image:: https://travis-ci.org/pndurette/gTTS.svg?branch=feature/cli-py-2-3
   :target: https://travis-ci.org/pndurette/gTTS
.. |PyPI version| image:: https://img.shields.io/pypi/v/gTTS.svg
   :target: https://pypi.org/project/gTTS/
.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/eiuxodugo78kemff?svg=true
   :target: https://ci.appveyor.com/project/pndurette/gtts
.. |Coveralls| image:: https://coveralls.io/repos/github/pndurette/gTTS/badge.svg?branch=feature%2Fcli-py-2-3
   :target: https://coveralls.io/github/pndurette/gTTS?branch=feature%2Fcli-py-2-3
.. |Commits Since| image:: https://img.shields.io/github/commits-since/pndurette/gTTS/v1.2.2.svg
   :target: https://github.com/pndurette/gTTS/commits/