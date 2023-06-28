#!/usr/bin/env python3

def sum_proper_divisors(value):
    # FIXME: Oczywiście można zoptymalizować wyszukiwanie znacznie lepiej...
    return sum(div for div in range(1, value // 2 + 1) if value % div == 0)

def is_perfect_number(value):
    return sum_proper_divisors(value) == value

# Return in range [min_value, max_value] (inclusive)
def perfect_number_in_range(min_value, max_value):
    
    for value in range(min_value, max_value + 1):
        if is_perfect_number(value):
            yield value

if __name__ == '__main__':

    for value in perfect_number_in_range(1, 10000):
        print(value)


