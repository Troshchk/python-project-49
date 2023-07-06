#!/usr/bin/env python3

from ..games.prime_module import play_round
from ..game_module import play_game


def main():
    play_game('Answer "yes" if given number is prime. Otherwise answer "no".',
              play_round)


if __name__ == "__main__":
    main()
