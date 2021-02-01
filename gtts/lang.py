# -*- coding: utf-8 -*-
import logging

__all__ = ['tts_langs']

# Logger
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def tts_langs():
    """Languages Google Text-to-Speech supports.

    Returns:
        dict: A dictionary of the type `{ '<lang>': '<name>'}`

            Where `<lang>` is an IETF language tag such as `en` or `pt-BR`,
            and `<name>` is the full English name of the language, such as
            `English` or `Portuguese (Brazil)`.

    The dictionary returned combines languages from two origins:

    - Languages fetched from Google Translate
    - Languages that are undocumented variations that were observed to work and
      present different dialects or accents.

    """
    langs = dict()
    langs.update(_main_langs())
    langs.update(_extra_langs())
    log.debug("langs: {}".format(langs))
    return langs


def _main_langs():
    """Define the main languages.

    Returns:
        dict: A dictionnary of the main languages extracted from
            Google Translate.

    """
    return {
        'af': 'Afrikaans',
        'ar': 'Arabic',
        'bn': 'Bengali',
        'bs': 'Bosnian',
        'ca': 'Catalan',
        'cs': 'Czech',
        'cy': 'Welsh',
        'da': 'Danish',
        'de': 'German',
        'el': 'Greek',
        'en': 'English',
        'eo': 'Esperanto',
        'es': 'Spanish',
        'et': 'Estonian',
        'fi': 'Finnish',
        'fr': 'French',
        'gu': 'Gujarati',
        'hi': 'Hindi',
        'hr': 'Croatian',
        'hu': 'Hungarian',
        'hy': 'Armenian',
        'id': 'Indonesian',
        'is': 'Icelandic',
        'it': 'Italian',
        'ja': 'Japanese',
        'jw': 'Javanese',
        'km': 'Khmer',
        'kn': 'Kannada',
        'ko': 'Korean',
        'la': 'Latin',
        'lv': 'Latvian',
        'mk': 'Macedonian',
        'ml': 'Malayalam',
        'mr': 'Marathi',
        'my': 'Myanmar (Burmese)',
        'ne': 'Nepali',
        'nl': 'Dutch',
        'no': 'Norwegian',
        'pl': 'Polish',
        'pt': 'Portuguese',
        'ro': 'Romanian',
        'ru': 'Russian',
        'si': 'Sinhala',
        'sk': 'Slovak',
        'sq': 'Albanian',
        'sr': 'Serbian',
        'su': 'Sundanese',
        'sv': 'Swedish',
        'sw': 'Swahili',
        'ta': 'Tamil',
        'te': 'Telugu',
        'th': 'Thai',
        'tl': 'Filipino',
        'tr': 'Turkish',
        'uk': 'Ukrainian',
        'ur': 'Urdu',
        'vi': 'Vietnamese',
        'zh': 'Chinese'
    }


def _extra_langs():
    """Define extra languages.

    Returns:
        dict: A dictionnary of extra languages manually defined.

            Variations of the ones fetched by `_main_langs`,
            observed to provide different dialects or accents or
            just simply accepted by the Google Translate Text-to-Speech API.

    """
    return {
        # Chinese
        'zh-CN': 'Chinese (Mandarin/China)',
        'zh-TW': 'Chinese (Mandarin/Taiwan)',
        # English
        'en-US': 'English (US)',
        'en-CA': 'English (Canada)',
        'en-UK': 'English (UK)',
        'en-GB': 'English (UK)',
        'en-AU': 'English (Australia)',
        'en-GH': 'English (Ghana)',
        'en-IN': 'English (India)',
        'en-IE': 'English (Ireland)',
        'en-NZ': 'English (New Zealand)',
        'en-NG': 'English (Nigeria)',
        'en-PH': 'English (Philippines)',
        'en-ZA': 'English (South Africa)',
        'en-TZ': 'English (Tanzania)',
        # French
        'fr-CA': 'French (Canada)',
        'fr-FR': 'French (France)',
        # Portuguese
        'pt-BR': 'Portuguese (Brazil)',
        'pt-PT': 'Portuguese (Portugal)',
        # Spanish
        'es-ES': 'Spanish (Spain)',
        'es-US': 'Spanish (United States)'
    }
