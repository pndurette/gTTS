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

Read "c'est la vie" in French to ``cestlavie.mp3``::

   $ gtts-cli "c'est la vie" --lang fr --output cestlavie.mp3

Read '你好' to ``你好.mp3`` (in Mandarin, using google.cn)::

   $ gtts-cli '你好' --tld cn --lang zh-cn --output 你好.mp3

Read 'slow' slowly to ``slow.mp3``::

   $ gtts-cli 'slow' --slow --output slow.mp3

Read 'hello' to ``stdout``::

   $ gtts-cli 'hello'

Read ``stdin`` to ``hello.mp3`` via ``<text>`` or ``<file>``::

   $ echo -n 'hello' | gtts-cli - --output hello.mp3
   $ echo -n 'hello' | gtts-cli --file - --output hello.mp3

Read 'no check' to ``nocheck.mp3`` without language checking::

   $ gtts-cli 'no check' --lang zh --nocheck --ouput nocheck.mp3

.. note:: Using ``--nocheck`` can speed up execution. It exists mostly however to force a ``<lang>`` language tag that might not be documented but would work with the API, such as for specific regional sub-tags of documented tags (examples for 'en': 'en-gb', 'en-au', etc.).

Playing sound directly
----------------------

You can pipe the output of ``gtts-cli`` into any media player that supports ``stdin``. For example, using the ``play`` command from `SoX <http://sox.sourceforge.net>`_::

   $ gtts-cli 'hello' | play -t mp3 -

