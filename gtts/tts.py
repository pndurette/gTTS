# -*- coding: utf-8 -*-
from . import Languages, LanguagesFetchError
from gtts_token import gtts_token
from six.moves import urllib
import re
import urllib3
import requests
import logging


class Speed:
    """Google TTS API read speeds"""

    # The API supports two speeds.
    # (speed <= 0.3: slow; speed > 0.3: normal; default: 1)
    SLOW = 0.3
    NORMAL = 1


class gTTS:
    """gTTS (Google Text to Speech): an interface to Google's Text to Speech API"""

    MAX_CHARS = 100  # Max characters the Google TTS API takes at a time
    GOOGLE_TTS_URL = "https://translate.google.com/translate_tts"
    GOOGLE_TTS_HEADERS = {
        "Referer": "http://translate.google.com/",
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/47.0.2526.106 Safari/537.36"
    }

    def __init__(
            self,
            text,
            lang='en',
            slow=False,
            lang_check=False):

        # Logger
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.NullHandler())
        self.debug = self.log.isEnabledFor(logging.DEBUG)

        # Debug
        if self.debug:
            for k, v in locals().items():
                if k == 'self':
                    continue
                self.log.debug("%s: %s", k, v)

        # Language
        if lang_check:
            try:
                if lang.lower() not in Languages().get():
                    raise ValueError("Language not supported: %s" % lang)
            except LanguagesFetchError as e:
                self.log.debug(str(e), exc_info=True)
                self.log.warn(str(e))

        self.lang_check = lang_check
        self.lang = lang.lower()

        # Text
        if not text.strip():
            raise ValueError('No text to speak')
        else:
            self.text = text

        # Read speed
        if slow:
            self.speed = Speed.SLOW
        else:
            self.speed = Speed.NORMAL

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

        self.log.debug("text_parts: %i", len(self.text_parts))

        # Google Translate token
        self.token = gtts_token.Token()

    def save(self, savefile):
        """Do the Web request and save to <savefile>"""
        with open(savefile, 'wb') as f:
            self.write_to_fp(f)
            self.log.debug("Saved to %s" % savefile)

    def write_to_fp(self, fp):
        """Do the Web request and save to a file-like object"""

        if not self.text_parts:
            self.log.warn("Nothing to speak")

        # When disabling ssl verify in requests (for proxies and firewalls),
        # urllib3 prints an insecure warning on stdout. We disable that.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

            self.log.debug("payload-%i: %s", idx, payload)

            try:
                # Request
                r = requests.get(self.GOOGLE_TTS_URL,
                                 params=payload,
                                 headers=self.GOOGLE_TTS_HEADERS,
                                 proxies=urllib.request.getproxies(),
                                 verify=False)

                self.log.debug("headers-%i: %s", idx, r.request.headers)
                self.log.debug("url-%i: %s", idx, r.request.url)
                self.log.debug("status-%i: %s", idx, r.status_code)

                r.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise gTTSError(tts=self, response=r)

            try:
                # Write
                for chunk in r.iter_content(chunk_size=1024):
                    fp.write(chunk)
                self.log.debug("part-%i written to %s", idx, fp)
            except AttributeError as e:
                raise TypeError("'fp' must be a file-like object: %s" % str(e))

    def _len(self, text):
        """Get char len of <text>, after Unicode encoding if Python 2"""
        try:
            # Python 2
            return len(unicode(text))
        except NameError:
            # Python 3
            return len(text)

    def _tokenize(self, text, max_size):
        """Tokenize <text> on speech-pausing punctuation
        of maximum <max_size>. Returns list."""

        punc = u"¡!()[]¿?.,…‥،;:—。，、：？！\n"
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

        # Remove <delim> from start of <thestring>
        if thestring.startswith(delim):
            thestring = thestring[len(delim):]

        if self._len(thestring) > max_size:
            try:
                idx = thestring.rindex(delim, 0, max_size)
            except ValueError:
                idx = max_size
            return [thestring[:idx]] + \
                self._minimize(thestring[idx:], delim, max_size)
        else:
            return [thestring]


class gTTSError(Exception):
    """Exception that uses heuristics to present a meaningful error message"""

    def __init__(self, msg=None, **kwargs):
        self.tts = kwargs.pop('tts', None)
        self.rsp = kwargs.pop('response', None)
        if msg:
            self.msg = msg
        elif self.tts and self.rsp:
            self.msg = self.infer_msg(self.tts, self.rsp)
        else:
            self.msg = None  # "Unknown error"
        super(gTTSError, self).__init__(self.msg)

    def infer_msg(self, tts, rsp):
        """Attempt to guess what went wrong by using known
        information (e.g. http response) and observed behaviour"""

        # rsp should be <requests.Response>
        # http://docs.python-requests.org/en/master/api/
        status = rsp.status_code
        reason = rsp.reason

        cause = "Unknown"
        if status == 403:
            cause = "Bad token or upstream API changes"
        elif status == 404 and not tts.lang_check:
            cause = "Unsupported language '%s'" % self.tts.lang
        elif status >= 500:
            cause = "Uptream API error. Try again later."

        return "%i (%s) from TTS API. Probable cause: %s" % (
            status, reason, cause)


if __name__ == "__main__":
    pass
