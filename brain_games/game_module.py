#!/usr/bin/env python3

import prompt

MAX_ROUNDS = 3


def play_game(game):
    name = prompt.string("May I have your name? ")
    while len(name.strip()) == 0:
        name = prompt.string("You entered empty name. "
                             "May I have your real name? ")
    print(f"Hello, {name.strip()}!")
    print(game.RULES)
    for _ in range(MAX_ROUNDS):
        question, calculation_result = game.play_round()
        print(question)
        answer = prompt.string("Your answer: ")
        answer = answer.strip()
        string = game.eval_answer(calculation_result, answer)
        if len(string) > 1:
            print(f"{string} Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
