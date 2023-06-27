#!/usr/bin/env python3

from board import Board
from player import Player
from color import Color
from console import Console


class Game:
    def __init__(self):
        self.__current_player = Player('Eve', Color.RED)
        self.__next_player = Player('Adam', Color.BLUE)
        self.__console = Console()
        self.__board = Board(self.__console)

    def run(self):
        self.__board.render()
        self.__console.display()

        while not self.__board.is_full():

            try:
                column = self.__current_player.get_column()
            except ValueError:
                print('Incorrect input format. Try again!')
                continue

            if column < 1 or column > self.__board.board_width:
                print('Incorrect column. Try again!')
                continue

            token = self.__current_player.get_token()

            if not self.__board.drop(token, column):
                print('Column is full. Try again!')
                continue

            # Swap players
            self.__current_player, self.__next_player = (
                    self.__next_player, self.__current_player)

            self.__board.render()
            self.__console.display()

        print('End game. Board is full.')


if __name__ == '__main__':
    game = Game()
    game.run()
