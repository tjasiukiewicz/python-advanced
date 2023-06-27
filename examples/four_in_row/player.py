#!/usr/bin/env python3

from color import Color
from token import Token


class Player:
    def __init__(self, name, color):
        self.__color = color
        self.__name = name

    def get_name(self):
        return self.__name

    def get_column(self):
        column = int(input(
            f'Player {self.__name}, color {self.__color}. Input column: '))
        return column

    def get_token(self):
        return Token(self.__color)


if __name__ == '__main__':
    color = Color.RED
    player = Player('Eve', color)
    player.get_column()
