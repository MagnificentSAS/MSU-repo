def binN(n, ones, base=0):
    if n == 0:
        if ones == 0:
            print(base)
    else:
        if ones != 0:
            binN(n - 1, ones - 1, 2 * base + 1)

        binN(n - 1, ones, base * 2)
