# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).
This file adheres to [Keep a CHANGELOG](http://keepachangelog.com).

## [Unreleased]

## [1.2.2] - 2017-08-15
### Added
- Updated LICENSE copyright date
- LICENSE file added to manifest (#77, thanks @mapreri!)

## [1.2.1] - 2017-08-02
### Added
- More Unicode punctuation to the tokenizer (such as for Chinese and Japanese)

### Fixed
- Unicode tokenization of strings larger than 100 characters in Python 2 (#71, #73)

## [1.2.0] - 2017-04-15
### Added
- Option for slower read speed (`slow=True` for `gTTS()`, `--slow` for `gtts-cli`)
- System proxy settings are passed transparently to all http requests
- Language: 'km', 'Khmer (Cambodian)'
- Language: 'si', 'Sinhala'
- Language: 'uk', 'Ukrainian'
- More debug output

### Removed
- Language: 'pt-br' : 'Portuguese (Brazil)' (it was the same as 'pt' and not Brazilian)

### Fixed
- The text to read is now cut in proper chunks in Python 2 unicode. This broke reading for many languages such as Russian.
- Disabled SSL verify on http requests to accommodate certain firewalls and proxies.
- Better Python 2/3 support in general
- Various fixes and cleanups

## [1.1.8] - 2017-01-15
### Added
- Added stdin support (w/ `text` set to `-`) to `gtts-cli.py`/`gtts-cli` (#56 thanks @WyohKnott)

## [1.1.7] - 2016-12-14
### Changed
- Added utf-8 support to `gtts-cli.py`/`gtts-cli` (#52 thanks @bakaiadam) 

## [1.1.6] - 2016-07-20
### Added
- 'bn' : 'Bengali' (thanks @sakibiqbal, @mshubhankar)

### Removed
- 'ht' : 'Haitian Creole' (removed by Google)
- 'token-script.js' (clean up)

## [1.1.5] - 2016-05-13
### Fixed
- Fixed HTTP 403s by updating the client argument to reflect new API usage

## [1.1.4] - 2016-02-22

### Changed
- Token calculation moved to now spun-off module [gTTS-Token](https://github.com/Boudewijn26/gTTS-token) maintained by @Boudewijn26

## [1.1.3] - 2016-01-24
### Added
- Contributing section to README.md,

### Changed
- Better CHANGELOG.md replacing CHANGES.txt

### Fixed
- Made `gtts-cli` work w/ Python 3.x, from @desbma
- Handle non-ASCII chars correctly (a wrong token would get generated resulting in a HTTP 403), from @Boudewijn26, h/t @desbma

### Removed
- Dropped Python 3.2 support and in .travis.yml

## [1.1.2] - 2016-01-13
- Packaging and Travis CI changes

## 1.1.1 - 2016-01-13 [YANKED]
### Changed
- Packaging and Travis CI changes

## [1.1.0] - 2016-01-13 [YANKED]
### Added
- Google Translate API token (`tk`) generation like translate.google.com to fix the constant HTTP 403 errors (for now), from @Boudewijn26

## [1.0.7] - 2015-10-07
### Changed
- `gtts-cli` can be piped, arguments made more standard, from @Dr-Horv.

## [1.0.6] - 2015-07-30
### Added:
- Raise an exception on bad HTTP response (4xx or 5xx).

### Fixed
- New required 'client=t' parameter for the api HTTP request, h/t @zainkhan_ on Twitter.

## [1.0.5] - 2015-07-15
### Added:
- Option to use `write_to_fp()` to write to a file-like object instead of only to a file, from @Holzhaus.

## [1.0.4] - 2015-05-11
### Added
- `gtts-cli` shows the version and pretty printed and sorted available languages.
- `zh-yue` : 'Chinese (Cantonese)'.
- `en-uk` : 'English (United Kingdom)'.
- `pt-br` : 'Portuguese (Brazil)'.
- `es-es` : 'Spanish (Spain)'.
- `es-us` : 'Spanish (United StateS)'

## Changed
- Language code are now case insensitive.
- Same voices but renamed for uniformity, better description:
  - `zh-CN` : 'Mandarin (simplified)' is now `zh-cn` : 'Chinese (Mandarin/China)'.
  - `zh-TW` : 'Mandarin (traditional)' is now `zh-tw` : 'Chinese (Mandarin/Taiwan)'.


## [1.0.3] - 2014-11-21
### Added
- 'en-us' : 'English (United States)' from @leo-labs.
- 'en-au' : 'English (Australia)'. from @leo-labs.

## [1.0.2] - 2014-05-15
### Changed
- Python 3.x support.

## 1.0.1 - 2014-05-15 [YANKED]
### Added
- Travis CI changes
- Following [SemVer](http://semver.org/).

## 1.0 - 2014-05-08
### Added
- Initial release

[Unreleased]: https://github.com/pndurette/gTTS/compare/v1.2.2...master
[1.2.2]: https://github.com/pndurette/gTTS/compare/v1.2.1...v1.2.2
[1.2.1]: https://github.com/pndurette/gTTS/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/pndurette/gTTS/compare/v1.1.8...v1.2.0
[1.1.8]: https://github.com/pndurette/gTTS/compare/v1.1.7...v1.1.8
[1.1.7]: https://github.com/pndurette/gTTS/compare/v1.1.6...v1.1.7
[1.1.6]: https://github.com/pndurette/gTTS/compare/v1.1.5...v1.1.6
[1.1.5]: https://github.com/pndurette/gTTS/compare/v1.1.4...v1.1.5
[1.1.4]: https://github.com/pndurette/gTTS/compare/v1.1.3...v1.1.4
[1.1.3]: https://github.com/pndurette/gTTS/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/pndurette/gTTS/compare/v1.1.0...v1.1.2
[1.1.0]: https://github.com/pndurette/gTTS/compare/v1.0.7...v1.1.0
[1.0.7]: https://github.com/pndurette/gTTS/compare/v1.0.6...v1.0.7
[1.0.6]: https://github.com/pndurette/gTTS/compare/v1.0.5...v1.0.6
[1.0.5]: https://github.com/pndurette/gTTS/compare/v1.0.4...v1.0.5
[1.0.4]: https://github.com/pndurette/gTTS/compare/v1.0.3...v1.0.4
[1.0.3]: https://github.com/pndurette/gTTS/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/pndurette/gTTS/compare/v1.0...v1.0.2
