#!/usr/bin/env python3

from ..games.even_module import play_round
from ..game_module import play_game


def main():
    play_game('Answer "yes" if the number is even, otherwise answer "no".',
              play_round)


if __name__ == "__main__":
    main()
