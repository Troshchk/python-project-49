import prompt
from .games.bool_game_module import evaluate_answer


MAX_ROUNDS = 3


def play_game(game):
    name = prompt.string("May I have your name? ")
    while len(name.strip()) == 0:
        name = prompt.string(
            "You entered empty name. " "May I have your real name? "
        )
    print(f"Hello, {name.strip()}!")
    print(game.RULES)
    for _ in range(MAX_ROUNDS):
        question, calculation_result = game.play_round()
        print(question)
        answer = prompt.string("Your answer: ")
        answer = answer.strip()
        string = evaluate_answer(calculation_result, answer, game.is_valid_func)
        if len(string) > 1:
            print(f"{string} Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
