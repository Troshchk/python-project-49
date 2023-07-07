#!/usr/bin/env python3

import random
from .bool_game_module import is_valid, translate_to_bool, revert_answer

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
    if not is_valid(answer):
        string = "You entered invalid answer."
    else:
        if translate_to_bool(answer) == calculation_result:
            string = ""
        else:
            string = f"{answer} is wrong answer ;(. "\
                f"Correct answer was {revert_answer(answer)}."
    return string


def play_round():
    number = random.randint(1, MAX_RANDOM_NUMBER)
    question = f"Question: {number}"
    calculation_result = check_if_prime(number)
    return question, calculation_result
