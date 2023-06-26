#!/usr/bin/env python3

from board import Board
from token import Token

if __name__ == '__main__':
    board = Board()
    board.display()
    token1 = Token('X')
    token2 = Token('O')

    board.drop(token1, 2)
    board.drop(token2, 2)

    while board.drop(token1, 7):
        pass

    board.display()
