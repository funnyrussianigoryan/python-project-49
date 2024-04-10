import random
from brain_games.games import game_interface
from brain_games.games.game_tools import make_progression


def game(user_name, progression_len=10, tries=3):
    print('What number is missing in the progression?')
    for attempt in range(0, tries):
        k = random.randint(1, 10)
        b = random.randint(1, 20)
        progression = make_progression.make_progression(k, b, progression_len)
        item_num = random.randint(0, progression_len - 1)
        correct_num = progression[item_num]
        progression[item_num] = '..'
        progression_str = [str(num) for num in progression]
        question = f'Question: {" ".join(progression_str)}'
        is_answer_correct = game_interface.cli(question, correct_num, user_name)
        if not is_answer_correct:
            return
    print(f'Congratulations, {user_name}!')
