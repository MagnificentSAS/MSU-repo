class CONST:
    a, b, c = input().split()

while s := input():
    match s.split():
        case [CONST.a, *tail] if "yes" in tail:
            print("1")
        case [CONST.b]:
            print("2")
        case [CONST.c, *mid] if mid[len(mid) - 1] == CONST.b:
            print("3")
        case _:
            print("WRONG")
