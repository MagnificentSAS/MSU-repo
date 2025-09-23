list = eval(input())
for i in list:
    if i % 2:
        print(i)
        break
else:
    print(list[0])
