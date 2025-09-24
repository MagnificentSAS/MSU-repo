lst = list(eval(input()))

for i in range(1, len(lst)):
    fl = True
    for j in range(len(lst) - i):
        if lst[j] ** 2 % 100 > lst[j + 1] ** 2 % 100:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            fl = False
    if fl:
        break

print(lst)
