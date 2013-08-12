Mocking & Patching
==================

Mocking and patching are very similar to PowerMock or Mockito in Java, just with a pythonic api. Mocks allow you to mock out any function or method call, capture parameters, and log specific function calls.

Patches are bit different and use the python import system to "patch" imported classes and fuctions with new things.

> _Note_: These tests assume python is python 3.3. The mock library comes by default in Python 3. You can install mock on 2.7 with `pip install mock`.

Example:
--------

```python
from unittest.mock import Mock, patch

cls = MyClass()
cls.method = Mock(return_value=42)
cls.method(4,2)
cls.method.assert_called_with(4,2)

from unittest.mock import patch
from functions import cwd

@patch('os.getcwd')
def test(cwd_mock):
    cwd_mock.return_value = 'TEST'
    assert cwd() == 'TEST' 
```

Tutorial:
---------

The first tutorial is a simple mock of a system library. The second showcases some more interesting mocking and patching.

```bash
$ python3.3 test_cwd.py
```

```bash
$ python3.3 test_classes.py
```

More Info:
----------

3.3 [http://docs.python.org/dev/library/unittest.mock](http://docs.python.org/dev/library/unittest.mock)
