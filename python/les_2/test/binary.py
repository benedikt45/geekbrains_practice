def dec(m):
    i = 0
    bin = 0
    reverse_list = list(str(m)[::-1])
    for x in reverse_list:
        if x == '0':
            i += 1
            continue
        bin = bin + 2 ** i
        i += 1
    return bin

def bin(m):
    bin = ''
    while m > 0:
        if m % 2 == 0:
            bin = '0' + bin
        else:
            bin = '1' + bin
        m = m // 2
    return bin

print(dec(100010))
print(bin(34))