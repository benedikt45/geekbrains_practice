# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
# собой (оба минимальны), так и различаться.

import random


mass = [random.randint(-100, 100) for _ in range(20)]
#mass = [1,-50,-50,-49,646,4811,-39]
print(mass)

elem = [0, 0]
count_elem = {}

for x in mass:
    if x in count_elem:
        count_elem[x] += 1
    else:
        count_elem[x] = 1

    if elem[0] > x:
        elem[0] = x
    elif elem[1] > x:
        elem[1] = x

if elem[0] > elem[1] and count_elem[elem[1]] > 1:
    print(elem[1] + ' ' + elem[1])
elif elem[1] > elem[0] and count_elem[elem[0]] > 1:
    print(elem[1] + ' ' + elem[1])
else:
    print(elem)

