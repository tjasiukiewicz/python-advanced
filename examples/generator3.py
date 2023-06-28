#!/usr/bin/env python3


def my_gen(max_counter):
    counter = 0
    while max_counter:
        counter += 1
        yield counter
        max_counter -= 1


for value in my_gen(8):
    print(value)

print(type(my_gen))
