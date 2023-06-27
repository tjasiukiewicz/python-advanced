#!/usr/bin/env python3

from color import Color
from token import Token


class Player:
    def __init__(self, name, color):
        assert isinstance(color, Color)

        self.__name = name
        self.__token = Token(color)

    def get_name(self):
        return self.__name

    def get_column(self):
        token_repr = self.__token.get_repr()
        column = int(input(
               f'Player {self.__name}, token {token_repr}. Input column: '))
        return column

    def get_token(self):
        return self.__token


if __name__ == '__main__':
    color = Color.RED
    player = Player('Eve', color)
    player.get_column()
