doctest
========

doctest is a very interesting library for creating functional tests right in the documentation of the code. Using docstrings, you can specify the test execution right next the the code.

Example:
--------

This is in _math.py_:
```python
def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b
```

Then run this file on the command line:

```bash
$ python -m doctest
```

Tutorial:
---------

This tutorial has a few functions and doctests written or left out. Try and make them all pass. Note we have a _if __name__ == '__main__':_ in there so just do:

```bash
$ python math.py
```

More Info:
----------

2.7 [http://docs.python.org/2/library/doctest.html](http://docs.python.org/2/library/doctest.html)

3.3 [http://docs.python.org/3.3/library/doctest.html](http://docs.python.org/3.3/library/doctest.html)
