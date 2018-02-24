# -*- coding: utf-8 -*-
from . import Languages, LanguagesFetchError
from six.moves import urllib
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from gtts_token.gtts_token import Token
import re
import requests
import warnings


class gTTSError(Exception):
    pass


class Speed:
    """Google TTS API read speeds"""

    # The API supports two speeds.
    # (speed <= 0.3: slow; speed > 0.3: normal; default: 1)
    SLOW = 0.3
    NORMAL = 1


class gTTS:
    """gTTS (Google Text to Speech): an interface to Google's Text to Speech API"""

    GOOGLE_TTS_URL = "https://translate.google.com/translate_tts"
    MAX_CHARS = 100  # Max characters the Google TTS API takes at a time

    def __init__(
            self,
            text,
            lang='en',
            slow=False,
            lang_check=False,
            debug=False):
        self.debug = debug

        # Language
        if lang_check:
            try:
                if lang.lower() not in Languages().get():
                    raise ValueError("Language not supported: %s" % lang)
            except LanguagesFetchError as e:
                # We ignore the language check but warn
                print("Warning: %s" % str(e))

        self.lang_check = lang_check
        self.lang = lang.lower()

        # Text
        if not text:
            raise ValueError('No text to speak')
        else:
            self.text = text

        # Read speed
        if slow:
            self.speed = Speed().SLOW
        else:
            self.speed = Speed().NORMAL

        # Split text in parts
        if self._len(text) <= self.MAX_CHARS:
            text_parts = [text]
        else:
            text_parts = self._tokenize(text, self.MAX_CHARS)

        # Clean
        def strip(x): return x.replace('\n', '').strip()
        text_parts = [strip(x) for x in text_parts]
        text_parts = [x for x in text_parts if len(x) > 0]
        self.text_parts = text_parts

        # Google Translate token
        self.token = Token()

    def save(self, savefile):
        """Do the Web request and save to <savefile>"""
        with open(savefile, 'wb') as f:
            self.write_to_fp(f)

    def write_to_fp(self, fp):
        """Do the Web request and save to a file-like object"""
        for idx, part in enumerate(self.text_parts):
            payload = {'ie': 'UTF-8',
                       'q': part,
                       'tl': self.lang,
                       'ttsspeed': self.speed,
                       'total': len(self.text_parts),
                       'idx': idx,
                       'client': 'tw-ob',
                       'textlen': self._len(part),
                       'tk': self.token.calculate_token(part)}
            headers = {
                "Referer": "http://translate.google.com/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
            }
            if self.debug:
                print(payload)
            try:
                # Disable requests' ssl verify to accomodate certain proxies and firewalls
                # Filter out urllib3's insecure warnings. We can live without
                # ssl verify here
                with warnings.catch_warnings():
                    warnings.filterwarnings(
                        "ignore", category=InsecureRequestWarning)
                    r = requests.get(self.GOOGLE_TTS_URL,
                                     params=payload,
                                     headers=headers,
                                     proxies=urllib.request.getproxies(),
                                     verify=False)
                if self.debug:
                    print("Headers: {}".format(r.request.headers))
                    print("Request url: {}".format(r.request.url))
                    print(
                        "Response: {}, Redirects: {}".format(
                            r.status_code, r.history))
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=1024):
                    fp.write(chunk)
            except Exception as e:
                if not self.lang_check and r.status_code == 404:
                    msg = "TTS API failed likely due to unsupported language '%s'. %s"
                    raise gTTSError(msg % (self.lang, str(e)))
                else:
                    raise

    def _len(self, text):
        """Get char len of <text>, after decoding if Python 2"""
        try:
            # Python 2
            return len(unicode(text))
        except NameError:
            # Python 3
            return len(text)

    def _tokenize(self, text, max_size):
        """Tokenizer on basic punctuation"""

        punc = "¡!()[]¿?.,…‥،;:—。，、：？！\n"
        punc_list = [re.escape(c) for c in punc]
        pattern = '|'.join(punc_list)
        parts = re.split(pattern, text)

        min_parts = []
        for p in parts:
            min_parts += self._minimize(p, " ", max_size)
        return min_parts

    def _minimize(self, thestring, delim, max_size):
        """Recursive function that splits <thestring> in chunks
        of maximum <max_size> chars delimited by <delim>. Returns list."""

        if self._len(thestring) > max_size:
            idx = thestring.rfind(delim, 0, max_size)
            return [thestring[:idx]] + \
                self._minimize(thestring[idx:], delim, max_size)
        else:
            return [thestring]


if __name__ == "__main__":
    pass
