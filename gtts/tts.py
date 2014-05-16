# -*- coding: utf-8 -*-
import re, requests

class gTTS:
    """ gTTS (Google Text to Speech): an interface to Google's Text to Speech API """

    GOOGLE_TTS_URL = 'http://translate.google.com/translate_tts'
    MAX_CHARS = 100 # Max characters the Google TTS API takes at a time
    LANGUAGES = {
        'af' : 'Afrikaans',
        'sq' : 'Albanian',
        'ar' : 'Arabic',
        'hy' : 'Armenian',
        'ca' : 'Catalan',
        'zh-CN' : 'Mandarin (simplified)',
        'zh-TW' : 'Mandarin (traditional)',
        'hr' : 'Croatian',
        'cs' : 'Czech',
        'da' : 'Danish',
        'nl' : 'Dutch',
        'en' : 'English',
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
        'ro' : 'Romanian',
        'ru' : 'Russian',
        'sr' : 'Serbian',
        'sk' : 'Slovak',
        'es' : 'Spanish',
        'sw' : 'Swahili',
        'sv' : 'Swedish',
        'ta' : 'Tamil',
        'th' : 'Thai',
        'tr' : 'Turkish',
        'vi' : 'Vietnamese',
        'cy' : 'Welsh'
    }

    def __init__(self, text, lang = 'en', debug = False):
        self.debug = debug
        if lang not in self.LANGUAGES:
            raise Exception('Language not supported: %s' % lang)
        else:
            self.lang = lang

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
        text_parts = map(lambda x: x.replace('\n', '').strip(), text_parts)
        text_parts = filter(lambda x: len(x) > 0, text_parts)
        self.text_parts = text_parts

    def save(self, savefile):
        """ Do the Web request and save to `savefile` """
        with open(savefile, 'wb') as f:
            for idx, part in enumerate(self.text_parts):
                payload = { 'ie' : 'UTF-8',
                            'tl' : self.lang,
                            'q' : part,
                            'total' : len(self.text_parts),
                            'idx' : idx,
                            'textlen' : len(part) }
                if self.debug: print payload
                try:
                    r = requests.get(self.GOOGLE_TTS_URL, params=payload)
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
                except Exception, e:
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
