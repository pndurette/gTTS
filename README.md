# gTTS

**gTTS** (_Google Text to Speech_): a *Python* interface for Google's _Text to Speech_ API. Create an _mp3_ file with the `gTTS` module or `gtts-cli` command line utility. It allows unlimited lengths to be spoken by tokenizing long sentences where the speech would naturally pause.

[![Build Status](https://travis-ci.org/pndurette/gTTS.svg?branch=master)](https://travis-ci.org/pndurette/gTTS)

## Install

    pip install gTTS

### Install on Ubuntu

    sudo pip install setuptools gTTS

## Usage

You may either use `gTTS` as a **__python module__** or as a **__command-line utility__**

### A. Module

##### 1. Import `gTTS`

```
>> from gtts import gTTS
```

##### 2. Create an instance

```
>> tts = gTTS(text='Hello', lang='en')
```

###### _Parameters:_
*  `text` - Text to be spoken (written to file instead)
*  `lang` - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in

##### 3. Write to a file

* Using [`save(file_name)`](https://github.com/pndurette/gTTS/blob/master/gtts/tts.py#L91)
   
```
>> tts.save("hello.mp3")
```

* Using [`write_to_fp(file_object)`](https://github.com/pndurette/gTTS/blob/master/gtts/tts.py#L97)
   
```  
>> from gtts import gTTS
>> from tempfile import TemporaryFile
>> tts = gTTS(text='Hello', lang='en')
>> f = TemporaryFile()
>> tts.write_to_fp(f)
>> f.close()
```

### B. Command line utility

##### Command
```
gtts-cli.py [-h] (["text to speak"] | -f FILE) [-l LANG] [--debug] [-o destination_file]
```
 
###### _Example:_
  
```
$ # Read the string 'Hello' in English to hello.mp3
$ gtts-cli.py "Hello" -l 'en' -o hello.mp3

$ # Read the contents of file 'hello.txt' in Czech to hello.mp3:
$ gtts-cli.py -f hello.txt -l 'cs' -o hello.mp3
```

##Supported Languages<a name="lang_list"></a>

  * 'af' : 'Afrikaans'
  * 'sq' : 'Albanian'
  * 'ar' : 'Arabic'
  * 'hy' : 'Armenian'
  * 'bn' : 'Bengali'
  * 'ca' : 'Catalan'
  * 'zh' : 'Chinese'
  * 'zh-cn' : 'Chinese (Mandarin/China)'
  * 'zh-tw' : 'Chinese (Mandarin/Taiwan)'
  * 'zh-yue' : 'Chinese (Cantonese)'
  * 'hr' : 'Croatian'
  * 'cs' : 'Czech'
  * 'da' : 'Danish'
  * 'nl' : 'Dutch'
  * 'en' : 'English'
  * 'en-au' : 'English (Australia)'
  * 'en-uk' : 'English (United Kingdom)'
  * 'en-us' : 'English (United States)'
  * 'eo' : 'Esperanto'
  * 'fi' : 'Finnish'
  * 'fr' : 'French'
  * 'de' : 'German'
  * 'el' : 'Greek'
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
  * 'pt-br' : 'Portuguese (Brazil)'
  * 'ro' : 'Romanian'
  * 'ru' : 'Russian'
  * 'sr' : 'Serbian'
  * 'sk' : 'Slovak'
  * 'es' : 'Spanish'
  * 'es-es' : 'Spanish (Spain)'
  * 'es-us' : 'Spanish (United States)'
  * 'sw' : 'Swahili'
  * 'sv' : 'Swedish'
  * 'ta' : 'Tamil'
  * 'th' : 'Thai'
  * 'tr' : 'Turkish'
  * 'vi' : 'Vietnamese'
  * 'cy' : 'Welsh'

Contributing
------------

1. _Fork_ [pndurette/gTTS](https://github.com/pndurette/gTTS) on GitHub and clone it locally
2. Make sure you write tests for new features or modify the existing ones if necessary
3. Open a new _Pull Request_ from your feature branch to the `develop` branch.
4. Thank you!
