#!/usr/bin/env python3

import random
from .bool_game_module import evaluate_answer


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


def eval_answer(calculation_result, answer):
    return evaluate_answer(
        calculation_result, answer, is_valid_func=lambda x: x.isnumeric()
    )


def play_round():
    number1 = random.randint(1, MAX_RANDOM_NUMBER)
    number2 = random.randint(1, MAX_RANDOM_NUMBER)
    calculation_result = find_gcd(number1, number2)  # alt: math.gcd(num1, num2)
    question = f"Question: {number1} {number2}"
    return question, calculation_result
