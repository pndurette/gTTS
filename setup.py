from setuptools import setup
from codecs import open
import site

# PEP517
site.ENABLE_USER_SITE = True

exec(open('gtts/version.py').read())

setup(
    version=__version__,   # type: ignore # noqa: F821
    test_suite='gtts.tests',
)
