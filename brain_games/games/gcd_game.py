import random
from brain_games.games import game_interface
from brain_games.games.game_tools import gcd


def game(user_name, tries=3):
    print('Find the greatest common divisor of given numbers.')
    for attempt in range(0, tries):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = f'Question: {num1} {num2}'
        correct = gcd.calc_gcd(num1, num2)
        is_answer_correct = game_interface.cli(question, correct, user_name)
        if not is_answer_correct:
            return
    print(f'Congratulations, {user_name}!')
