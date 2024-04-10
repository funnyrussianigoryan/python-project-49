import random
from brain_games.games import game_interface
from brain_games.games.game_tools import check_prime


def game(user_name, yes='yes', no='no', tries=3):
    print(f'Answer "{yes}" if given number is prime. Otherwise answer "{no}".')
    for attempt in range(0, tries):
        number = random.randint(1, 50)
        question = f'Question: {number}'
        correct = yes if check_prime.is_prime(number) else no
        is_answer_correct = game_interface.cli(question, correct, user_name)
        if not is_answer_correct:
            return
    print(f'Congratulations, {user_name}!')
