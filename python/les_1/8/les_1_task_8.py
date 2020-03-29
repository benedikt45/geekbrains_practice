a = int(input('Введите число 1 '))
b = int(input('Введите число 2 '))
c = int(input('Введите число 3 '))

if a > b:
    if c>a:
        print(f'Среднее число {a}')
    else:
        if c > b:
            print(f'Среднее число {c}')
        else:
            print(f'Среднее число {b}')
else:
    if c > b:
        print(f'Среднее число  {b}')
    else:
        if c > a:
            print(f'Среднее число {c}')
        else:
            print(f'Среднее число {a}')
