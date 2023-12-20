# Changelog

## [2.5.0](https://github.com/pndurette/gTTS/compare/v2.4.0...v2.5.0) (2023-12-20)


### Features

* Add connection timeout + misc improvements ([#440](https://github.com/pndurette/gTTS/issues/440)) ([bcdb79d](https://github.com/pndurette/gTTS/commit/bcdb79df41e76c5c1e4fea6388d0eeb3f0c009f6))

## [2.4.0](https://github.com/pndurette/gTTS/compare/v2.3.2...v2.4.0) (2023-10-03)


### Features

* Add Python 3.12 support  ([75294b2](https://github.com/pndurette/gTTS/commit/75294b227f5c428436215abaf6cddc9f3d10f4de))
* Remove Python 3.7 support (end-of-life) ([75294b2](https://github.com/pndurette/gTTS/commit/75294b227f5c428436215abaf6cddc9f3d10f4de))

## [2.3.2](https://github.com/pndurette/gTTS/compare/v2.3.1...v2.3.2) (2023-04-29)


### Bug Fixes

* Add new error helper for when using a custom (non-`.com`) TLD results in a 404 ([5a860ed](https://github.com/pndurette/gTTS/commit/5a860edd27a6772d7facc384927e3b87439e2ccd))
* **cli:** Add deprecated language fallback support to CLI ([5a860ed](https://github.com/pndurette/gTTS/commit/5a860edd27a6772d7facc384927e3b87439e2ccd))


### Documentation

* **cli:** Fix older invalid example ([5a860ed](https://github.com/pndurette/gTTS/commit/5a860edd27a6772d7facc384927e3b87439e2ccd))

## [2.3.1](https://github.com/pndurette/gTTS/compare/v2.3.0...v2.3.1) (2023-01-16)


### Bug Fixes

* **test:** include missing required `*.txt` test files in dist ([#395](https://github.com/pndurette/gTTS/issues/395)) ([63f10ff](https://github.com/pndurette/gTTS/commit/63f10ff6aec877103c3459fc6d3c261d469b6770))
* loosen dependancies for `click` and `requests`, removes `six` dependancy ([#394](https://github.com/pndurette/gTTS/issues/394)) ([a4ce0c9](https://github.com/pndurette/gTTS/commit/a4ce0c9a26778c079fd49c7e2d89ab03bbc22cc3))
* **test:** missing `@pytest.mark.net` on net-enabled test ([#391](https://github.com/pndurette/gTTS/issues/391)) ([3667f06](https://github.com/pndurette/gTTS/commit/3667f06d16152961df2ff8067384f11be9b327c0))
* **test:** remove `mock` package test dependancy ([#390](https://github.com/pndurette/gTTS/issues/390)) ([9b54fc1](https://github.com/pndurette/gTTS/commit/9b54fc12b7839d3ab3ee0e948df45dfd840061c5))

## [2.3.0](https://github.com/pndurette/gTTS/compare/v2.2.4...v2.3.0) (2022-11-21)


### Features

* centralizes project metadata and config into a single `pyproject.toml` ([25d3c1c](https://github.com/pndurette/gTTS/commit/25d3c1c9ee16da81d1b766b9ee6649831a8a1719))
* drops support for Python 2.7 (long overdue), Python 3.6 (end-of-life) ([25d3c1c](https://github.com/pndurette/gTTS/commit/25d3c1c9ee16da81d1b766b9ee6649831a8a1719))
* modernize package config and build/release workflow ([25d3c1c](https://github.com/pndurette/gTTS/commit/25d3c1c9ee16da81d1b766b9ee6649831a8a1719))
* Simplify language generator ([5dbdf10](https://github.com/pndurette/gTTS/commit/5dbdf105b9ca4639577d8904001581434741fe34))


### Bug Fixes

* Languages added: `zh-CN` (Chinese (Simplified)), `zh-TW` (Chinese (Traditional)) ([5dbdf10](https://github.com/pndurette/gTTS/commit/5dbdf105b9ca4639577d8904001581434741fe34))
* Languages removed: `cy` (Welsh),  `eo` (Esperanto), `mk` (Macedonian), `ms` (Malay), `zh-CN` (Chinese) ([5dbdf10](https://github.com/pndurette/gTTS/commit/5dbdf105b9ca4639577d8904001581434741fe34))


2.2.4 (2022-03-14)
------------------

### Features

-   Added Malay language support ([\#316](https://github.com/pndurette/gTTS/issues/316))
-   Added Hebrew language support ([\#324](https://github.com/pndurette/gTTS/issues/324))
-   Added new `gTTS.stream()` method to stream bytes ([\#319](https://github.com/pndurette/gTTS/issues/319))

### Misc

-   [\#334](https://github.com/pndurette/gTTS/issues/334)

2.2.3 (2021-06-17)
------------------

### Features

-   Added Bulgarian language support ([\#302](https://github.com/pndurette/gTTS/issues/302))

2.2.2 (2021-02-03)
------------------

### Features

-   Adds a language fallback feature for deprecated languages to
    maintain compatiblity (e.g. `en-us` becomes `en`). Fallback can be
    disabled with `lang_check=False` or `--nocheck` for the cli ([\#267](https://github.com/pndurette/gTTS/issues/267))

### Bugfixes

-   Fix Python 2.7 compatiblity (!). Python 2 is long gone, but the cut
    wasn\'t clearly communicated for gTTS, so it was restored. Python 2
    support will be completely removed in the next major release. ([\#255](https://github.com/pndurette/gTTS/issues/255))
-   Language code case sensitivity is maintained throughout ([\#267](https://github.com/pndurette/gTTS/issues/267))

### Deprecations and Removals

-   The following list of \'hyphenated\' language codes no longer work
    and have been removed: `en-us`, `en-ca`, `en-uk`, `en-gb`, `en-au`,
    `en-gh`, `en-in`, `en-ie`, `en-nz`, `en-ng`, `en-ph`, `en-za`,
    `en-tz`, `fr-ca`, `fr-fr`, `pt-br`, `pt-pt`, `es-es`, `es-us`,
    `zh-cn`, `zh-tw` ([\#267](https://github.com/pndurette/gTTS/issues/267))
-   Removed the `gtts.get_url()` method (outdated since `2.1.0`) ([\#270](https://github.com/pndurette/gTTS/issues/270))

2.2.1 (2020-11-15)
------------------

### Bugfixes

-   `_package_rpc()` was erroneously packaging the entire text instead
    of tokenized part ([\#252](https://github.com/pndurette/gTTS/issues/252))

### Improved Documentation

-   Removes reference to automatic retrieval of languages ([\#250](https://github.com/pndurette/gTTS/issues/250))

### Misc

-   [\#251](https://github.com/pndurette/gTTS/issues/251)

2.2.0 (2020-11-14)
------------------

### Features

-   Switch to the newer Google TTS API (thanks to[@Boudewijn26!](https://github.com/pndurette/gTTS/pull/244)). See [his great writeup](https://github.com/Boudewijn26/gTTS-token/blob/master/docs/november-2020-translate-changes.md) for more on the methodology and why this was necessary. ([\#226](https://github.com/pndurette/gTTS/issues/226), [#232](https://github.com/pndurette/gTTS/issues/232), [\#236](https://github.com/pndurette/gTTS/issues/236), [\#241](https://github.com/pndurette/gTTS/issues/241))

### Deprecations and Removals

-   Removed automatic language download from the main code, which has
    become too unreliable & slow. Languages will still be fetched but a
    pre-generated list will be shipped with `gTTS`. ([\#233](https://github.com/pndurette/gTTS/issues/233), [\#241](https://github.com/pndurette/gTTS/issues/241), [\#242](https://github.com/pndurette/gTTS/issues/242), [\#243](https://github.com/pndurette/gTTS/issues/243))
-   Because languages are now pre-generated, removed custom TLD support
    for language URL (which allowed to get language **names** in other
    than English) ([\#245](https://github.com/pndurette/gTTS/issues/245))

### Misc

-   [\#245](https://github.com/pndurette/gTTS/issues/245)

2.1.2 (2020-11-10)
------------------

### Features

-   Update `gTTS-token` to `1.1.4` ([\#238](https://github.com/pndurette/gTTS/issues/238))

### Bugfixes

-   Fixed an issue where some tokens could be empty after minimization ([\#229](https://github.com/pndurette/gTTS/issues/229), [\#239](https://github.com/pndurette/gTTS/issues/239))

### Improved Documentation

-   Grammar, spelling and example fixes ([\#227](https://github.com/pndurette/gTTS/issues/227))

### Misc

-   [\#218](https://github.com/pndurette/gTTS/issues/218), [\#230](https://github.com/pndurette/gTTS/issues/230), [\#231](https://github.com/pndurette/gTTS/issues/231), [\#239](https://github.com/pndurette/gTTS/issues/239)

2.1.1 (2020-01-25)
------------------

### Bugfixes

-   Debug mode now uses a copy of locals() to prevent RuntimeError ([\#213](https://github.com/pndurette/gTTS/issues/213))

2.1.0 (2020-01-01)
------------------

### Features

-   The `gtts` module
    -   Added the ability to customize the Google Translate URL
        hostname. This is useful when `google.com` might be blocked
        within a network but a local or different Google host (e.g.
        `google.cn`) is not ([\#143](https://github.com/pndurette/gTTS/issues/143), [\#203](https://github.com/pndurette/gTTS/issues/203)):
        -   New `gTTS()` parameter `tld` to specify the top-level domain
            to use for the Google hostname, i.e
            `https://translate.google.<tld>` (default: `com`).
        -   Languages are also now fetched using the same customized
            hostname.
    -   Pre-generated TTS API request URLs can now be obtained instead
        of writing an `mp3` file to disk (for example to be used in an
        external program):
        -   New `get_urls()` method returns the list of URLs generated
            by `gTTS`, which can be used in lieu of `write_to_fp()` or
            `save()`.
-   The `gtts-cli` command-line tool
    -   New `--tld` option to match the new `gtts` customizable hostname [\#200](https://github.com/pndurette/gTTS/issues/200), [#207](https://github.com/pndurette/gTTS/issues/207))
-   Other
    -   Added Python 3.8 support ([\#204](https://github.com/pndurette/gTTS/issues/204))

### Bugfixes

-   Changed default word-for-word pre-processor (`('M.', 'Monsieur')`)
    which would substitute any \'m.\' for \'monsieur\' (e.g. \'them.\'
    became \'themonsieur\') ([\#197](https://github.com/pndurette/gTTS/issues/197))

### Improved Documentation

-   Added examples for newer features ([\#205](https://github.com/pndurette/gTTS/issues/205), [\#207](https://github.com/pndurette/gTTS/issues/207))

### Misc

-   [\#204](https://github.com/pndurette/gTTS/issues/204), [\#205](https://github.com/pndurette/gTTS/issues/205), [\#207](https://github.com/pndurette/gTTS/issues/207)

2.0.4 (2019-08-29)
------------------

### Features

-   gTTS is now built as a wheel package (Python 2 & 3) ([\#181](https://github.com/pndurette/gTTS/issues/181))

### Improved Documentation

-   Fixed bad example in docs ([\#163](https://github.com/pndurette/gTTS/issues/163), [\#166](https://github.com/pndurette/gTTS/issues/166))

### Misc

-   [\#164](https://github.com/pndurette/gTTS/issues/164), [\#171](https://github.com/pndurette/gTTS/issues/171), [\#173](https://github.com/pndurette/gTTS/issues/173), [\#185](https://github.com/pndurette/gTTS/issues/185)

2.0.3 (2018-12-15)
------------------

### Features

-   Added new tokenizer case for \':\' preventing cut in the middle of a
    time notation ([\#135](https://github.com/pndurette/gTTS/issues/135))

### Misc

-   [\#159](https://github.com/pndurette/gTTS/issues/159)

2.0.2 (2018-12-09)
------------------

### Features

-   Added Python 3.7 support, modernization of packaging, testing and CI ([\#126](https://github.com/pndurette/gTTS/issues/126))

### Bugfixes

-   Fixed language retrieval/validation broken from new Google Translate
    page ([\#156](https://github.com/pndurette/gTTS/issues/156))

2.0.1 (2018-06-20)
------------------

### Bugfixes

-   Fixed an UnicodeDecodeError when installing gTTS if system locale
    was not utf-8 ([\#120](https://github.com/pndurette/gTTS/issues/120))

### Improved Documentation

-   Added *Pre-processing and tokenizing \> Minimizing* section about
    the API\'s 100 characters limit and how larger tokens are handled ([\#121](https://github.com/pndurette/gTTS/issues/121))

### Misc

-   [\#122](https://github.com/pndurette/gTTS/issues/122)

2.0.0 (2018-04-30)
------------------

([\#108](https://github.com/pndurette/gTTS/issues/108))

### Features

-   The `gtts` module
    -   New logger (\"gtts\") replaces all occurrences of `print()`
    -   Languages list is now obtained automatically (`gtts.lang`) ([\#91](https://github.com/pndurette/gTTS/issues/91), [#94](https://github.com/pndurette/gTTS/issues/94), [\#106](https://github.com/pndurette/gTTS/issues/106))
    -   Added a curated list of language sub-tags that have been
        observed to provide different dialects or accents (e.g.
        \"en-gb\", \"fr-ca\")
    -   New `gTTS()` parameter `lang_check` to disable language
        checking.
    -   `gTTS()` now delegates the `text` tokenizing to the API request
        methods (i.e. `write_to_fp()`, `save()`), allowing `gTTS`
        instances to be modified/reused
    -   Rewrote tokenizing and added pre-processing (see below)
    -   New `gTTS()` parameters `pre_processor_funcs` and
        `tokenizer_func` to configure pre-processing and tokenizing (or
        use a 3rd party tokenizer)
    -   Error handling:
        -   Added new exception `gTTSError` raised on API request
            errors. It attempts to guess what went wrong based on known
            information and observed behaviour ([\#60](https://github.com/pndurette/gTTS/issues/60), [\#106](https://github.com/pndurette/gTTS/issues/106))
        -   `gTTS.write_to_fp()` and `gTTS.save()` also raise
            `gTTSError` on [gtts\_token]{.title-ref} error
        -   `gTTS.write_to_fp()` raises `TypeError` when `fp` is not a
            file-like object or one that doesn\'t take bytes
        -   `gTTS()` raises `ValueError` on unsupported languages (and
            `lang_check` is `True`)
        -   More fine-grained error handling throughout (e.g. [request
            failed]{.title-ref} vs. [request successful with a bad
            response]{.title-ref})
-   Tokenizer (and new pre-processors):
    -   Rewrote and greatly expanded tokenizer (`gtts.tokenizer`)
    -   Smarter token \'cleaning\' that will remove tokens that only
        contain characters that can\'t be spoken (i.e. punctuation and
        whitespace)
    -   Decoupled token minimizing from tokenizing, making the latter
        usable in other contexts
    -   New flexible speech-centric text pre-processing
    -   New flexible full-featured regex-based tokenizer
        (`gtts.tokenizer.core.Tokenizer`)
    -   New `RegexBuilder`, `PreProcessorRegex` and `PreProcessorSub`
        classes to make writing regex-powered text
        [pre-processors]{.title-ref} and [tokenizer cases]{.title-ref}
        easier
    -   Pre-processors:
        -   Re-form words cut by end-of-line hyphens
        -   Remove periods after a (customizable) list of known
            abbreviations (e.g. \"jr\", \"sr\", \"dr\") that can be
            spoken the same without a period
        -   Perform speech corrections by doing word-for-word
            replacements from a (customizable) list of tuples
    -   Tokenizing:
        -   Keep punctuation that modify the inflection of speech (e.g.
            \"?\", \"!\")
        -   Don\'t split in the middle of numbers (e.g. \"10.5\",
            \"20,000,000\") ([\#101](https://github.com/pndurette/gTTS/issues/101))
        -   Don\'t split on \"dotted\" abbreviations and accronyms (e.g.
            \"U.S.A\")
        -   Added Chinese comma (\"，\"), ellipsis (\"...\") to
            punctuation list to tokenize on ([\#86](https://github.com/pndurette/gTTS/issues/86))
-   The `gtts-cli` command-line tool
    -   Rewrote cli as first-class citizen module (`gtts.cli`), powered
        by [Click](http://click.pocoo.org)
    -   Windows support using [setuptool]{.title-ref}\'s
        [entry\_points]{.title-ref}
    -   Better support for Unicode I/O in Python 2
    -   All arguments are now pre-validated
    -   New `--nocheck` flag to skip language pre-checking
    -   New `--all` flag to list all available languages
    -   Either the `--file` option or the `<text>` argument can be set
        to \"-\" to read from `stdin`
    -   The `--debug` flag uses logging and doesn\'t pollute `stdout`
        anymore

### Bugfixes

-   `_minimize()`: Fixed an infinite recursion loop that would occur
    when a token started with the miminizing delimiter (i.e. a space) ([\#86](https://github.com/pndurette/gTTS/issues/86))
-   `_minimize()`: Handle the case where a token of more than 100
    characters did not contain a space (e.g. in Chinese).
-   Fixed an issue that fused multiline text together if the total
    number of characters was less than 100
-   Fixed `gtts-cli` Unicode errors in Python 2.7 (famous last words) ([\#78](https://github.com/pndurette/gTTS/issues/78), [\#93](https://github.com/pndurette/gTTS/issues/93), [\#96](https://github.com/pndurette/gTTS/issues/96))

### Deprecations and Removals

-   Dropped Python 3.3 support
-   Removed `debug` parameter of `gTTS` (in favour of logger)
-   `gtts-cli`: Changed long option name of `-o` to `--output` instead
    of `--destination`
-   `gTTS()` will raise a `ValueError` rather than an `AssertionError`
    on unsupported language

### Improved Documentation

-   Rewrote all documentation files as reStructuredText
-   Comprehensive documentation writen for
    [Sphinx](http://www.sphinx-doc.org), published to <http://gtts.readthedocs.io>
-   Changelog built with [towncrier](https://github.com/hawkowl/towncrier)

### Misc

-   Major test re-work
-   Language tests can read a `TEST_LANGS` enviromment variable so not
    all language tests are run every time.
-   Added [AppVeyor](https://www.appveyor.com) CI for Windows
-   [PEP 8](https://www.python.org/dev/peps/pep-0008/) compliance

1.2.2 (2017-08-15)
------------------

### Misc

-   Update LICENCE, add to manifest ([\#77](https://github.com/pndurette/gTTS/issues/77))

1.2.1 (2017-08-02)
------------------

### Features

-   Add Unicode punctuation to the tokenizer (such as for Chinese and
    Japanese) ([\#75](https://github.com/pndurette/gTTS/issues/75))

### Bugfixes

-   Fix \> 100 characters non-ASCII split, `unicode()` for Python 2 ([\#71](https://github.com/pndurette/gTTS/issues/71), [#73](https://github.com/pndurette/gTTS/issues/73), [\#75](https://github.com/pndurette/gTTS/issues/75))

1.2.0 (2017-04-15)
------------------

### Features

-   Option for slower read speed (`slow=True` for `gTTS()`, `--slow` for
    `gtts-cli`) ([\#40](https://github.com/pndurette/gTTS/issues/40), [\#41](https://github.com/pndurette/gTTS/issues/41), [\#64](https://github.com/pndurette/gTTS/issues/64), [\#67](https://github.com/pndurette/gTTS/issues/67))
-   System proxy settings are passed transparently to all http requests ([\#45](https://github.com/pndurette/gTTS/issues/45), [\#68](https://github.com/pndurette/gTTS/issues/68))
-   Silence SSL warnings from urllib3 ([\#69](https://github.com/pndurette/gTTS/issues/69))

### Bugfixes

-   The text to read is now cut in proper chunks in Python 2 unicode.
    This broke reading for many languages such as Russian.
-   Disabled SSL verify on http requests to accommodate certain
    firewalls and proxies.
-   Better Python 2/3 support in general ([\#9](https://github.com/pndurette/gTTS/issues/9), [\#48](https://github.com/pndurette/gTTS/issues/48), [\#68](https://github.com/pndurette/gTTS/issues/68))

### Deprecations and Removals

-   \'pt-br\' : \'Portuguese (Brazil)\' (it was the same as \'pt\' and
    not Brazilian) ([\#69](https://github.com/pndurette/gTTS/issues/69))

1.1.8 (2017-01-15)
------------------

### Features

-   Added `stdin` support via the \'-\' `text` argument to `gtts-cli` ([\#56](https://github.com/pndurette/gTTS/issues/56))

1.1.7 (2016-12-14)
------------------

### Features

-   Added utf-8 support to `gtts-cli` ([\#52](https://github.com/pndurette/gTTS/issues/52))

1.1.6 (2016-07-20)
------------------

### Features

-   Added \'bn\' : \'Bengali\' ([\#39](https://github.com/pndurette/gTTS/issues/39), [\#44](https://github.com/pndurette/gTTS/issues/44))

### Deprecations and Removals

-   \'ht\' : \'Haitian Creole\' (removed by Google) ([\#43](https://github.com/pndurette/gTTS/issues/43))

1.1.5 (2016-05-13)
------------------

### Bugfixes

-   Fixed HTTP 403s by updating the client argument to reflect new API
    usage ([\#32](https://github.com/pndurette/gTTS/issues/32), [\#33](https://github.com/pndurette/gTTS/issues/33))

1.1.4 (2016-02-22)
------------------

### Features

-   Spun-off token calculation to [gTTS-Token](https://github.com/Boudewijn26/gTTS-token) ([\#23](https://github.com/pndurette/gTTS/issues/23), [\#29](https://github.com/pndurette/gTTS/issues/29))

1.1.3 (2016-01-24)
------------------

### Bugfixes

-   `gtts-cli` works with Python 3 ([\#20](https://github.com/pndurette/gTTS/issues/20))
-   Better support for non-ASCII characters ([\#21](https://github.com/pndurette/gTTS/issues/21), [\#22](https://github.com/pndurette/gTTS/issues/22))

### Misc

-   Moved out gTTS token to its own module ([\#19](https://github.com/pndurette/gTTS/issues/19))

1.1.2 (2016-01-13)
------------------

### Features

-   Added gTTS token (tk url parameter) calculation ([\#14](https://github.com/pndurette/gTTS/issues/14), [\#15](https://github.com/pndurette/gTTS/issues/15), [\#17](https://github.com/pndurette/gTTS/issues/17))

1.0.7 (2015-10-07)
------------------

### Features

-   Added `stdout` support to `gtts-cli`, text now an argument rather
    than an option ([\#10](https://github.com/pndurette/gTTS/issues/10))

1.0.6 (2015-07-30)
------------------

### Features

-   Raise an exception on bad HTTP response (4xx or 5xx) ([\#8](https://github.com/pndurette/gTTS/issues/8))

### Bugfixes

-   Added `client=t` parameter for the api HTTP request ([\#8](https://github.com/pndurette/gTTS/issues/8))

1.0.5 (2015-07-15)
------------------

### Features

-   `write_to_fp()` to write to a file-like object ([\#6](https://github.com/pndurette/gTTS/issues/6))

1.0.4 (2015-05-11)
------------------

### Features

-   Added Languages: `zh-yue` : `Chinese (Cantonese)`,
    `en-uk` : `English (United Kingdom)`,
    `pt-br`: `Portuguese (Brazil)`, `es-es`:
    `Spanish (Spain)`, `es-us` : `Spanish (United
    StateS)`, `zh-cn`: `Chinese (Mandarin/China)`,
    `zh-tw`: `Chinese (Mandarin/Taiwan)` ([\#4](https://github.com/pndurette/gTTS/issues/4))

### Bugfixes

-   `gtts-cli` print version and pretty printed available languages,
    language codes are now case insensitive
    ([\#4](https://github.com/pndurette/gTTS/issues/4))

1.0.3 (2014-11-21)
------------------

### Features

-   Added Languages: \'en-us\' : \'English (United States)\', \'en-au\' : \'English (Australia)\' ([\#3](https://github.com/pndurette/gTTS/issues/3))

1.0.2 (2014-05-15)
------------------

### Features

-   Python 3 support

1.0.1 (2014-05-15)
------------------

### Misc

-   SemVer versioning, CI changes

1.0 (2014-05-08)
----------------

### Features

-   Initial release
