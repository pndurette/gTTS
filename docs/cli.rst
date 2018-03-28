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

Read 'hello' to :file:`hello.mp3`::

   $ gtts-cli 'hello' --output hello.mp3

Read 'bonjour' in French to :file:`bonjour.mp3`::

   $ gtts-cli 'bonjour' --lang fr --output bonjour.mp3

Read 'slow' slowly to :file:`slow.mp3`::

   $ gtts-cli 'slow' --slow --output slow.mp3

Read 'hello' to :mod:`stdout`::

   $ gtts-cli 'hello'

Read :mod:`stdin` to :file:`hello.mp3` via ``<text>`` or ``<file>``::

   $ echo -n 'hello' | gtts-cli - --output hello.mp3
   $ echo -n 'hello' | gtts-cli --file - --output hello.mp3

Read 'no check' to :file:`nocheck.mp3` without language checking::

   $ gtts-cli --lang zh --nocheck --ouput nocheck.mp3

.. note:: Using ``--nocheck`` can make the command *slightly* faster. It exists however to force a ``<lang>`` tag that might not be documented but would work, such as for specific regional sub-tags of documented tags (examples for 'en': 'en-gb', 'en-au', ...)
