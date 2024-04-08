import prompt
import random


def game(user_name, yes='yes', no='no', tries=3):
    print(f'Answer "{yes}" if the number is even, otherwise answer "{no}".')
    for attempt in range(0, tries):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        correct = yes if number % 2 == 0 else no
        if user_answer != correct:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {user_name}!")
            return
        print('Correct!')
    print(f'Congratulations, {user_name}!')
