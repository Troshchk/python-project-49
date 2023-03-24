#!/usr/bin/env python3

import prompt


def play_game(instruction_string, eval_function):
    name = prompt.string("May I have your name? ")
    while len(name.strip()) == 0:
        name = prompt.string("You entered empty name."
                             "May I have your real name? ")
    print(f"Hello, {name.strip()}!\n"
          f'{instruction_string}')
    counter = 0
    while counter < 3:
        round_result = eval_function()
        if len(round_result) < 1:
            counter += 1
        else:
            print(f"{round_result} Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")