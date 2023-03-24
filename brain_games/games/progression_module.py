#!/usr/bin/env python3

import prompt
import random
from ..game_module import play_game, MAX_RANDOM_NUMBER

MAX_PROGRESSION_LENGTH = 10


def play_round():
    start = random.randint(1, MAX_RANDOM_NUMBER)
    step = random.randint(1, MAX_RANDOM_NUMBER)
    progression = list(range(start,
                             start + step * MAX_PROGRESSION_LENGTH + 1,
                             step))
    position = random.randint(0, MAX_PROGRESSION_LENGTH)
    correct_answer = progression[position]
    progression_new = list(progression[:position]
                           + [".."]
                           + progression[position + 1:])
    progression_new = [str(element) for element in progression_new]
    print(f"Question: {' '.join(progression_new)}")
    answer = prompt.string("Your answer: ")
    answer = answer.strip()
    if not answer.isnumeric():
        string = "You entered invalid answer."
    else:
        if int(answer) == correct_answer:
            string = ""
        else:
            string = f"{answer} is wrong answer ;(. "\
                f"Correct answer was {correct_answer}."
    return string


def play_progression():
    play_game('What number is missing in the progression?', play_round)
