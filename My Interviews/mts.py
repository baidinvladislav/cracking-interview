import datetime
from functools import wraps


a = 1
def decorator(func):
    b = 345
    @wraps
    def wrapper(*arsg, **kwargs):
        nonlocal a
        a = 123
        print(b)
        time_start = datetime.datetime.now()
        result = func(*arsg, **kwargs)
        time_end = datetime.datetime.now() - time_start
        print(time_end)
        return result

    print(a)
    return wrapper


@decorator
def my_func():
    """documentation"""
    pass

my_func.__doc__  # - ?


new_func = decorator(my_func)
new_func()
