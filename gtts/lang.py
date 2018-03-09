# -*- coding: utf-8 -*-
import requests
import logging
import re
from bs4 import BeautifulSoup

"""Google Translate loads a JavaScript Array of 'languages
codes' that can be read. We intersect with all the
languages Google Translate provides.
"""


class LanguagesFetchError(Exception):
    pass


class Languages:
    """Supported languages by Google's Text to Speech API"""

    URL_BASE = 'http://translate.google.com'
    JS_FILE = 'desktop_module_main.js'

    """Extra undocumented language codes observed
    to provide different dialects or accents
    """
    EXTRA_LANGS = {
        # Chinese
        'zh-cn': 'Chinese (Mandarin/China)',
        'zh-tw': 'Chinese (Mandarin/Taiwan)',
        #'zh-yue': 'Chinese (Cantonese)',
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
        # Portuguese
        'pt-br': 'Portuguese (Brazil)',
        'pt-pt': 'Portuguese (Portugal)',
        # Spanish
        'es-es': 'Spanish (Spain)',
        'es-us': 'Spanish (United States)'
    }

    def __init__(self):
        self.langs = dict()

        # Logger
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.NullHandler())

    def get(self):
        self.langs = self._fetch_langs()
        self.langs.update(self.EXTRA_LANGS)

        self.log.debug("langs: %s", self.langs)
        return self.langs

    def _fetch_langs(self):
        try:
            """Load HTML"""
            page = requests.get(self.URL_BASE)
            soup = BeautifulSoup(page.content, 'html.parser')

            """JavaScript URL
            The <script src=''> path can change, but not the file.
            Ex: /zyx/abc/20180211/desktop_module_main.js
            """
            js_path = soup.find(src=re.compile(self.JS_FILE))['src']
            js_url = "{}/{}".format(self.URL_BASE, js_path)

            """Load JavaScript"""
            js_contents = str(requests.get(js_url).content)

            """Approximately extract TTS-enabled language codes
            RegEx pattern search because minified variables can change.
            Extra garbage will be dealt with later as we keep languages only.
            In: "[...]Fv={af:1,ar:1,[...],zh:1,"zh-cn":1,"zh-tw":1}[...]"
            Out: ['is', '12', [...], 'af', 'ar', [...], 'zh', 'zh-cn', 'zh-tw']
            """
            pattern = '[{,\"](\w{2}|\w{2}-\w{2,3})(?=:1|\":1)'
            tts_langs = re.findall(pattern, js_contents)

            """Build lang. dict. from HTML lang. <select>
            Filtering with the TTS-enabled languages
            In: [<option value='af'>Afrikaans</option>, [...]]
            Out: {'af': 'Afrikaans', [...]}
            """
            langs_html = soup.find('select', {'id': 'gt-sl'}).findAll('option')
            langs = {
                l['value']: l.text for l in langs_html if l['value'] in tts_langs}
            return langs
        except Exception as e:
            raise LanguagesFetchError("Unable to get language list")


if __name__ == "__main__":
    pass
