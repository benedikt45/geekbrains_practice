year = int(input('Введите год для проверки: '))
answer_1 = 'Год високосный'
answer_2 = 'Год обычный'
if year % 4 != 0:
    print(answer_2)
else:
    if year % 100 != 0:
        print(answer_1)
    else:
        if year % 400 != 0:
            print(answer_2)
        else:
            print(answer_1)