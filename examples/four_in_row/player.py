#!/usr/bin/env python3

from color import Color
from token import Token
from console import Console


class Player:
    def __init__(self, console, name, color):
        assert isinstance(color, Color)

        self.__name = name
        self.__token = Token(color)
        self.__console = console

    def get_name(self):
        return self.__name

    def get_column(self):
        token_repr = self.__token.get_repr()
        column = self.__console.get_column(self.__name, token_repr)
        return column

    def get_token(self):
        return self.__token


if __name__ == '__main__':
    pass
