#!/usr/bin/env python3



class Funny_Adds:
    @staticmethod
    def _is_palindrome(value):
        return str(value) == str(value)[::-1]

    @staticmethod
    def _funny_add(value):
        return value + int(str(value)[::-1])

    def _add_to_palindrome(self, value):
        add_count = 0
        result_correct = False
        while not self._is_palindrome(value) and add_count < self._max_counter:
            value = self._funny_add(value)
            add_count += 1
        if add_count < self._max_counter:
            result_correct = True
        return add_count, value, result_correct

    # [min_value, max_value] (inclusive)
    def __init__(self, min_value, max_value, max_counter = 1000):
        self._min_value = min_value
        self._max_value = max_value
        self._current_value = min_value
        self._max_counter = max_counter

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_value > self._max_value:
            raise StopIteration()

        add_count, value, result_correct = self._add_to_palindrome(self._current_value)
        correct_repr = ':  ' if result_correct else ':! '
        result = str(self._current_value) + correct_repr + str(add_count) + ' ' + str(value)
        self._current_value += 1
        return result

if __name__ == '__main__':
    for result in Funny_Adds(1, 300, 10000):
        print(result)
            
