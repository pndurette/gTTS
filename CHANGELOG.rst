.. NOTE: You should *NOT* be adding new change log entries to this file, this
         file is managed by towncrier. You *may* edit previous change logs to
         fix problems like typo corrections or such.

         To add a new change log entry, please see CONTRIBUTING.rst

Changelog
=========

.. towncrier release notes start

2.2.2 (2021-02-03)
------------------

Features
~~~~~~~~

- Adds a language fallback feature for deprecated languages to maintain compatiblity  (e.g. ``en-us`` becomes ``en``). Fallback can be disabled with ``lang_check=False`` or ``--nocheck`` for the cli (`#267 <https://github.com/pndurette/gTTS/issues/267>`_)


Bugfixes
~~~~~~~~

- Fix Python 2.7 compatiblity (!). Python 2 is long gone, but the cut wasn't clearly communicated for gTTS, so it was restored. Python 2 support will be completely removed in the next major release. (`#255 <https://github.com/pndurette/gTTS/issues/255>`_)
- Language code case sensitivity is maintained throughout (`#267 <https://github.com/pndurette/gTTS/issues/267>`_)


Deprecations and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~

- The following list of 'hyphenated' language codes no longer work and have been removed: ``en-us``, ``en-ca``, ``en-uk``, ``en-gb``, ``en-au``, ``en-gh``, ``en-in``, ``en-ie``, ``en-nz``, ``en-ng``, ``en-ph``, ``en-za``, ``en-tz``, ``fr-ca``, ``fr-fr``, ``pt-br``, ``pt-pt``, ``es-es``, ``es-us``, ``zh-cn``, ``zh-tw`` (`#267 <https://github.com/pndurette/gTTS/issues/267>`_)
- Removed the ``gtts.get_url()`` method (outdated since ``2.1.0``) (`#270 <https://github.com/pndurette/gTTS/issues/270>`_)


2.2.1 (2020-11-15)
------------------

Bugfixes
~~~~~~~~

- ``_package_rpc()`` was erroneously packaging the entire text instead of tokenized part (`#252 <https://github.com/pndurette/gTTS/issues/252>`_)


Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Removes reference to automatic retrieval of languages (`#250 <https://github.com/pndurette/gTTS/issues/250>`_)


Misc
~~~~

- `#251 <https://github.com/pndurette/gTTS/issues/251>`_


2.2.0 (2020-11-14)
------------------

Features
~~~~~~~~

- Switch to the newer Google TTS API (thanks to `@Boudewijn26! <https://github.com/pndurette/gTTS/pull/244>`_). See `his great writeup <https://github.com/Boudewijn26/gTTS-token/blob/master/docs/november-2020-translate-changes.md>`_ for more on the methodology and why this was necessary. (`#226 <https://github.com/pndurette/gTTS/issues/226>`_, `#232 <https://github.com/pndurette/gTTS/issues/232>`_, `#236 <https://github.com/pndurette/gTTS/issues/236>`_, `#241 <https://github.com/pndurette/gTTS/issues/241>`_)


Deprecations and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~

- Removed automatic language download from the main code, which has become too unreliable & slow.
  Languages will still be fetched but a pre-generated list will be shipped with ``gTTS``. (`#233 <https://github.com/pndurette/gTTS/issues/233>`_, `#241 <https://github.com/pndurette/gTTS/issues/241>`_, `#242 <https://github.com/pndurette/gTTS/issues/242>`_, `#243 <https://github.com/pndurette/gTTS/issues/243>`_)
- Because languages are now pre-generated, removed custom TLD support for language URL (which allowed to get language **names** in other than English) (`#245 <https://github.com/pndurette/gTTS/issues/245>`_)


Misc
~~~~

- `#245 <https://github.com/pndurette/gTTS/issues/245>`_


2.1.2 (2020-11-10)
------------------

Features
~~~~~~~~

- Update `gTTS-token` to `1.1.4` (`#238 <https://github.com/pndurette/gTTS/issues/238>`_)


Bugfixes
~~~~~~~~

- Fixed an issue where some tokens could be empty after minimization (`#229 <https://github.com/pndurette/gTTS/issues/229>`_, `#239 <https://github.com/pndurette/gTTS/issues/239>`_)


Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Grammar, spelling and example fixes (`#227 <https://github.com/pndurette/gTTS/issues/227>`_)


Misc
~~~~

- `#218 <https://github.com/pndurette/gTTS/issues/218>`_, `#230 <https://github.com/pndurette/gTTS/issues/230>`_, `#231 <https://github.com/pndurette/gTTS/issues/231>`_, `#239 <https://github.com/pndurette/gTTS/issues/239>`_


2.1.1 (2020-01-25)
------------------

Bugfixes
~~~~~~~~

- Debug mode now uses a copy of locals() to prevent RuntimeError (`#213 <https://github.com/pndurette/gTTS/issues/213>`_)


2.1.0 (2020-01-01)
------------------

Features
~~~~~~~~

- The ``gtts`` module

  - Added the ability to customize the Google Translate URL hostname.
    This is useful when ``google.com`` might be blocked within a network but
    a local or different Google host (e.g. ``google.cn``) is not
    (`#143 <https://github.com/pndurette/gTTS/issues/143>`_, `#203 <https://github.com/pndurette/gTTS/issues/203>`_):

    - New ``gTTS()`` parameter ``tld`` to specify the top-level
      domain to use for the Google hostname, i.e ``https://translate.google.<tld>``
      (default: ``com``).
    - Languages are also now fetched using the same customized hostname.

  - Pre-generated TTS API request URLs can now be obtained instead of
    writing an ``mp3`` file to disk (for example to be used in an
    external program):

    - New ``get_urls()`` method returns the list of URLs generated by ``gTTS``,
      which can be used in lieu of ``write_to_fp()`` or ``save()``.

- The ``gtts-cli`` command-line tool

  - New ``--tld`` option to match the new ``gtts`` customizable hostname (`#200 <https://github.com/pndurette/gTTS/issues/200>`_, `#207 <https://github.com/pndurette/gTTS/issues/207>`_)

- Other

  - Added Python 3.8 support (`#204 <https://github.com/pndurette/gTTS/issues/204>`_)


Bugfixes
~~~~~~~~

- Changed default word-for-word pre-processor (``('M.', 'Monsieur')``) which would substitute any 'm.' for 'monsieur' (e.g. 'them.' became 'themonsieur') (`#197 <https://github.com/pndurette/gTTS/issues/197>`_)


Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Added examples for newer features (`#205 <https://github.com/pndurette/gTTS/issues/205>`_, `#207 <https://github.com/pndurette/gTTS/issues/207>`_)


Misc
~~~~

- `#204 <https://github.com/pndurette/gTTS/issues/204>`_, `#205 <https://github.com/pndurette/gTTS/issues/205>`_, `#207 <https://github.com/pndurette/gTTS/issues/207>`_


2.0.4 (2019-08-29)
------------------

Features
~~~~~~~~

- gTTS is now built as a wheel package (Python 2 & 3) (`#181 <https://github.com/pndurette/gTTS/issues/181>`_)


Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Fixed bad example in docs (`#163 <https://github.com/pndurette/gTTS/issues/163>`_, `#166 <https://github.com/pndurette/gTTS/issues/166>`_)


Misc
~~~~

- `#164 <https://github.com/pndurette/gTTS/issues/164>`_, `#171 <https://github.com/pndurette/gTTS/issues/171>`_, `#173 <https://github.com/pndurette/gTTS/issues/173>`_, `#185 <https://github.com/pndurette/gTTS/issues/185>`_


2.0.3 (2018-12-15)
------------------

Features
~~~~~~~~

- Added new tokenizer case for ':' preventing cut in the middle of a time notation (`#135 <https://github.com/pndurette/gTTS/issues/135>`_)


Misc
~~~~

- `#159 <https://github.com/pndurette/gTTS/issues/159>`_


2.0.2 (2018-12-09)
------------------

Features
~~~~~~~~

- Added Python 3.7 support, modernization of packaging, testing and CI (`#126 <https://github.com/pndurette/gTTS/issues/126>`_)


Bugfixes
~~~~~~~~

- Fixed language retrieval/validation broken from new Google Translate page (`#156 <https://github.com/pndurette/gTTS/issues/156>`_)


2.0.1 (2018-06-20)
------------------

Bugfixes
~~~~~~~~

- Fixed an UnicodeDecodeError when installing gTTS if system locale was not
  utf-8 (`#120 <https://github.com/pndurette/gTTS/issues/120>`_)


Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Added *Pre-processing and tokenizing > Minimizing* section about the API's
  100 characters limit and how larger tokens are handled (`#121
  <https://github.com/pndurette/gTTS/issues/121>`_)


Misc
~~~~

- `#122 <https://github.com/pndurette/gTTS/issues/122>`_


2.0.0 (2018-04-30)
------------------
(`#108 <https://github.com/pndurette/gTTS/issues/108>`_)

Features
~~~~~~~~

- The ``gtts`` module

  - New logger ("gtts") replaces all occurrences of ``print()``
  - Languages list is now obtained automatically (``gtts.lang``)
    (`#91 <https://github.com/pndurette/gTTS/issues/91>`_,
    `#94 <https://github.com/pndurette/gTTS/issues/94>`_,
    `#106 <https://github.com/pndurette/gTTS/issues/106>`_)
  - Added a curated list of language sub-tags that
    have been observed to provide different dialects or accents
    (e.g. "en-gb", "fr-ca")
  - New ``gTTS()`` parameter ``lang_check`` to disable language
    checking.
  - ``gTTS()`` now delegates the ``text`` tokenizing to the
    API request methods (i.e. ``write_to_fp()``, ``save()``),
    allowing ``gTTS`` instances to be modified/reused
  - Rewrote tokenizing and added pre-processing (see below)
  - New ``gTTS()`` parameters ``pre_processor_funcs`` and
    ``tokenizer_func`` to configure pre-processing and tokenizing
    (or use a 3rd party tokenizer)
  - Error handling:

    - Added new exception ``gTTSError`` raised on API request errors.
      It attempts to guess what went wrong based on known information
      and observed behaviour
      (`#60 <https://github.com/pndurette/gTTS/issues/60>`_,
      `#106 <https://github.com/pndurette/gTTS/issues/106>`_)
    - ``gTTS.write_to_fp()`` and ``gTTS.save()`` also raise ``gTTSError``
      on `gtts_token` error
    - ``gTTS.write_to_fp()`` raises ``TypeError`` when ``fp`` is not a
      file-like object or one that doesn't take bytes
    - ``gTTS()`` raises ``ValueError`` on unsupported languages
      (and ``lang_check`` is ``True``)
    - More fine-grained error handling throughout (e.g.
      `request failed` vs. `request successful with a bad response`)

- Tokenizer (and new pre-processors):

  - Rewrote and greatly expanded tokenizer (``gtts.tokenizer``)
  - Smarter token 'cleaning' that will remove tokens that only contain
    characters that can't be spoken (i.e. punctuation and whitespace)
  - Decoupled token minimizing from tokenizing, making the latter usable
    in other contexts
  - New flexible speech-centric text pre-processing
  - New flexible full-featured regex-based tokenizer
    (``gtts.tokenizer.core.Tokenizer``)
  - New ``RegexBuilder``, ``PreProcessorRegex`` and ``PreProcessorSub`` classes
    to make writing regex-powered text `pre-processors` and `tokenizer cases`
    easier
  - Pre-processors:

    - Re-form words cut by end-of-line hyphens
    - Remove periods after a (customizable) list of known abbreviations
      (e.g. "jr", "sr", "dr") that can be spoken the same without a period
    - Perform speech corrections by doing word-for-word replacements
      from a (customizable) list of tuples

  - Tokenizing:

    - Keep punctuation that modify the inflection of speech (e.g. "?", "!")
    - Don't split in the middle of numbers (e.g. "10.5", "20,000,000")
      (`#101 <https://github.com/pndurette/gTTS/issues/101>`_)
    - Don't split on "dotted" abbreviations and accronyms (e.g. "U.S.A")
    - Added Chinese comma ("，"), ellipsis ("…") to punctuation list
      to tokenize on (`#86 <https://github.com/pndurette/gTTS/issues/86>`_)

- The ``gtts-cli`` command-line tool

  - Rewrote cli as first-class citizen module (``gtts.cli``),
    powered by `Click <http://click.pocoo.org>`_
  - Windows support using `setuptool`'s `entry_points`
  - Better support for Unicode I/O in Python 2
  - All arguments are now pre-validated
  - New ``--nocheck`` flag to skip language pre-checking
  - New ``--all`` flag to list all available languages
  - Either the ``--file`` option or the ``<text>`` argument can be set to
    "-" to read from ``stdin``
  - The ``--debug`` flag uses logging and doesn't pollute ``stdout``
    anymore


Bugfixes
~~~~~~~~

- ``_minimize()``: Fixed an infinite recursion loop that would occur
  when a token started with the miminizing delimiter (i.e. a space)
  (`#86 <https://github.com/pndurette/gTTS/issues/86>`_)
- ``_minimize()``: Handle the case where a token of more than 100
  characters did not contain a space (e.g. in Chinese).
- Fixed an issue that fused multiline text together if the total number of
  characters was less than 100
- Fixed ``gtts-cli`` Unicode errors in Python 2.7 (famous last words)
  (`#78 <https://github.com/pndurette/gTTS/issues/78>`_,
  `#93 <https://github.com/pndurette/gTTS/issues/93>`_,
  `#96 <https://github.com/pndurette/gTTS/issues/96>`_)


Deprecations and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~

- Dropped Python 3.3 support
- Removed ``debug`` parameter of ``gTTS`` (in favour of logger)
- ``gtts-cli``: Changed long option name of ``-o`` to ``--output``
  instead of ``--destination``
- ``gTTS()`` will raise a ``ValueError`` rather than an ``AssertionError``
  on unsupported language


Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Rewrote all documentation files as reStructuredText
- Comprehensive documentation writen for `Sphinx <http://www.sphinx-doc.org>`_, published to http://gtts.readthedocs.io
- Changelog built with `towncrier <https://github.com/hawkowl/towncrier>`_

Misc
~~~~

- Major test re-work
- Language tests can read a ``TEST_LANGS`` enviromment variable so
  not all language tests are run every time.
- Added `AppVeyor <https://www.appveyor.com>`_ CI for Windows
- `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ compliance


1.2.2 (2017-08-15)
------------------

Misc
~~~~

- Update LICENCE, add to manifest (`#77 <https://github.com/pndurette/gTTS/issues/77>`_)


1.2.1 (2017-08-02)
------------------

Features
~~~~~~~~

- Add Unicode punctuation to the tokenizer (such as for Chinese and Japanese)
  (`#75 <https://github.com/pndurette/gTTS/issues/75>`_)


Bugfixes
~~~~~~~~

- Fix > 100 characters non-ASCII split, ``unicode()`` for Python 2 (`#71
  <https://github.com/pndurette/gTTS/issues/71>`_, `#73
  <https://github.com/pndurette/gTTS/issues/73>`_, `#75
  <https://github.com/pndurette/gTTS/issues/75>`_)


1.2.0 (2017-04-15)
------------------

Features
~~~~~~~~

- Option for slower read speed (``slow=True`` for ``gTTS()``, ``--slow`` for
  ``gtts-cli``) (`#40 <https://github.com/pndurette/gTTS/issues/40>`_, `#41
  <https://github.com/pndurette/gTTS/issues/41>`_, `#64
  <https://github.com/pndurette/gTTS/issues/64>`_, `#67
  <https://github.com/pndurette/gTTS/issues/67>`_)
- System proxy settings are passed transparently to all http requests (`#45
  <https://github.com/pndurette/gTTS/issues/45>`_, `#68
  <https://github.com/pndurette/gTTS/issues/68>`_)
- Silence SSL warnings from urllib3 (`#69
  <https://github.com/pndurette/gTTS/issues/69>`_)


Bugfixes
~~~~~~~~

- The text to read is now cut in proper chunks in Python 2 unicode. This
  broke reading for many languages such as Russian.
- Disabled SSL verify on http requests to accommodate certain firewalls
  and proxies.
- Better Python 2/3 support in general (`#9 <https://github.com/pndurette/gTTS/issues/9>`_,
  `#48 <https://github.com/pndurette/gTTS/issues/48>`_, `#68
  <https://github.com/pndurette/gTTS/issues/68>`_)


Deprecations and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~

- 'pt-br' : 'Portuguese (Brazil)' (it was the same as 'pt' and not Brazilian)
  (`#69 <https://github.com/pndurette/gTTS/issues/69>`_)


1.1.8 (2017-01-15)
------------------

Features
~~~~~~~~

- Added ``stdin`` support via the '-' ``text`` argument to ``gtts-cli`` (`#56
  <https://github.com/pndurette/gTTS/issues/56>`_)


1.1.7 (2016-12-14)
------------------

Features
~~~~~~~~

- Added utf-8 support to ``gtts-cli`` (`#52
  <https://github.com/pndurette/gTTS/issues/52>`_)


1.1.6 (2016-07-20)
------------------

Features
~~~~~~~~

- Added 'bn' : 'Bengali' (`#39 <https://github.com/pndurette/gTTS/issues/39>`_,
  `#44 <https://github.com/pndurette/gTTS/issues/44>`_)


Deprecations and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~

- 'ht' : 'Haitian Creole' (removed by Google) (`#43
  <https://github.com/pndurette/gTTS/issues/43>`_)


1.1.5 (2016-05-13)
------------------

Bugfixes
~~~~~~~~

- Fixed HTTP 403s by updating the client argument to reflect new API usage
  (`#32 <https://github.com/pndurette/gTTS/issues/32>`_, `#33
  <https://github.com/pndurette/gTTS/issues/33>`_)


1.1.4 (2016-02-22)
------------------

Features
~~~~~~~~

- Spun-off token calculation to `gTTS-Token
  <https://github.com/Boudewijn26/gTTS-token>`_ (`#23
  <https://github.com/pndurette/gTTS/issues/23>`_, `#29
  <https://github.com/pndurette/gTTS/issues/29>`_)


1.1.3 (2016-01-24)
------------------

Bugfixes
~~~~~~~~

- ``gtts-cli`` works with Python 3 (`#20
  <https://github.com/pndurette/gTTS/issues/20>`_)
- Better support for non-ASCII characters (`#21
  <https://github.com/pndurette/gTTS/issues/21>`_, `#22
  <https://github.com/pndurette/gTTS/issues/22>`_)


Misc
~~~~

- Moved out gTTS token to its own module (`#19 <https://github.com/pndurette/gTTS/issues/19>`_)


1.1.2 (2016-01-13)
------------------

Features
~~~~~~~~

- Added gTTS token (tk url parameter) calculation (`#14
  <https://github.com/pndurette/gTTS/issues/14>`_, `#15
  <https://github.com/pndurette/gTTS/issues/15>`_, `#17
  <https://github.com/pndurette/gTTS/issues/17>`_)


1.0.7 (2015-10-07)
------------------

Features
~~~~~~~~

- Added ``stdout`` support to ``gtts-cli``, text now an argument rather than an
  option (`#10 <https://github.com/pndurette/gTTS/issues/10>`_)


1.0.6 (2015-07-30)
------------------

Features
~~~~~~~~

- Raise an exception on bad HTTP response (4xx or 5xx) (`#8
  <https://github.com/pndurette/gTTS/issues/8>`_)


Bugfixes
~~~~~~~~

- Added ``client=t`` parameter for the api HTTP request (`#8
  <https://github.com/pndurette/gTTS/issues/8>`_)


1.0.5 (2015-07-15)
------------------

Features
~~~~~~~~

- ``write_to_fp()`` to write to a file-like object (`#6
  <https://github.com/pndurette/gTTS/issues/6>`_)


1.0.4 (2015-05-11)
------------------

Features
~~~~~~~~

- Added Languages: `zh-yue` : 'Chinese (Cantonese)', `en-uk` : 'English (United
  Kingdom)', `pt-br` : 'Portuguese (Brazil)', `es-es` : 'Spanish (Spain)',
  `es-us` : 'Spanish (United StateS)', `zh-cn` : 'Chinese (Mandarin/China)',
  `zh-tw` : 'Chinese (Mandarin/Taiwan)' (`#4
  <https://github.com/pndurette/gTTS/issues/4>`_)


Bugfixes
~~~~~~~~

- ``gtts-cli`` print version and pretty printed available languages, language
  codes are now case insensitive (`#4 <https://github.com/pndurette/gTTS/issues/4>`_)


1.0.3 (2014-11-21)
------------------

Features
~~~~~~~~

- Added Languages: 'en-us' : 'English (United States)', 'en-au' : 'English
  (Australia)' (`#3 <https://github.com/pndurette/gTTS/issues/3>`_)


1.0.2 (2014-05-15)
------------------

Features
~~~~~~~~

- Python 3 support


1.0.1 (2014-05-15)
------------------

Misc
~~~~

- SemVer versioning, CI changes


1.0 (2014-05-08)
----------------

Features
~~~~~~~~

- Initial release


