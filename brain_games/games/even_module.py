#!/usr/bin/env python3

import random

MAX_RANDOM_NUMBER = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_if_even(number):
    return not number % 2


def is_valid_func(x):
    return x in ["yes", "no"],


def play_round():
    number = random.randint(1, MAX_RANDOM_NUMBER)
    question = f"Question: {number}"
    calculation_result = check_if_even(number)
    return question, calculation_result
