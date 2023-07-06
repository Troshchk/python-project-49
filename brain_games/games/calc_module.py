#!/usr/bin/env python3

import prompt
import random
MAX_RANDOM_NUMBER = 100

RULES = 'What is the result of the expression?'


def evaluate_calculation(number1, number2, operation):
    if operation == "+":
        return (number1 + number2)
    elif operation == "-":
        return (number1 - number2)
    if operation == "*":
        return (number1 * number2)


def play_round():
    number1 = random.randint(1, MAX_RANDOM_NUMBER)
    number2 = random.randint(1, MAX_RANDOM_NUMBER)
    operation = random.choice(["+", "-", "*"])
    calculation_result = evaluate_calculation(number1, number2, operation)
    print(f"Question: {number1} {operation} {number2}")
    answer = prompt.string("Your answer: ")
    answer = answer.strip()
    if not answer.lstrip("-").isnumeric():
        string = "You entered invalid answer."
    else:
        if int(answer) == calculation_result:
            string = ""
        else:
            string = f"{answer} is wrong answer ;(. "\
                f"Correct answer was {calculation_result}."
    return string
