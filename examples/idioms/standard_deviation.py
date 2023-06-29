#!/usr/bin/env python3

from math import sqrt
from functools import reduce


# C/Java/C#/... - way
def standard_deviation1(data_container):
    my_sum = 0
    for i in range(len(data_container)):
        my_sum += data_container[i]
    my_average = my_sum / len(data_container)

    my_squares = 0
    for i in range(len(data_container)):
        my_squares += pow(data_container[i] - my_average, 2)

    return sqrt(my_squares / len(data_container))

def standard_deviation2(data_container):
    my_average = sum(data_container) / len(data_container)

    my_squares = sum(pow(my_average - value, 2) for value in data_container)

    return sqrt(my_squares / len(data_container))

def standard_deviation3(data_container):
    my_average = sum(data_container) / len(data_container)

    return sqrt(
            sum(val**2 for val in map(lambda value: my_average - value, data_container))
            / len(data_container))

# Maciej way ??
def standard_deviation4(a):
    avg_a = sum(a)/len(a)
    return sqrt(reduce(lambda x, s: s + avg_a  - x, a)/len(a))

data = [17, 19, 20, 21, 23]

print(standard_deviation1(data))
print(standard_deviation2(data))
print(standard_deviation3(data))
print(standard_deviation4(data))
