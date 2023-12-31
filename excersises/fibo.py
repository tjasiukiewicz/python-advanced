#!/usr/bin/env python3

def my_cache(func):
    cache = {}

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

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
