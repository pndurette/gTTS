# -*- coding: utf-8 -*-
from .version import __version__
from .lang import Languages, LanguagesFetchError
from .tts import gTTS, gTTSError

__all__ = ['Languages', 'LanguagesFetchError',
           'gTTS', 'gTTSError']
