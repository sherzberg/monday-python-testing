unittest
========

Unit test is the "batteries-included" testing framework so nothing extra needs to be installed to create and run unit tests. It is very similar to how junit and nunit works.

> _Note_: These tests assume python is python 2.7

Example:
--------

```python
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        print('set up')
    
    def test_mod(self):
        self.assertEquals(1, 3 % 2)

    def tearDown(self):
        print('tear down')
```

Tutorial:
---------

This tutorial has one already written function with failing tests and one failing test for an unwritten function. Fix them:

```bash
$ python test_function1.py
```

```bash
$ python test_function2.py
```

More Info:
----------

2.7 [http://docs.python.org/2/library/unittest.html](http://docs.python.org/2/library/unittest.html)

3.3 [http://docs.python.org/3.3/library/unittest.html](http://docs.python.org/3.3/library/unittest.html)
