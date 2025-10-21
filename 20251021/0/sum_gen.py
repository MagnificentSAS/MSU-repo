def sum_gen(n):
    sum = 0.0
    curr = 0.0
    while curr <= n:
        yield (sum := sum + 1 / (curr := curr + 1.0) / curr)
