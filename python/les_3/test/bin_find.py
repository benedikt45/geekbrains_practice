def bin_find(a, mass):
    pos = len(mass) // 2
    if a == mass[pos]:
        return pos
    elif len(mass) == 1:
        return -1
    elif a > mass[pos]:
        pos = bin_find(a, mass[pos:len(mass)])
    elif a < mass[pos]:
        pos = bin_find(a, mass[:pos])
    return pos

def bin_find_2(a, mass):
    left = 0
    right = len(mass) - 1
    pos = len(mass) // 2
    while mass[pos] != a and left <= right:
        if a > mass[pos]:
            left = pos + 1
        else:
            right = pos - 1
        pos = (left + right) // 2
    return -1 if left > right else pos



mass = [1, 3, 5, 6, 7, 99, 45, 879, 2313, 41241]


a = int(input('Введите число поиска '))
#bin_find(a, mass)
print(bin_find(a, mass))
