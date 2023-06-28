#!/usr/bin/env python3



class Funny_Adds:
    def _is_palindrome(self, value):
        return str(value) == str(value)[::-1]

    def _funny_add(self, value):
        return value + int(str(value)[::-1])

    # [min_value, max_value] (inclusive)
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._current_value = min_value

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_value > self._max_value:
            raise StopIteration()

        add_count = 0
        value = self._current_value
        while not self._is_palindrome(value):
            value = self._funny_add(value)
            add_count += 1
        result = str(self._current_value) + ': ' + str(add_count) + ' ' + str(value)
        self._current_value += 1
        return result

if __name__ == '__main__':
    for result in Funny_Adds(1, 190):
        print(result)
            
