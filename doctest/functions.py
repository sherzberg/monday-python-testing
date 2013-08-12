

def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b


def double(x):
    """
    >>> double(1)
    1
    >>> double(2)
    4
    >>> double('a')
    'aa'
    """
    return None


def reverse(my_list):
    """
    >>> reverse(['a', 'b', 'c', 'd'])
    None
    >>> reverse(['a'])
    None
    >>> reverse([1, 2, 3, 4, 5])
    """
    return list(reversed(my_list))


def avg(my_list):
    """
    >>> avg([1, 2, 3, 4])
    2.5
    >>> avg([0])
    0.0
    >>> avg([0, 1, 2, 3, 4, 5])
    2.5
    """
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
