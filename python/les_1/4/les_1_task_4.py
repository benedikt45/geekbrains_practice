a = input('Введите первый символ ').lower()
b = input('Введите второй символ ').lower()
first_pos = ord(a) - ord('a') +1
second_pos = ord(b) - ord('a') +1
count_letters = second_pos-first_pos-1
print(f'Позиция первого символа {first_pos}')
print(f'Позиция второго символа {second_pos}')
print(f'Между ними {count_letters} символов')