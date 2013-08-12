Mocking & Patching
==================

Mocking and patching are very similar to PowerMock or Mockito in Java, just with a pythonic api. 
Mocks allow you to mock out any function, method call ,or callable. They also capture call parameters and call counts.

Patches are bit different and use the python import system to "patch" imported classes and fuctions with new things.
These are useful when a method you are wanting to test creates new objects and you want to replace the whole object
with a mocked object.

> _Note_: These tests assume python is python 3.3. The mock library comes by default in Python 3. You can install mock on 2.7 with `pip install mock`.

Example:
--------

```python
from unittest.mock import Mock, patch
from functions import cwd

class MyClass(object):
    pass
    
cls = MyClass()
cls.method = Mock(return_value=42)
cls.method(4,2)
cls.method.assert_called_with(4,2)

def create_stuff():
    return MyClass()
    
@patch('__main__.MyClass')
def test_create_stuff(patched_class):
    print patched_class
    return patched_class()
    
@patch('__main__.MyClass')
def test_create_stuff(patched_class):
    print(patched_class)
    patched_class.side_effect = Exception
    return patched_class()

test_create_stuff()
```

Tutorial:
---------

The first tutorial is a simple mock of a system library. The second showcases some more interesting mocking and patching.

```bash
$ python3.3 test_cwd.py
```

This second example shows off some mocking. There are 2 failing and 1 passing test. Try and make the two tests pass.

```bash
$ python3.3 test_classes.py
```

More Info:
----------

3.3 [http://docs.python.org/dev/library/unittest.mock](http://docs.python.org/dev/library/unittest.mock)
