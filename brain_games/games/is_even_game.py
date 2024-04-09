import random
from brain_games.games import game_interface


def game(user_name, yes='yes', no='no', tries=3):
    print(f'Answer "{yes}" if the number is even, otherwise answer "{no}".')
    for attempt in range(0, tries):
        number = random.randint(1, 100)
        question = f'Question: {number}'
        correct = yes if number % 2 == 0 else no
        is_answer_correct = game_interface.cli(question, correct, user_name)
        if not is_answer_correct:
            return
    print(f'Congratulations, {user_name}!')
