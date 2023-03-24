#!/usr/bin/env python3

import prompt
import random
from .game_module import play_game


def find_gcd(number1, number2):
    small = min(number1, number2)
    big = max(number1, number2)
    for n in range(1, small + 1):
        if small % n == 0:
            potencial_divisor = small / n
            if small % potencial_divisor == 0 and big % potencial_divisor == 0:
                return int(potencial_divisor)


def play_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    gcd = find_gcd(number1, number2)  # alternative: math.gcd(number1, number2)
    print(f"Question: {number1} {number2}")
    answer = prompt.string("Your answer: ")
    answer = answer.strip()
    if not answer.isnumeric():
        string = "You entered invalid answer."
    else:
        if int(answer) == gcd:
            string = ""
        else:
            string = f"{answer} is wrong answer ;(. "\
                f"Correct answer was {gcd}."
    return string


def play_gcd():
    play_game('Find the greatest common divisor of given numbers.', play_round)
