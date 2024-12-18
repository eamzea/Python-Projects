from time import time
from types import FunctionType


def my_decorator(func: FunctionType):
    '''
    my_decorator

    Args:
        func ():

    Returns:
        FunctionType:
    '''
    def wrapper():
        print('**********')
        func()
        print('**********')
    return wrapper


@my_decorator # type: ignore
def hello() -> None:
    print('Jello')


hello()


# It is the same than this
def my_dec(func):  # type: ignore
    def wrapper():
        print('**********')
        func()
        print('**********')
    return wrapper


def greet():
    print('Hello')


var_1 = my_dec(greet)
var_1()


def performance(fn):  # type: ignore
    def wrapper(*args, **kwargs):  # type: ignore
        t1 = time()
        result = fn(*args, **kwargs)  # type: ignore
        t2 = time()
        print(f'took {t2-t1} ms')
        return result  # type: ignore
    return wrapper  # type: ignore
