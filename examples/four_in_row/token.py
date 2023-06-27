#!/usr/bin/env python3

from color import Color


class Token:
    def __init__(self, color):
        self.__color = color
        self.__my_repr = 'X' if color == Color.RED else 'O'

    def get_repr(self):
        return self.__my_repr


if __name__ == '__main__':
    token = Token('X')
    print(token.get_repr())
    print('')
