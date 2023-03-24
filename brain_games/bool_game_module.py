#!/usr/bin/env python3


def is_valid(answer):
    return answer in ["yes", "no"]


def translate_to_bool(answer):
    if answer == "yes":
        return True
    elif answer == "no":
        return False


def revert_answer(answer):
    if answer == "yes":
        return "no"
    elif answer == "no":
        return "yes"

