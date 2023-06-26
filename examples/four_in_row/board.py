#!/usr/bin/env python3

class Board:
    board_width = 7
    board_height = 6

    def __display_col_numbers(self):
        print('   ' + ' '.join(str(col_number + 1)
              for col_number in range(self.board_width)))

    def __display_row_separator(self):
        print('  ' + '+-' * self.board_width, end='+\n')

    def __display_row(self, row, idx):
        self.__display_row_separator()

        # Print row
        print('  ', end='')
        for field in row:
            my_field = ' ' if field is None else '?'
            print('|', my_field, sep='', end='')
        print('|')

    def __init__(self):
        self.__fields = [[None for _ in range(self.board_width)]
                         for _ in range(self.board_height)]

    def display(self):

        self.__display_col_numbers()

        for num, row in enumerate(reversed(self.__fields)):
            self.__display_row(row, num)

        self.__display_row_separator()
        self.__display_col_numbers()


if __name__ == '__main__':
    board = Board()
    board.display()
