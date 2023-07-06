#!/usr/bin/env python3

from ..games.progression_module import play_round
from ..game_module import play_game


def main():
    play_game('What number is missing in the progression?', play_round)


if __name__ == "__main__":
    main()
