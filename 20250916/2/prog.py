sum = 0
while (i := int(input())) > 0:
    sum += i
    if sum > 21:
        print(sum)
        break
else:
    print(i)
