#!/usr/bin/env python3

from color import Color
from console import Console
from player import Player
from board import Board

class Game_Context_Creator:
    def __init__(self):
        pass

    def create(self):
        self.console = Console()
        self.first_player = Player(self.console, 'Eve', Color.RED)
        self.second_player = Player(self.console, 'Adam', Color.BLUE)
        self.board = Board(self.console)
        return self

if __name__ == '__main__':
    pass

