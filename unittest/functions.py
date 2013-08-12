

class IncorrectParameterTypeException(Exception):
    pass


def function1(my_list):
    '''If a valid list is used as a parameter,
    a new list is returned were each item is the difference
    between the number at the same index and the average of the
    items in the list.

    A IncorrectParameterTypeException raised if the parameter is
    not a list.
    '''

    pass


def function2(x):
    '''Doubles the number if greater than -1 and less than 100.
    Raise exception if negative.
    If x > 100 return 100.
    '''

    if x < 0:
        raise Exception("parameter must be positive")
    elif x > 100:
        return 100
    else:
        return max(100, x * 2)
