# gTTS

**gTTS** (*Google Text-to-Speech*), a Python library and CLI tool to interface with Google Translate's text-to-speech API. 
Write spoken `mp3` data to a file, a file-like object (bytestring) for further audio manipulation, or `stdout`. Or simply pre-generate Google Translate TTS request URLs to feed to an external program.
<http://gtts.readthedocs.org/>

[![PyPI version](https://img.shields.io/pypi/v/gTTS.svg)](https://pypi.org/project/gTTS/)
[![Python versions](https://img.shields.io/pypi/pyversions/gTTS.svg)](https://pypi.org/project/gTTS/)
[![Tests workflow](https://github.com/pndurette/gTTS/workflows/Tests/badge.svg)](https://github.com/pndurette/gTTS/actions)
[![codecov](https://codecov.io/gh/pndurette/gTTS/branch/master/graph/badge.svg)](https://codecov.io/gh/pndurette/gTTS)
[![Commits Since](https://img.shields.io/github/commits-since/pndurette/gTTS/latest.svg)](https://github.com/pndurette/gTTS/commits/)
[![PyPi Downloads](http://pepy.tech/badge/gtts)](http://pepy.tech/project/gtts)
[![Buy me a Coffee](https://img.shields.io/badge/buy%20me%20a-coffee-orange)](https://www.buymeacoffee.com/pndurette)

## Features

-   Customizable speech-specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;
-   Customizable text pre-processors which can, for example, provide pronunciation corrections;

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

### Disclaimer

This project is *not* affiliated with Google or Google Cloud. Breaking upstream changes *can* occur without notice. This project is leveraging the undocumented [Google Translate](https://translate.google.com) speech functionality and is *different* from [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/).

### Project

-   [Changelog](CHANGELOG.rst)
-   [Contributing](CONTRIBUTING.rst)

### Licence

[The MIT License (MIT)](LICENSE) Copyright © 2014-2021 Pierre Nicolas Durette & [Contributors](https://github.com/pndurette/gTTS/graphs/contributors)