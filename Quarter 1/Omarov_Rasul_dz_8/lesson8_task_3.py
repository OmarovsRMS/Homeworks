from functools import wraps

def decor_func(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}:{type(arg)})', end=', ')
    return wrapper

@decor_func
def calc_cube():
    return x ** 3

a = calc_cube(1, 2, 3, 4)
