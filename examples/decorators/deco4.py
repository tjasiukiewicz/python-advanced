from functools import wraps


def my_clip(my_min, my_max):
    def internal(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > my_max:
                result = my_max
            elif result < my_min:
                result = my_min 
            return result
        return wrapper
    return internal

@my_clip(0, 10)
def my_add(a, b):
    return a + b

print(my_add(13, 23))

