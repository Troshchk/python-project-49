#!/usr/bin/env python3

import random
from bool_game_module import evaluate_answer

MAX_RANDOM_NUMBER = 100

RULES = "What is the result of the expression?"


def evaluate_calculation(number1, number2, operation):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    if operation == "*":
        return number1 * number2


def eval_answer(calculation_result, answer):
    return evaluate_answer(
        calculation_result,
        answer,
        is_valid_func=lambda x: x.lstrip("-").isnumeric(),
    )


def play_round():
    number1 = random.randint(1, MAX_RANDOM_NUMBER)
    number2 = random.randint(1, MAX_RANDOM_NUMBER)
    operation = random.choice(["+", "-", "*"])
    calculation_result = evaluate_calculation(number1, number2, operation)
    question = f"Question: {number1} {operation} {number2}"
    return question, str(calculation_result)
