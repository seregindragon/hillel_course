def fibonachi(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


fib = fibonachi(20)
for i in fib:
    print(i)
