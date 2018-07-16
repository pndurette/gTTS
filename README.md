# gTTS

**gTTS** (*Google Text-to-Speech*), a Python library and CLI tool to interface with Google Translate's text-to-speech API. 
Writes spoken `mp3` data to a file, a file-like object (bytestring) for further audio
manipulation, or `stdout`. <http://gtts.readthedocs.org/>

[![PyPI version](https://img.shields.io/pypi/v/gTTS.svg)](https://pypi.org/project/gTTS/)
[![Python versions](https://img.shields.io/pypi/pyversions/gTTS.svg)](https://pypi.org/project/gTTS/)
[![Build Status](https://travis-ci.org/pndurette/gTTS.svg?branch=master)](https://travis-ci.org/pndurette/gTTS)
[![AppVeyor](https://ci.appveyor.com/api/projects/status/eiuxodugo78kemff/branch/master?svg=true)](https://ci.appveyor.com/project/pndurette/gtts)
[![Coveralls](https://coveralls.io/repos/github/pndurette/gTTS/badge.svg?branch=master)](https://coveralls.io/github/pndurette/gTTS?branch=master)
[![Commits Since](https://img.shields.io/github/commits-since/pndurette/gTTS/latest.svg)](https://github.com/pndurette/gTTS/commits/)
[![PyPi Downloads](http://pepy.tech/badge/gtts)](http://pepy.tech/project/gtts)

## Features

-   Customizable speech-specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;
-   Customizable text pre-processors which can, for example, provide pronunciation corrections;
-   Automatic retrieval of supported languages.

### Installation

    $ pip install gTTS

### Quickstart

Command Line:

    $ gtts-cli 'hello' --output hello.mp3

Module:

    >>> from gtts import gTTS
    >>> tts = gTTS('hello')
    >>> tts.save('hello.mp3')

See <http://gtts.readthedocs.org/> for documentation and examples.

### Project

-   [Changelog](CHANGELOG.rst)
-   [Contributing](CONTRIBUTING.rst)

### Licence

[The MIT License (MIT)](LICENSE) Copyright © 2014-2018 Pierre Nicolas Durette
