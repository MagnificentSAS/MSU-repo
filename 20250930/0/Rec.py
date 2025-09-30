def rec(n):
    return rec(n - 1) + 1 if n > 0 else 0


def rec_m(n):
    if n <= 0:
        print(cnt)
        return
    cnt += 1
    rec(n-1)
