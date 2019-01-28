from setuptools import setup
from codecs import open

exec(open('gtts/version.py').read())

setup(
    version=__version__,   # type: ignore # noqa: F821
    test_suite='gtts.tests',
)
