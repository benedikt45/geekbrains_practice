# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

mass = [x for x in range(2, 100)]
mass_2 = [x for x in range(2, 10)]
answer = {}

for i in mass:
    for j in mass_2:
        if i % j == 0:
            if j in answer:
                answer[j] += 1
            else:
                answer[j] = 1

for key in answer:
    print(f'Кратно {key}: {answer[key]}')