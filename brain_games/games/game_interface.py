import prompt


def cli(question, correct, user_name):
    print(question)
    answer = prompt.string('Your answer: ')
    if answer != str(correct):
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {user_name}!")
        return False
    print('Correct!')
    return True
