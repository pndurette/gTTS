# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import logging
import re
from .server import server

__all__ = ['tts_langs']

JS_FILE = 'translate_m.js'

# Logger
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def tts_langs(country_code=None):
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
        langs.update(_fetch_langs(country_code))
        langs.update(_extra_langs())
        log.debug("langs: %s", langs)
        return langs
    except Exception as e:
        raise RuntimeError("Unable to get language list: %s" % str(e))


def _fetch_langs(country_code=None):
    """Fetch (scrape) languages from Google Translate.

    Google Translate loads a JavaScript Array of 'languages codes' that can
    be spoken. We intersect this list with all the languages Google Translate
    provides to get the ones that support text-to-speech.

    Returns:
        dict: A dictionary of languages from Google Translate

    """

    srv = server(country_code)

    # Load HTML
    page = requests.get(srv["url_base"])
    if page.status_code != 200:
        raise RuntimeError("Could not reach server {} got HTTP status code {}".format(srv['url_base'], page.status_code))

    soup = BeautifulSoup(page.content, 'html.parser')

    # JavaScript URL
    # The <script src=''> path can change, but not the file.
    # Ex: /zyx/abc/20180211/desktop_module_main.js
    js_soup = soup.find(src=re.compile(JS_FILE))
    if not js_soup:
        log.warning('Could not get langs from {}'.format(srv['url_base']))
        return {}

    js_url = "{}/{}".format(srv["url_base"], js_soup['src'])

    # Load JavaScript
    js = requests.get(js_url)
    if js.status_code != 200:
        raise RuntimeError("Could not reach server {} got HTTP status code {}".format(js_url, js.status_code))

    # Approximately extract TTS-enabled language codes
    # RegEx pattern search because minified variables can change.
    # Extra garbage will be dealt with later as we keep languages only.
    # In: "[...]Fv={af:1,ar:1,[...],zh:1,"zh-cn":1,"zh-tw":1}[...]"
    # Out: ['is', '12', [...], 'af', 'ar', [...], 'zh', 'zh-cn', 'zh-tw']
    pattern = r'[{,\"](\w{2}|\w{2}-\w{2,3})(?=:1|\":1)'
    tts_langs = re.findall(pattern, js.text)

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
