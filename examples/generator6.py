#!/usr/bin/env python3

class MyGenerator:
    def __init__(self, counter):
        self._counter = counter

    def __iter__(self):
        return self

    def __next__(self):
        while self._counter > 1:
            self._counter -= 1
            return self._counter
        raise StopIteration()


for value in MyGenerator(8):
    print(value)
