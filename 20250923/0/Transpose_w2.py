list = []
while l := input():
    l = eval(l)
    list.append(l)

if all([len(l) == len(list) for l in list]):

    for i, _ in enumerate(list):
        for j in range(i, len(list)):
            list[i][j], list[j][i] = list[j][i], list[i][j]

    for i in list:
        print(*i)

else:
    print("not square")
