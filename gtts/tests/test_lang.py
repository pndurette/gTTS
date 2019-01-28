# -*- coding: utf-8 -*-
import pytest
from mock import patch

from gtts.lang import tts_langs, _fetch_langs, _extra_langs


"""Test language list downloading"""


def test_fetch_langs():
    """Fetch languages successfully"""
    # Downloaded Languages
    # Safe to assume 'en' (english) will always be there
    scraped_langs = _fetch_langs()
    assert 'en' in scraped_langs

    # Scraping garbage
    assert 'Detect language' not in scraped_langs
    assert '—' not in scraped_langs

    # Add-in Languages
    all_langs = tts_langs()
    extra_langs = _extra_langs()
    assert len(all_langs) == len(scraped_langs) + len(extra_langs)


@patch("gtts.lang.URL_BASE", "http://abc.def.hij.dghj")
def test_fetch_langs_exception():
    """Raise RuntimeError on language fetch exception"""
    with pytest.raises(RuntimeError):
        tts_langs()


if __name__ == '__main__':
    pytest.main(['-x', __file__])
