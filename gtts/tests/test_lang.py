# -*- coding: utf-8 -*-
import pytest
from gtts.lang import tts_langs, _main_langs, _extra_langs


"""Test language list downloading"""


@pytest.mark.net
def test_main_langs():
    """Fetch languages successfully"""
    # Downloaded Languages
    # Safe to assume 'en' (english) will always be there
    scraped_langs = _main_langs()
    assert 'en' in scraped_langs

    # Add-in Languages
    all_langs = tts_langs()
    extra_langs = _extra_langs()
    assert len(all_langs) == len(scraped_langs) + len(extra_langs)


if __name__ == '__main__':
    pytest.main(['-x', __file__])
