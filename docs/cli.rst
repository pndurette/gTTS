Command-line (:mod:`gtts-cli`)
==============================

After installing the package, the ``gtts-cli`` tool becomes available::

$ gtts-cli

.. click:: gtts.cli:tts_cli
   :prog: gtts-cli
   :show-nested:

Examples
--------

List available languages::

   $ gtts-cli --all

Read 'hello' to ``hello.mp3``::

   $ gtts-cli 'hello' --output hello.mp3

Read 'bonjour' in French to ``bonjour.mp3``::

   $ gtts-cli 'bonjour' --lang fr --output bonjour.mp3

.. note:: Alternatively, you can enclose your text with quotation marks to avoid errors associated with phrases that may need the use of an apostrophe::

   $ gtts-cli "c'est la vie" --lang fr --output test.mp3

Read 'slow' slowly to ``slow.mp3``::

   $ gtts-cli 'slow' --slow --output slow.mp3

Read 'hello' to ``stdout``::

   $ gtts-cli 'hello'

Read ``stdin`` to ``hello.mp3`` via ``<text>`` or ``<file>``::

   $ echo -n 'hello' | gtts-cli - --output hello.mp3
   $ echo -n 'hello' | gtts-cli --file - --output hello.mp3

Read 'no check' to ``nocheck.mp3`` without language checking::

   $ gtts-cli 'no check' --lang zh --nocheck --ouput nocheck.mp3

.. note:: Using ``--nocheck`` can make the command `slightly` faster. It exists however to force a ``<lang>`` language tag that might not be documented but would work with the API, such as for specific regional sub-tags of documented tags (examples for 'en': 'en-gb', 'en-au', etc.).

Playing sound directly
----------------------

You can pipe the output of ``gtts-cli`` into any media player that supports ``stdin``. For example, using the ``play`` command from `SoX <http://sox.sourceforge.net>`_::

   $ gtts-cli 'hello' | play -t mp3 -

