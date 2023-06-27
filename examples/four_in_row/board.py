#!/usr/bin/env python3

from token import Token
from console import Console
from color import Color


class Board:
    board_width = 7
    board_height = 6

    def __token_gravity(self, token, col_number):
        row_number = self.board_height - 1
        while row_number:
            if self.__fields[row_number - 1][col_number] is None:
                self.__fields[row_number - 1][col_number] = token
                self.__fields[row_number][col_number] = None
            else:
                break
            row_number -= 1

    def __init__(self, console):
        self.__fields = [[None for _ in range(self.board_width)]
                         for _ in range(self.board_height)]
        self.__console = console

    def drop(self, token, col_number):
        assert col_number > 0 and col_number <= self.board_width

        # Normalize col_number to offset
        col_number -= 1

        # Check col is not empty
        if self.__fields[self.board_height - 1][col_number] is not None:
            return False

        # Drop token into first row field
        self.__fields[self.board_height - 1][col_number] = token

        self.__token_gravity(token, col_number)

        return True

    def is_full(self):
        return all(self.__fields[-1])

    def render(self):
        console_fields = [[None for _ in range(self.board_width)]
                         for _ in range(self.board_height)]

        # TODO: Refactor!
        for row_number in range(Board.board_height):
            for col_number in range(Board.board_width):
                token = self.__fields[row_number][col_number]
                if token is None:
                    console_fields[row_number][col_number] = 0
                elif token.get_color() == Color.RED:
                    console_fields[row_number][col_number] = 1
                else:
                    console_fields[row_number][col_number] = 2

        self.__console.set_state(console_fields)


if __name__ == '__main__':
    board = Board(Console())
    board.drop(Token('X'), 2)
    board.drop(Token('O'), 3)
    board.render()
