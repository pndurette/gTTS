gTTS
====

**gTTS** (*Google Text to Speech*): a *Python* interface for Google's
*Text to Speech* API. Create an *mp3* file with the ``gTTS`` module or
``gtts-cli`` command line utility. It allows unlimited lengths to be
spoken by tokenizing long sentences where the speech would naturally
pause.

|Build Status| |PyPI version| |AppVeyor|

Install
-------

::

    pip install gTTS

Usage
-----

You may either use ``gTTS`` as a ****python module**** or as a
****command-line utility****

A. Module
~~~~~~~~~

1. Import ``gTTS``
''''''''''''''''''

::

    >> from gtts import gTTS

2. Create an instance
'''''''''''''''''''''

::

    >> tts = gTTS(text='Hello', lang='en', slow=True)

*Parameters:*
             

-  ``text`` - String - Text to be spoken.
-  ``lang`` - String - `ISO 639-1 language code <#lang_list>`__
   (supported by the Google *Text to Speech* API) to speak in.
-  ``slow`` - Boolean - Speak slowly. Default ``False`` (Note: only two
   speeds are provided by the API).

3. Write to a file
''''''''''''''''''

-  *To disk* using ``save(file_name)``

::

    >> tts.save("hello.mp3")

-  *To a file pointer* using ``write_to_fp(file_object)``

::

    >> f = TemporaryFile()
    >> tts.write_to_fp(f)
    >> # <Do something with f>
    >> f.close()

B. Command line utility
~~~~~~~~~~~~~~~~~~~~~~~

Command
'''''''

::

    gtts-cli.py [-h] (["text to speak"] | -f FILE) [-l LANG] [--slow] [--debug] [-o destination_file]

*Example:*
          

::

    $ # Read the string 'Hello' in English to hello.mp3
    $ gtts-cli "Hello" -l 'en' -o hello.mp3

    $ # Read the string 'Hello' in English (slow speed) to hello.mp3
    $ gtts-cli "Hello" -l 'en' -o hello.mp3 --slow

    $ # Read the contents of file 'hello.txt' in Czech to hello.mp3:
    $ gtts-cli -f hello.txt -l 'cs' -o hello.mp3

    $ # Read the string 'Hello' from stdin in English to hello.mp3
    $ echo "Hello" | gtts-cli -l 'en' -o hello.mp3 -

Supported Languages 
--------------------

-  'af' : 'Afrikaans'
-  'sq' : 'Albanian'
-  'ar' : 'Arabic'
-  'hy' : 'Armenian'
-  'bn' : 'Bengali'
-  'ca' : 'Catalan'
-  'zh' : 'Chinese'
-  'zh-cn' : 'Chinese (Mandarin/China)'
-  'zh-tw' : 'Chinese (Mandarin/Taiwan)'
-  'zh-yue' : 'Chinese (Cantonese)'
-  'hr' : 'Croatian'
-  'cs' : 'Czech'
-  'da' : 'Danish'
-  'nl' : 'Dutch'
-  'en' : 'English'
-  'en-au' : 'English (Australia)'
-  'en-uk' : 'English (United Kingdom)'
-  'en-us' : 'English (United States)'
-  'eo' : 'Esperanto'
-  'fi' : 'Finnish'
-  'fr' : 'French'
-  'de' : 'German'
-  'el' : 'Greek'
-  'hi' : 'Hindi'
-  'hu' : 'Hungarian'
-  'is' : 'Icelandic'
-  'id' : 'Indonesian'
-  'it' : 'Italian'
-  'ja' : 'Japanese'
-  'km' : 'Khmer (Cambodian)'
-  'ko' : 'Korean'
-  'la' : 'Latin'
-  'lv' : 'Latvian'
-  'mk' : 'Macedonian'
-  'no' : 'Norwegian'
-  'pl' : 'Polish'
-  'pt' : 'Portuguese'
-  'ro' : 'Romanian'
-  'ru' : 'Russian'
-  'sr' : 'Serbian'
-  'si' : 'Sinhala'
-  'sk' : 'Slovak'
-  'es' : 'Spanish'
-  'es-es' : 'Spanish (Spain)'
-  'es-us' : 'Spanish (United States)'
-  'sw' : 'Swahili'
-  'sv' : 'Swedish'
-  'ta' : 'Tamil'
-  'th' : 'Thai'
-  'tr' : 'Turkish'
-  'uk' : 'Ukrainian'
-  'vi' : 'Vietnamese'
-  'cy' : 'Welsh'

Contributing
------------

1. *Fork* `pndurette/gTTS <https://github.com/pndurette/gTTS>`__ on
   GitHub and clone it locally
2. Make sure you write tests for new features or modify the existing
   ones if necessary
3. Open a new *Pull Request* from your feature branch to the ``master``
   branch.
4. Thank you!

.. |Build Status| image:: https://travis-ci.org/pndurette/gTTS.svg?branch=master
   :target: https://travis-ci.org/pndurette/gTTS
.. |PyPI version| image:: https://badge.fury.io/py/gTTS.svg
   :target: https://badge.fury.io/py/gTTS
.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/eiuxodugo78kemff?svg=true
   :target: https://ci.appveyor.com/project/pndurette/gtts
