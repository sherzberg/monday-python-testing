Test Runners & Coverage
=======================

Running tests manually with _python tests.py_ is fun until it isn't. What if you have 30 test files? Lamesauce. So we need a test runner. A defacto test runner is [Nose](https://nose.readthedocs.org).  Also, this means no more _if __name__ == '__main__'_ junk.

Example:
--------

```bash
$ cd unittests
$ cd nosetests
```

Converage
---------

```bash
$ nosetests --with-coverage
```

```bash
$ nosetests --with-coverage --cover-html --cover-xml
```

More Info:
----------

Nose Usage: [https://nose.readthedocs.org/en/latest/usage.html#options](https://nose.readthedocs.org/en/latest/usage.html#options)
