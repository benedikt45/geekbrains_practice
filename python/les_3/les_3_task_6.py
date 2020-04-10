# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

mass = [random.randint(-100, 100) for _ in range(20)]
data = {'max': [0, 0], 'min': [0, 0]}
sum = 0

print(mass)

for ind, value in enumerate(mass):
    if data['max'][1] < value:
        data['max'] = [ind, value]
    if data['min'][1] > value:
        data['min'] = [ind, value]


print(f'Минимум {data["min"][1]}; максимум {data["max"][1]}')

if data['min'][0] > data['max'][0]:
    for x in mass[data['max'][0]+1:data['min'][0]]:
        sum += int(x)
else:
    for x in mass[data['min'][0]+1:data['max'][0]+1]:
        sum += int(x)

print(f'Сумма {sum}')
