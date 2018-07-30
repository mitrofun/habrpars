from functools import wraps

import time


def timed(func):
    """This decorator prints the execution time for the decorated function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} ran in {round(end - start, 2)}s')
        return result
    return wrapper


def flat_list(_list):
    """[(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def get_max_len_word(_list):
    """Return max len word from list"""
    return max(len(item) for item in _list if type(item) != int)


def get_max_len_number(_list):
    """Return max number from list"""
    return max(len(str(item)) for item in _list if type(item) == int)
