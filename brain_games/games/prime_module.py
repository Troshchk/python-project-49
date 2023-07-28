#!/usr/bin/env python3

import random

MAX_RANDOM_NUMBER = 100
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_if_prime(number):
    if number == 1:
        return False
    for div in range(2, number // 2):
        if number % div == 0:
            return False
    return True


def is_valid_func(x):
    return x in ["yes", "no"],


def play_round():
    number = random.randint(1, MAX_RANDOM_NUMBER)
    question = f"Question: {number}"
    calculation_result = check_if_prime(number)
    return question, calculation_result
