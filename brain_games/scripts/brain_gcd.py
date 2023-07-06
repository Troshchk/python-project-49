#!/usr/bin/env python3

from ..games.gcd_module import play_round
from ..game_module import play_game


def main():
    play_game('Find the greatest common divisor of given numbers.', play_round)


if __name__ == "__main__":
    main()
