def rec_func(a, b):
    if a == b:
        return f'{a}'

    if a > b:
        return f'{a}, {rec_func(a - 1, b)}'

    if a < b:
        return f'{a}, {rec_func(a + 1, b)}'

print(rec_func(1, 5))
