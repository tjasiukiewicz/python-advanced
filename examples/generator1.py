#!/usr/bin/env python3


def my_gen():
    counter = 0
    while True:
        counter += 1
        yield counter


gen = my_gen()

print(type(gen))

for _ in range(8):
    print(gen.__next__())

