#!/usr/bin/env python3

from token import Token

class Board:
    board_width = 7
    board_height = 6

    def __display_col_numbers(self):
        print('   ' + ' '.join(str(col_number + 1)
              for col_number in range(self.board_width)))

    def __display_row_separator(self):
        print('  ' + '+-' * self.board_width, end='+\n')

    def __display_row(self, row):
        self.__display_row_separator()

        # Print row
        print('  ', end='')
        for field in row:
            my_field = ' ' if field is None else field.get_repr()
            print('|', my_field, sep='', end='')
        print('|')

    def __token_gravity(self, token, col_number):
        row_number = self.board_height - 1
        while row_number:
            if self.__fields[row_number - 1][col_number] is None:
                self.__fields[row_number - 1][col_number] = token
                self.__fields[row_number][col_number] = None
            else:
                break
            row_number -= 1

    def __init__(self):
        self.__fields = [[None for _ in range(self.board_width)]
                         for _ in range(self.board_height)]

    def display(self):

        self.__display_col_numbers()

        for row in reversed(self.__fields):
            self.__display_row(row)

        self.__display_row_separator()
        self.__display_col_numbers()

    def drop(self, token, col_number):
        assert col_number > 0 and col_number <= self.board_width

        # Normalize col_number to offset
        col_number -= 1

        # Check col is not empty
        if self.__fields[self.board_height - 1][col_number] != None:
            return False

        # Drop token into first row field
        self.__fields[self.board_height - 1][col_number] = token

        self.__token_gravity(token, col_number)

        return True

if __name__ == '__main__':
    board = Board()
    board.display()
    board.drop(Token('X'), 2)
    board.drop(Token('O'), 3)
    board.display()
