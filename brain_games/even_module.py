#!/usr/bin/env python3

import prompt
import random
from .game_module import play_game
from .bool_game_module import is_valid, translate_to_bool, revert_answer


def check_if_even(number):
    return not number % 2


def play_round():
    number = random.randint(1, 100)
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    answer = answer.strip()
    if not is_valid(answer):
        string = "You entered invalid answer."
    else:
        if translate_to_bool(answer) == check_if_even(number):
            string = ""
        else:
            string = f"{answer} is wrong answer ;(. "\
                f"Correct answer was {revert_answer(answer)}."
    return string


def play_even_game():
    play_game('Answer "yes" if the number is even, otherwise answer "no".',
              play_round)
