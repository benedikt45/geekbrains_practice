# Написать программу, которая будет складывать, вычитать, умножать или делить
# два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые
# данные для вычислений. Завершение программы должно выполняться при вводе
# символа '0' в качестве знака операции. Если пользователь вводит неверный
# знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова
# запрашивать знак операции. Также она должна сообщать пользователю о
# невозможности деления на ноль, если он ввел его в качестве делителя.

def calc(a, b, oper):
    temp_oper = oper
    while not valid_oper(temp_oper):
        temp_oper = input('Введите операцию еще раз ')
    if b == 0 and temp_oper == '/':
        return 'Деленине на ноль'
    if temp_oper == '0':
        print('До свидания')
        raise SystemExit
    elif temp_oper == '+':
        return a + b
    elif temp_oper == '-':
        return a - b
    elif temp_oper == '*':
        return a * b
    elif temp_oper == '/':
        return a / b


def valid_oper(oper):
    if oper == '0' or oper == '+' or oper == '-' or oper == '*' or oper == '/':
        return True
    else:
        return False


while True:
    a = int(input('Введите первое число '))
    b = int(input('Введите второе число '))
    oper = input('Введите операцию ')
    print(calc(a, b, oper))
