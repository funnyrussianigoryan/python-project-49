import random
from brain_games.games import game_interface
from brain_games.games.game_tools import calc_game_functions


def game(user_name, tries=3):
    print('What is the result of the expression?')
    for attempt in range(0, tries):
        type_num = random.randint(1, calc_game_functions.get_function_count())
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        game_function = calc_game_functions.get_function(type_num)
        question, correct = game_function(num1, num2)
        is_answer_correct = game_interface.cli(question, correct, user_name)
        if not is_answer_correct:
            return
    print(f'Congratulations, {user_name}!')
