def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(gcd(36,48))
