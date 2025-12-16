n = int(input())

for i in range(3):
    a = n + i
    for j in range(3):
        b = n + j
        m = a * b
        res = m
        s = 0
        print(a, '*', b, '=', end = ' ')
        while m != 0:
            s += m % 10
            m //= 10
            if s < 6:
                continue
            if s > 6:
                # print(s, '>6')
                print(res, end = ' ' if j < 2 else '\n')
                break
        else:
            # print(s, '<=6')
            print(res if s != 6 else ':=)', end = ' ' if j < 2 else '\n')
# print()
