#!/usr/bin/env python3

class MyGenerator:
    def __init__(self, counter):
        self._counter = counter

    def __iter__(self):
        return (value for value in range(self._counter)).__iter__()
        #return range(self._counter).__iter__()


for value in MyGenerator(8):
    print(value)
