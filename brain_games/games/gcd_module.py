#!/usr/bin/env python3

import random


MAX_RANDOM_NUMBER = 100
RULES = "Find the greatest common divisor of given numbers."


def find_gcd(number1, number2):
    small = min(number1, number2)
    big = max(number1, number2)
    for n in range(1, small + 1):
        if small % n == 0:
            potencial_divisor = small / n
            if small % potencial_divisor == 0 and big % potencial_divisor == 0:
                return int(potencial_divisor)


def is_valid_func(x):
    return x.isnumeric()


def play_round():
    number1 = random.randint(1, MAX_RANDOM_NUMBER)
    number2 = random.randint(1, MAX_RANDOM_NUMBER)
    calculation_result = find_gcd(number1, number2)  # alt: math.gcd(num1, num2)
    question = f"Question: {number1} {number2}"
    return question, str(calculation_result)
