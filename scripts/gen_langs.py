# -*- coding: utf-8 -*-
import io
import json
import logging
import logging.config
import sys
import uuid

import requests
from gtts import gTTS
from gtts.tts import gTTSError
from gtts.utils import _translate_url

# Logger settings
LOGGER_SETTINGS = {
    "version": 1,
    "formatters": {"default": {"format": "%(name)s - %(levelname)s - %(message)s"}},
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "default"}},
    "loggers": {"gtts": {"handlers": ["console"], "level": "INFO"}},
}

# Logger
logging.config.dictConfig(LOGGER_SETTINGS)
log = logging.getLogger("gtts")


# This file is used to generate the language dict (as a module)
# Usage:
# * Install gTTS
# * $ python gen_langs.py <path to gtts>/langs.py


def _fetch_langs(tld="com"):
    """Fetch all the valid languages from Google Translate.

    There's no easy way to get the list of languages that have TTS voices, so we can just grab the list of languages from Google Translate and try to get a TTS voice for each one, and only keep the ones that work.

    Args:
        tld (string): Top-level domain for the Google Translate host
            to fetch languages from. i.e `https://translate.google.<tld>`.
            The language names obtained will be in a language locale of the TLD
            (e.g. ``tld=fr`` will retrieve the French names of the languages).
            Default is ``com``.

    Returns:
        dict: A dictionary of languages from Google Translate

    """
    LANGUAGES_URL = _translate_url(tld + "/translate_a/l").strip("/")

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/14.0 Safari/605.1.15"
    }
    params = {"client": "t", "alpha": "true"}

    log.info("Getting language list...")
    data = requests.get(LANGUAGES_URL, headers=headers, params=params)
    json = data.json()

    working_languages = {}
    test_text = str(uuid.uuid4())
    for key in json["tl"]:
        try:
            tts = gTTS(test_text, lang=key, lang_check=False)
            tts.write_to_fp(io.BytesIO())
            working_languages[key] = json["tl"][key]
            log.info(f"Added '{key}' ({working_languages[key]})")
        except (gTTSError, ValueError):  # Language not supported
            log.info(f"Rejected '{key}'")

    return working_languages


if __name__ == "__main__":
    """Language list generation 'main'

    CLI to generate the language list as a dict in
    an importable python file/module

    Usage:
        python ./scripts/gen_langs.py ./gTTS/gtts/langs.py

    """

    lang_file_path = sys.argv[1]
    with open(lang_file_path, "w") as f:
        langs = _fetch_langs()

        py_content = f"""# Note: this file is generated
_langs = {json.dumps(langs, indent=4, sort_keys=True)}

def _main_langs():
    return _langs
"""
        log.info(f"Writing to {lang_file_path}...")
        f.write(py_content)
