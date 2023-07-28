#!/usr/bin/env python3

import random

MAX_PROGRESSION_LENGTH = 10
MAX_RANDOM_NUMBER = 100
RULES = "What number is missing in the progression?"


def is_valid_func(x):
    return x.isnumeric()


def play_round():
    start = random.randint(1, MAX_RANDOM_NUMBER)
    step = random.randint(1, MAX_RANDOM_NUMBER)
    progression = list(
        range(start, start + step * MAX_PROGRESSION_LENGTH + 1, step)
    )
    position = random.randint(0, MAX_PROGRESSION_LENGTH)
    calculation_result = progression[position]
    progression_new = list(
        progression[:position] + [".."] + progression[position + 1:]
    )
    progression_new = [str(element) for element in progression_new]
    question = f"Question: {' '.join(progression_new)}"
    return question, str(calculation_result)
