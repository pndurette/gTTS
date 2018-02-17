from __future__ import print_function
from gtts import gTTS
from gtts import Languages
from gtts import __version__
import sys
import argparse
import os
import codecs

def languages():
    """Sorted pretty printed string of supported languages"""
    langs = Languages().get()
    return "\n".join(sorted("{}: '{}'".format(langs[k], k) for k in langs))

def parse_args(sysargs):
    desc = "Creates an mp3 file from spoken text via the Google Text-to-Speech API ({v})".format(v=__version__)
    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)

    text_group = parser.add_mutually_exclusive_group(required=True)
    text_group.add_argument('text', nargs='?', help="text to speak")
    text_group.add_argument('-f', '--file', help="file to speak")

    parser.add_argument("-o", '--destination', help="destination mp3 file", action='store')
    parser.add_argument('-l', '--lang', default='en', help="ISO 639-1/IETF language tag to speak in:\n" + languages())
    parser.add_argument('-x', '--nocheck', action="store_false", help="disable language check")
    parser.add_argument('-s', '--slow', action="store_true", help="slower read speed")
    parser.add_argument('-d', '--debug', action="store_true")

    return parser.parse_args(sysargs)

def tts_cli(args):
    try:
        if args.text:
            if args.text == "-":
                text = sys.stdin.read()
            else:
                text = args.text
        else:
            with codecs.open(args.file, "r", "utf-8") as f:
                text = f.read()

        # TTSTF (Text to Speech to File)
        tts = gTTS(text=text, lang=args.lang, slow=args.slow,
                  lang_check=args.nocheck, debug=args.debug)

        if args.destination:
            tts.save(args.destination)
        else:
            tts.write_to_fp(os.fdopen(sys.stdout.fileno(), "wb"))
    except Exception as e:
        if args.destination:
            print(str(e))
        else:
            print("ERROR: ", e, file=sys.stderr)

def main():
    parsed_args = parse_args(sys.argv[1:])
    tts_cli(parsed_args)

if __name__ == '__main__':
    main()
