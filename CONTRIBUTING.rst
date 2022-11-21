Contributing
============

Reporting Issues
----------------

On the Github issues_ page. Thanks!

Submitting Patches
------------------

1. **Fork**. Follow `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_!
2. **Write/Update tests** (see below).
3. **Document**. Docstrings follow the `Google Python Style Guide`_ (docs by Sphinx_).
   You can 'test' documentation::

     $ pip install .[docs]
     $ cd docs && make html # generated in docs/_build/html/

4. **Open Pull Request**. To the ``main`` branch.

.. note:: | Please don't hesitate to contribute! While good tests, docs and structure are
          | encouraged, I do welcome great ideas over absolute comformity to the above!
          | Thanks! ❤️

Testing
-------

| Testing is done with the ``unittest`` framework.
| As a rule, the file ``./tests/test_<module>.py`` file tests the ``<module>`` module.

To run all tests (testing only language 'en' and generating an html coverage
report in ``gtts/htmlcov/``)::

  $ pip install .[tests]
  $ TEST_LANGS=en pytest -v -s gtts/ --cov=gtts --cov-report=html

.. _repo: https://github.com/pndurette/gTTS/
.. _issues: https://github.com/pndurette/gTTS/issues

.. _Google Python Style Guide: http://google.github.io/styleguide/pyguide.html#Comments
.. _Sphinx: http://www.sphinx-doc.org/
.. _towncrier: https://github.com/hawkowl/towncrier
