fl = False
while inp := input():
    if int(inp) == 13:
        fl = True
        print("13 :(")
        break
    elif int(inp) % 2 == 0:
        print(inp)

if not fl:
    print("GOOD")
