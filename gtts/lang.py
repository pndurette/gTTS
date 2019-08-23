# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import logging
import re

__all__ = ['tts_langs']

URL_BASE = 'https://translate.google.com'
JS_FILE = 'translate_m.js'

# Logger
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def tts_langs():
    """Languages Google Text-to-Speech supports.

    Returns:
        dict: A dictionnary of the type `{ '<lang>': '<name>'}`

        Where `<lang>` is an IETF language tag such as `en` or `pt-br`,
        and `<name>` is the full English name of the language, such as
        `English` or `Portuguese (Brazil)`.

    The dictionnary returned combines languages from two origins:

    - Languages fetched automatically from Google Translate
    - Languages that are undocumented variations that were observed to work and
      present different dialects or accents.

    """
    try:
        langs = dict()
        langs.update(_fetch_langs())
        langs.update(_extra_langs())
        log.debug("langs: %s", langs)
        return langs
    except Exception as e:
        raise RuntimeError("Unable to get language list: %s" % str(e))


def _fetch_langs():
    """Fetch (scrape) languages from Google Translate.

    Google Translate loads a JavaScript Array of 'languages codes' that can
    be spoken. We intersect this list with all the languages Google Translate
    provides to get the ones that support text-to-speech.

    Returns:
        dict: A dictionnary of languages from Google Translate

    """
    # Load HTML
    page = requests.get(URL_BASE)
    soup = BeautifulSoup(page.content, 'html.parser')

    # JavaScript URL
    # The <script src=''> path can change, but not the file.
    # Ex: /zyx/abc/20180211/desktop_module_main.js
    js_path = soup.find(src=re.compile(JS_FILE))['src']
    js_url = "{}/{}".format(URL_BASE, js_path)

    # Load JavaScript
    js_contents = requests.get(js_url).text

    # Approximately extract TTS-enabled language codes
    # RegEx pattern search because minified variables can change.
    # Extra garbage will be dealt with later as we keep languages only.
    # In: "[...]Fv={af:1,ar:1,[...],zh:1,"zh-cn":1,"zh-tw":1}[...]"
    # Out: ['is', '12', [...], 'af', 'ar', [...], 'zh', 'zh-cn', 'zh-tw']
    pattern = r'[{,\"](\w{2}|\w{2}-\w{2,3})(?=:1|\":1)'
    tts_langs = re.findall(pattern, js_contents)

    # Build lang. dict. from main page (JavaScript object populating lang. menu)
    # Filtering with the TTS-enabled languages
    # In: "{code:'auto',name:'Detect language'},{code:'af',name:'Afrikaans'},[...]"
    # re.findall: [('auto', 'Detect language'), ('af', 'Afrikaans'), [...]]
    # Out: {'af': 'Afrikaans', [...]}
    trans_pattern = r"{code:'(?P<lang>.+?[^'])',name:'(?P<name>.+?[^'])'}"
    trans_langs = re.findall(trans_pattern, page.text)
    return {lang: name for lang, name in trans_langs if lang in tts_langs}


def _extra_langs():
    """Define extra languages.

    Returns:
        dict: A dictionnary of extra languages manually defined.

        Variations of the ones fetched by `_fetch_langs`,
        observed to provide different dialects or accents or
        just simply accepted by the Google Translate Text-to-Speech API.

    """
    return {
        # Chinese
        'zh-cn': 'Chinese (Mandarin/China)',
        'zh-tw': 'Chinese (Mandarin/Taiwan)',
        # English
        'en-us': 'English (US)',
        'en-ca': 'English (Canada)',
        'en-uk': 'English (UK)',
        'en-gb': 'English (UK)',
        'en-au': 'English (Australia)',
        'en-gh': 'English (Ghana)',
        'en-in': 'English (India)',
        'en-ie': 'English (Ireland)',
        'en-nz': 'English (New Zealand)',
        'en-ng': 'English (Nigeria)',
        'en-ph': 'English (Philippines)',
        'en-za': 'English (South Africa)',
        'en-tz': 'English (Tanzania)',
        # French
        'fr-ca': 'French (Canada)',
        'fr-fr': 'French (France)',
        # Portuguese
        'pt-br': 'Portuguese (Brazil)',
        'pt-pt': 'Portuguese (Portugal)',
        # Spanish
        'es-es': 'Spanish (Spain)',
        'es-us': 'Spanish (United States)'
    }
