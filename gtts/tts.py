# -*- coding: utf-8 -*-
import re
import requests



def rshift(val, n): return val>>n if val >= 0 else (val+0x100000000)>>n

class gTTS:
    """ gTTS (Google Text to Speech): an interface to Google's Text to Speech API """

    GOOGLE_TTS_URL = 'https://translate.google.com/translate_tts'
    MAX_CHARS = 100 # Max characters the Google TTS API takes at a time
    LANGUAGES = {
        'af' : 'Afrikaans',
        'sq' : 'Albanian',
        'ar' : 'Arabic',
        'hy' : 'Armenian',
        'ca' : 'Catalan',
        'zh' : 'Chinese',
        'zh-cn' : 'Chinese (Mandarin/China)',
        'zh-tw' : 'Chinese (Mandarin/Taiwan)',
        'zh-yue' : 'Chinese (Cantonese)',
        'hr' : 'Croatian',
        'cs' : 'Czech',
        'da' : 'Danish',
        'nl' : 'Dutch',
        'en' : 'English',
        'en-au' : 'English (Australia)',
        'en-uk' : 'English (United Kingdom)',
        'en-us' : 'English (United States)',
        'eo' : 'Esperanto',
        'fi' : 'Finnish',
        'fr' : 'French',
        'de' : 'German',
        'el' : 'Greek',
        'ht' : 'Haitian Creole',
        'hi' : 'Hindi',
        'hu' : 'Hungarian',
        'is' : 'Icelandic',
        'id' : 'Indonesian',
        'it' : 'Italian',
        'ja' : 'Japanese',
        'ko' : 'Korean',
        'la' : 'Latin',
        'lv' : 'Latvian',
        'mk' : 'Macedonian',
        'no' : 'Norwegian',
        'pl' : 'Polish',
        'pt' : 'Portuguese',
        'pt-br' : 'Portuguese (Brazil)',
        'ro' : 'Romanian',
        'ru' : 'Russian',
        'sr' : 'Serbian',
        'sk' : 'Slovak',
        'es' : 'Spanish',
        'es-es' : 'Spanish (Spain)',
        'es-us' : 'Spanish (United States)',
        'sw' : 'Swahili',
        'sv' : 'Swedish',
        'ta' : 'Tamil',
        'th' : 'Thai',
        'tr' : 'Turkish',
        'vi' : 'Vietnamese',
        'cy' : 'Welsh'
    }

    GOOGLE_TRANSLATE_URL = "http://translate.google.com"
    SALT_1 = "+-a^+6"
    SALT_2 = "+-3^+b+-f"


    def __init__(self, text, lang = 'en', debug = False):
        self.debug = debug
        if lang.lower() not in self.LANGUAGES:
            raise Exception('Language not supported: %s' % lang)
        else:
            self.lang = lang.lower()

        if not text:
            raise Exception('No text to speak')
        else:
            self.text = text

        # Split text in parts
        if len(text) <= self.MAX_CHARS: 
            text_parts = [text]
        else:
            text_parts = self._tokenize(text, self.MAX_CHARS)           

        # Clean
        def strip(x): return x.replace('\n', '').strip()
        text_parts = [strip(x) for x in text_parts]
        text_parts = [x for x in text_parts if len(x) > 0]
        self.text_parts = text_parts
        self.token_key = None

    def save(self, savefile):
        """ Do the Web request and save to `savefile` """
        with open(savefile, 'wb') as f:
            self.write_to_fp(f)
            f.close()

    def write_to_fp(self, fp):
        """ Do the Web request and save to a file-like object """
        for idx, part in enumerate(self.text_parts):
            payload = { 'ie' : 'UTF-8',
                        'q' : part,
                        'tl' : self.lang,
                        'total' : len(self.text_parts),
                        'idx' : idx,
                        'client' : 't',
                        'textlen' : len(part),
                        'tk' : self.calculate_token(part)}
            headers = {
                "Referer" : "http://translate.google.com/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
            }
            if self.debug: print(payload)
            try:
                r = requests.get(self.GOOGLE_TTS_URL, params=payload, headers=headers)
                if self.debug:
                    print("Headers: {}".format(r.request.headers))
                    print("Reponse: {}, Redirects: {}".format(r.status_code, r.history))
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=1024):
                    fp.write(chunk)
            except Exception as e:
                raise

    def _tokenize(self, text, max_size):
        """ Tokenizer on basic roman punctuation """ 
        
        punc = "¡!()[]¿?.,;:—«»\n"
        punc_list = [re.escape(c) for c in punc]
        pattern = '|'.join(punc_list)
        parts = re.split(pattern, text)

        min_parts = []
        for p in parts:
            min_parts += self._minimize(p, " ", max_size)
        return min_parts

    def calculate_token(self, text, seed=None):
        if self.token_key is None and seed is None:
            r = requests.get(self.GOOGLE_TRANSLATE_URL)
            m = re.search(r"TKK='(\d+)'", r.text)
            self.token_key = int(m.group(1))
        tk = "tk"
        e = 0
        f = 0
        d = [None] * len(text)
        for c in text:
            g = ord(c)
            if 128 > g:
                d[e] = g
                e += 1
            elif 2048 > g:
                d[e] = g >> 6 | 192
                e += 1
            else:
                if 55296 == (g & 64512) and f + 1 < len(text) and 56320 == (ord(text[f + 1]) & 64512):
                    f += 1
                    g = 65536 + ((g & 1023) << 10) + (ord(text[f]) & 1023)
                    d[e] = g >> 18 | 240
                    e += 1
                    d[e] = g >> 12 & 63 | 128
                    e += 1
                else:
                    d[e] = g >> 12 | 224
                    e += 1
                    d[e] = g >> 6 & 63 | 128
                    e += 1
                    d[e] = g & 63 | 128
                    e += 1

        a = seed if seed is not None else self.token_key
        for value in d:
            a += value
            a = self.work_token(a, self.SALT_1)
        a = self.work_token(a, self.SALT_2)
        if 0 > a:
            a = (a & 2147483647) + 2147483648
        a %= 1E6
        a = int(a)
        return str(a) + "." + str(a ^ self.token_key)

    def work_token(self, a, seed):
        for i in range(0, len(seed) - 2, 3):
            char = seed[i + 2]
            d = ord(char[0]) - 87 if char >= "a" else int(char)
            d = rshift(a, d) if seed[i + 1] == "+" else a << d
            a = a + d & 4294967295 if seed[i] == "+" else a ^ d
        return a


    def _minimize(self, thestring, delim, max_size):
        """ Recursive function that splits `thestring` in chunks
        of maximum `max_size` chars delimited by `delim`. Returns list. """ 
        
        if len(thestring) > max_size:
            idx = thestring.rfind(delim, 0, max_size)
            return [thestring[:idx]] + self._minimize(thestring[idx:], delim, max_size)
        else:
            return [thestring]

if __name__ == "__main__":
        pass
