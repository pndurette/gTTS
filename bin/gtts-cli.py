#! /usr/bin/python

from gtts import gTTS
from gtts import __version__
import argparse

def languages():
    """Sorted pretty printed string of supported languages"""
    return ", ".join(sorted("{}: '{}'".format(v,k) for k,v in gTTS.LANGUAGES.iteritems()))

# Args
desc = "Creates an mp3 file from spoken text via the Google Text-to-Speech API ({v})".format(v=__version__)
parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)
text_group = parser.add_mutually_exclusive_group(required=True)
text_group.add_argument('-t', '--text', help="text to speak")
text_group.add_argument('-f', '--file', help="file to speak")
args = parser.add_argument("destination", help="destination mp3 file", action='store')
args = parser.add_argument('-l', '--lang', default='en', help="ISO 639-1/IETF language tag to speak in:\n" + languages())
args = parser.add_argument('--debug', default=False, action="store_true")
args = parser.parse_args()

try:
    if args.text:
        text = args.text
    else:
        with open(args.file, "r") as f:
            text = f.read()

    # TTSTF (Text to Speech to File)
    tts = gTTS(text=text, lang=args.lang, debug=args.debug)
    tts.save(args.destination)
except Exception as e:
    print(str(e))
