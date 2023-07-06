#!/usr/bin/env python3

import prompt

MAX_ROUNDS = 3


def play_game(game):
    name = prompt.string("May I have your name? ")
    while len(name.strip()) == 0:
        name = prompt.string("You entered empty name."
                             "May I have your real name? ")
    print(f"Hello, {name.strip()}!")
    print(game.RULES)
    for _ in range(MAX_ROUNDS):
        round_result = game.play_round()
        if len(round_result) > 1:
            print(f"{round_result} Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
