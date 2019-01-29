# -*- coding: utf-8 -*-
import pytest

from gtts.lang import tts_langs, _fetch_langs, _extra_langs


"""Test language list downloading"""


@pytest.mark.parametrize("country_code", [None, "CN"])
def test_fetch_langs(country_code):
    """Fetch languages successfully"""
    # Downloaded Languages
    # Safe to assume 'en' (english) will always be there
    scraped_langs = _fetch_langs(country_code)
    if 'en' not in scraped_langs:
        if country_code == 'CN':
            pytest.xfail('scraping not yet enabled for CN server')
        else:
            raise AssertionError

    # Scraping garbage
    assert 'Detect language' not in scraped_langs
    assert '—' not in scraped_langs

    # Add-in Languages
    all_langs = tts_langs(country_code)
    extra_langs = _extra_langs()
    assert len(all_langs) == len(scraped_langs) + len(extra_langs)


def test_fetch_langs_exception():
    """Raise RuntimeError on language fetch exception
    """
    with pytest.raises(RuntimeError):
        tts_langs(country_code="invalid")


if __name__ == '__main__':
    pytest.main(['-x', __file__])
