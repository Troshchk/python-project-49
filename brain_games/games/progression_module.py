#!/usr/bin/env python3

import random

MAX_PROGRESSION_LENGTH = 10
MAX_RANDOM_NUMBER = 100
RULES = 'What number is missing in the progression?'


def eval_answer(calculation_result, answer):
    if not answer.isnumeric():
        string = "You entered invalid answer."
    else:
        if int(answer) == calculation_result:
            string = ""
        else:
            string = f"{answer} is wrong answer ;(. "\
                f"Correct answer was {calculation_result}."
    return string


def play_round():
    start = random.randint(1, MAX_RANDOM_NUMBER)
    step = random.randint(1, MAX_RANDOM_NUMBER)
    progression = list(range(start,
                             start + step * MAX_PROGRESSION_LENGTH + 1,
                             step))
    position = random.randint(0, MAX_PROGRESSION_LENGTH)
    calculation_result = progression[position]
    progression_new = list(progression[:position]
                           + [".."]
                           + progression[position + 1:])
    progression_new = [str(element) for element in progression_new]
    question = f"Question: {' '.join(progression_new)}"
    return question, calculation_result
