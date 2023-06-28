#!/usr/bin/env python3

class Console:
    def __display_col_numbers(self):
        print('   ' + ' '.join(str(col_number + 1)
              for col_number in range(self.__width)))

    def __display_row_separator(self):
        print('  ' + '+-' * self.__width, end='+\n')

    def __display_row(self, row):
        self.__display_row_separator()

        # Print row
        print('  ', end='')
        for field in row:
            my_field = ' XO'[field]
            print('|', my_field, sep='', end='')
        print('|')

    def __init__(self):
        self.__fields = []

    def display(self):
        self.__display_col_numbers()

        for row in reversed(self.__fields):
            self.__display_row(row)

        self.__display_row_separator()
        self.__display_col_numbers()

    def set_state(self, data):
        self.__fields = data
        self.__width = len(data[0])


if __name__ == '__main__':
    pass
