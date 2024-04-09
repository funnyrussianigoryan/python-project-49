def plus(num1, num2):
    question = f'Question: {num1} + {num2}'
    correct_answer = num1 + num2
    return question, correct_answer


def minus(num1, num2):
    if num1 - num2 < 0:
        num1, num2 = num2, num1
    question = f'Question: {num1} - {num2}'
    correct_answer = num1 - num2
    return question, correct_answer


def multiply(num1, num2):
    question = f'Question: {num1} * {num2}'
    correct_answer = num1 * num2
    return question, correct_answer


NUMBER_TO_FUNC = {
    1: plus,
    2: minus,
    3: multiply
}


def get_function(num):
    return NUMBER_TO_FUNC[num]


def get_function_count():
    return len(NUMBER_TO_FUNC)
