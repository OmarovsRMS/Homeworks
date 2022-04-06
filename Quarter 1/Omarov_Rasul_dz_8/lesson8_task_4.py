from functools import wraps

def val_check(check_function):
    def decor_func(func):
        @wraps(func)
        def wrapper(x):
            if check_function(x):
                return func(x)
            else:
                raise ValueError('Не пройдена валидация')
        return wrapper
    return decor_func


@val_check(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(3))
print(calc_cube.__name__)
