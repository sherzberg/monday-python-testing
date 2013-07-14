

class IncorrectParameterTypeException(Exception):
    pass


def function1(my_list):
    pass


def function2(x):
    if x < 0:
        raise Exception("parameter must be positive")
    elif x > 100:
        return 100
    else:
        return max(100, x * 2)
