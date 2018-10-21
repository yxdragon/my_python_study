def fib(n):
    a, b = 1, 0
    lst = []
    for i in range(n):
        c = a + b
        a, b = b, c
        lst.append(c)
    return lst

print(fib(8))
