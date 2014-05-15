gTTS
====

*gTTS* (Google Text to Speech): a Python interface to Google's Text to Speech API. Create an mp3 file with the `gTTS` module or `tts-cli.py` command line utility.

Module
------

Initialize a new `GoogleTTS`:

    >> from gtts import gTTS
    >> tts = gTTS(text='Hello', lang='en')
    >> tts.save("hello.mp3")

**Parameters**:

  *  `text` is the text to speak to file;
  *  `lang` is the language to speak in. A ISO 639-1 language code supported by the Google Text to Speech API.

Command line utility
--------------------
Invoke `tts-cli.py`:

    tts-cli.py --help
    usage: tts-cli.py [-h] (-t TEXT | -f FILE) [-l LANG] [--debug] destination

(Ex.) Read the string 'Hello' in English:

    $ tts-cli.py -t "Hello" -l 'en' hello.mp3

(Ex.) Read the contents of file 'hello.txt' in Czech:

    $ tts-cli.py -f hello.txt -l 'cs' hello.mp3

Supported Languages
-------------------

  * 'af' : 'Afrikaans'
  * 'sq' : 'Albanian'
  * 'ar' : 'Arabic'
  * 'hy' : 'Armenian'
  * 'ca' : 'Catalan'
  * 'zh-CN' : 'Mandarin (simplified)'
  * 'zh-TW' : 'Mandarin (traditional)'
  * 'hr' : 'Croatian'
  * 'cs' : 'Czech'
  * 'da' : 'Danish'
  * 'nl' : 'Dutch'
  * 'en' : 'English'
  * 'eo' : 'Esperanto'
  * 'fi' : 'Finnish'
  * 'fr' : 'French'
  * 'de' : 'German'
  * 'el' : 'Greek'
  * 'ht' : 'Haitian Creole'
  * 'hi' : 'Hindi'
  * 'hu' : 'Hungarian'
  * 'is' : 'Icelandic'
  * 'id' : 'Indonesian'
  * 'it' : 'Italian'
  * 'ja' : 'Japanese'
  * 'ko' : 'Korean'
  * 'la' : 'Latin'
  * 'lv' : 'Latvian'
  * 'mk' : 'Macedonian'
  * 'no' : 'Norwegian'
  * 'pl' : 'Polish'
  * 'pt' : 'Portuguese'
  * 'ro' : 'Romanian'
  * 'ru' : 'Russian'
  * 'sr' : 'Serbian'
  * 'sk' : 'Slovak'
  * 'es' : 'Spanish'
  * 'sw' : 'Swahili'
  * 'sv' : 'Swedish'
  * 'ta' : 'Tamil'
  * 'th' : 'Thai'
  * 'tr' : 'Turkish'
  * 'vi' : 'Vietnamese'
  * 'cy' : 'Welsh'
