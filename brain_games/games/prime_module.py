#!/usr/bin/env python3

import random
from .bool_game_module import translate_to_bool, evaluate_answer

MAX_RANDOM_NUMBER = 100
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_if_prime(number):
    if number == 1:
        return False
    for div in range(2, number // 2):
        if number % div == 0:
            return False
    return True


def eval_answer(calculation_result, answer):
    return evaluate_answer(
        calculation_result,
        answer,
        is_valid_func=lambda x: x in ["yes", "no"],
        compare_func=lambda x, y: translate_to_bool(x) == y,
    )


def play_round():
    number = random.randint(1, MAX_RANDOM_NUMBER)
    question = f"Question: {number}"
    calculation_result = check_if_prime(number)
    return question, calculation_result
