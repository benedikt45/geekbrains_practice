# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random


mass = [random.randint(-100, 100) for _ in range(100)]
max_min = 0
print(mass)

for x in mass:
    if max_min == 0 and x < 0:
        max_min = x
    elif max_min < x < 0 and x != 0:
        max_min = x

if max_min >= 0:
    print('В массиве нет отрицательных элементов')
else:
    print(f'В массиве найти максимальный отрицательный элемент: {max_min}')