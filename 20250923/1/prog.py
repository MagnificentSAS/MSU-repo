M, N = eval(input())
print([x for x in range(max(M, 2), N) if all([x % i != 0 for i in range(2, x // 2 + 1)])])
