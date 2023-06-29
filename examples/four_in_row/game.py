#!/usr/bin/env python3

from game_context_creator import Game_Context_Creator
from board import Board
from player import Player
from console import Console


class Game:
    def __init__(self, game_context):
        self.__current_player = game_context.first_player
        self.__next_player = game_context.second_player
        self.__console = game_context.console
        self.__board = game_context.board

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
