#!/usr/bin/env python3

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


def eval_answer(calculation_result, answer):
    if not answer.lstrip("-").isnumeric():
        string = "You entered invalid answer."
    else:
        if answer == calculation_result:
            string = ""
        else:
            string = f"{answer} is wrong answer ;(. "\
                f"Correct answer was {calculation_result}."
    return string


def play_round():
    number1 = random.randint(1, MAX_RANDOM_NUMBER)
    number2 = random.randint(1, MAX_RANDOM_NUMBER)
    operation = random.choice(["+", "-", "*"])
    calculation_result = evaluate_calculation(number1, number2, operation)
    question = f"Question: {number1} {operation} {number2}"
    return question, str(calculation_result)
