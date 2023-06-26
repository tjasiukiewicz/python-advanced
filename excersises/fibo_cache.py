#!/usr/bin/env python3

from functools import wraps

def my_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = tuple(args) + tuple(kwargs.items())
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

@my_cache
def fibo(index):
    if index == 0:
        return 0
    if index == 1 or index == 2:
        return 1

    else:
        return fibo(index - 1) + fibo(index - 2)

print(fibo(35))
print(fibo(36))
