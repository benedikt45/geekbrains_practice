
def test_fib(func):
    lst = [0, 1 , 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(test_fib(fib))