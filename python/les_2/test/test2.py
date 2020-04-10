def akkerman(m, n):
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return akkerman(m - 1, 1)
    if m > 0 and n > 0:
        return akkerman(m - 1, akkerman(m, n - 1))

print(akkerman(1, 5))