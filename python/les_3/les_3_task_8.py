# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу

import random


matrix = [[0 for _ in range(5)] for _ in range(4)]
for line in matrix:
    count = 1
    sum = 0
    for index, item in enumerate(line):
        if count == len(line):
            line[index] = sum
        else:
            line[index] = int(input('Введите число '))
            sum += line[index]
        count += 1
        #print(f'{line[index]:>5}', end='')
    #print()

print(matrix)

for i in matrix:
    for j in i:
        print(f'{j:5}', end='')
    print()