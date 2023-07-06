#!/usr/bin/env python3

from ..games.calc_module import play_round
from ..game_module import play_game


def main():
    play_game('What is the result of the expression?', play_round)


if __name__ == "__main__":
    main()
