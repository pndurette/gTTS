try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

exec(open('gtts/version.py').read())

setup(
    name='gTTS',
    version=__version__,
    author='Pierre Nicolas Durette',
    author_email='pndurette@gmail.com',
    url='https://github.com/pndurette/gTTS',
    packages=['gtts'],
    scripts=['bin/gtts-cli', 'bin/gtts-cli.py'],
    license='MIT',
    description='Create an mp3 file from spoken text via the Google TTS (Text-to-Speech) API',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests"
    ]
)
