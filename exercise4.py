# Exercise 4, time to do some decoration (hard-ish)!
import functools


def add_some(additional_value: int):
    """
    Decorator wrapper, adds 'additional_value' value to output of decorated function
    :param additional_value: A value to add to the return value of the decorated function.
    :return:
    """
    # Complete this decorator.
    def decorator_wrapper(func):
        @functools.wraps(func)
        def decorated_func(*args, **kwargs):
            output = func(*args, **kwargs) + additional_value
            return output
        return decorated_func
    return decorator_wrapper

@add_some(5)
def add_one(a_value) -> int:
    return a_value + 1



# Change no code below.
if __name__ == "__main__":
    print(f"Value of add_one for 2+1+5 == {add_one(2)}")




'''# Exercise 4, time to do some decoration (hard-ish)!
import functools


def add_some(additional_value:int):
    """
    Decorator wrapper, adds 'additional_value' value to output of decorated function
    :param additional_value: A value to add to the return value of the decorated function.
    :return:
    """
    # Complete this decorator.
    def decorator_wrapper(func):
        @functools.wraps(func)
        def decorated_func(*args, **kwargs):
            a_value = additional_value
            return a_value
        return decorated_func
    return decorator_wrapper

@add_some(1)
def add_one(a_value) -> int:
    return a_value  +1


# Change no code below.
if __name__ == "__main__":
    print(f"Value of add_one for 2+1+5 == {add_one(2)}")
'''