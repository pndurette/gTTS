# -*- coding: utf-8 -*-
"""
allow servers other than translate.google.COM
"""
import logging
log = logging.getLogger(__name__)


def server(country_code=None):
    """ ISO Alpha country code """

    url = "https://translate.google.com"

    if not country_code:
        pass
    elif country_code in ("CN", "CHN"):
        url = "https://translate.google.cn"
    elif country_code == "invalid":
        """ https://tools.ietf.org/html/rfc2606 """
        url = "https://translate.invalid"
    else:
        log.warning("Unknown country code {}, falling back to default URL".format(country_code))

    return {'max_chars': 100,  # Max characters the Google TTS API takes at a time
            'url': "{}/translate_tts".format(url),
            'url_base': url,
            'headers': {"Referer": "http://translate.google.com/",
                        "User-Agent":
                            "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/47.0.2526.106 Safari/537.36"
                        }
            }
