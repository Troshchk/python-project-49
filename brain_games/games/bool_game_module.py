#!/usr/bin/env python3


def translate_to_bool(answer):
    if answer == "yes":
        return True
    elif answer == "no":
        return False


def evaluate_answer(calculation_result, answer, is_valid_func):
    if not is_valid_func(answer):
        return "You entered invalid answer."
    if answer in ["yes", "no"]:
        answer = translate_to_bool(answer)
    if answer == calculation_result:
        return ""
    return (
        f"{answer} is wrong answer ;(. "
        f"Correct answer was {calculation_result}."
    )
