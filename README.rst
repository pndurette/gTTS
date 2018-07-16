.. image:: http://pepy.tech/badge/gtts
   :target: http://pepy.tech/project/gtts
   :alt: PyPi Downloads

====
gTTS
====

**gTTS** (*Google Text-to-Speech*), a Python library and CLI tool to interface with Google Translate's text-to-speech API. Writes spoken ``mp3`` data to a file, a file-like object (bytestring) for further audio manipulation, or ``stdout``. 
http://gtts.readthedocs.org/

|PyPI version| |Python versions| |Build Status| |AppVeyor| |Coveralls| |Commits Since|

Features
--------

* Customizable speech-specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;
* Customizable text pre-processors which can, for example, provide pronunciation corrections;
* Automatic retrieval of supported languages.

Installation
============

::

    $ pip install gTTS

Quickstart
==========

Command Line::

    $ gtts-cli 'hello' --output hello.mp3


Module::

    >>> from gtts import gTTS
    >>> tts = gTTS('hello')
    >>> tts.save('hello.mp3')

See http://gtts.readthedocs.org/ for documentation and examples.

Project
=======

* Changelog_
* Contributing_

Licence
=======
| `The MIT License (MIT) <LICENSE>`_
| Copyright © 2014-2018 Pierre Nicolas Durette


.. |PyPI version| image:: https://img.shields.io/pypi/v/gTTS.svg
   :target: https://pypi.org/project/gTTS/
.. |Python versions| image:: https://img.shields.io/pypi/pyversions/gTTS.svg
   :target: https://pypi.org/project/gTTS/ 

.. |Build Status| image:: https://travis-ci.org/pndurette/gTTS.svg?branch=master
   :target: https://travis-ci.org/pndurette/gTTS
.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/eiuxodugo78kemff/branch/master?svg=true
   :target: https://ci.appveyor.com/project/pndurette/gtts
.. |Coveralls| image:: https://coveralls.io/repos/github/pndurette/gTTS/badge.svg?branch=master
   :target: https://coveralls.io/github/pndurette/gTTS?branch=master

.. |Commits Since| image:: https://img.shields.io/github/commits-since/pndurette/gTTS/latest.svg
   :target: https://github.com/pndurette/gTTS/commits/

.. _contributing: CONTRIBUTING.rst
.. _changelog: CHANGELOG.rst
.. _licence: LICENSE
