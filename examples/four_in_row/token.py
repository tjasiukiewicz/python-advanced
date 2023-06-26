#!/usr/bin/env python3

class Token:
    def __init__(self, my_repr):
        self.__my_repr = my_repr

    def get_repr(self):
        return self.__my_repr


if __name__ == '__main__':
    token = Token('X')
    print(token.get_repr())
    print('')
