#!/usr/bin/env python3

import random
from .bool_game_module import is_valid, translate_to_bool

MAX_RANDOM_NUMBER = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_if_even(number):
    return not number % 2


def eval_answer(calculation_result, answer):
    if not is_valid(answer):
        string = "You entered invalid answer."
    else:
        if translate_to_bool(answer) == calculation_result:
            string = ""
        else:
            string = f"{answer} is wrong answer ;(. "\
                f"Correct answer was {calculation_result}."
    return string


def play_round():
    number = random.randint(1, MAX_RANDOM_NUMBER)
    question = f"Question: {number}"
    calculation_result = check_if_even(number)
    return question, calculation_result
