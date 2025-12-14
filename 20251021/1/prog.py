import sys

def fib(m, n):
    a, b = 1, 1
    for _ in range(m):
        a, b = b, a + b
    for _ in range(n):
        yield a
        a, b = b, a + b

exec(sys.stdin.read())
