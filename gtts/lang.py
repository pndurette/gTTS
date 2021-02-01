# -*- coding: utf-8 -*-
from warnings import warn
import logging

__all__ = ['tts_langs']

# Logger
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def tts_langs():
    """Languages Google Text-to-Speech supports.

    Returns:
        dict: A dictionary of the type `{ '<lang>': '<name>'}`

            Where `<lang>` is an IETF language tag such as `en` or `zh-TW`,
            and `<name>` is the full English name of the language, such as
            `English` or `Chinese (Mandarin/Taiwan)`.

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
        'zh-CN': 'Chinese'
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
    }


def _fallback_deprecated_lang(lang):
    """Languages Google Text-to-Speech used to support.

    Language tags that don't work anymore, but that can
    fallback to a more general language code to maintain
    compatibility.

    Args:
        lang (string): The language tag.

    Returns:
        string: The language tag, as-is if not deprecated,
            or a fallack if it exits.

    Example:
        ``en-GB`` returns ``en``.
        ``en-gb`` returns ``en``.

    """

    deprecated = {
        'en': ['en-us', 'en-ca', 'en-uk', 'en-gb', 'en-au', 'en-gh', 'en-in',
               'en-ie', 'en-nz', 'en-ng', 'en-ph', 'en-za', 'en-tz'],
        'fr': ['fr-ca', 'fr-fr'],
        'pt': ['pt-br', 'pt-pt'],
        'es': ['es-es', 'es-us'],
        'zh-CN': ['zh-cn'],
        'zh-TW': ['zh-tw'],
    }

    for fallback_lang, deprecated_langs in deprecated.items():
        if lang.lower() in deprecated_langs:
            msg = (
                "'{}' has been deprecated, falling back to '{}'. "
                "This fallback will be removed in a future version."
            ).format(lang, fallback_lang)

            warn(msg, DeprecationWarning)
            log.warn(msg)

            return fallback_lang

    return lang