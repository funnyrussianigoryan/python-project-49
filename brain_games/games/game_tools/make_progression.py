def make_progression(k, b, progression_len=10):
    progression = []
    for x in range(0, progression_len):
        y = k * x + b
        progression.append(y)
    return progression
