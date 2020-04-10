# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def calc(a):
    even = 0
    odd = 0
    for chr in a:
        if int(chr) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (odd, even)

a = input('Введите число ')
odd, even = calc(a)
print(f'Четных {even}, нечетных {odd}')
