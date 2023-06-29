#!/usr/bin/env python3

from game_context_creator import Game_Context_Creator
from game import Game


def main():
    context = Game_Context_Creator()
    game = Game(context.create())
    game.run()

if __name__ == '__main__':
    main()
