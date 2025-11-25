class CONST:
    A = 100500

match eval(input()):
    case "QWE":
        print("QWE!")
    case "A" | "B" as s:
        print("Letter", s)
    case CONST.A:
        print("StoPyatsot")
    case int(n) if n > 0:
        print(f"POSITIVE: {int(n)}")
    case int(n):
        print(f"NOT POSITIVE: {int(n)}")
    case (0, *tail):
        print("Zero tuple", tail)
    case (float(n) | int(n), *tail):
        print(f"{n}-tuple", tail)
    case _:
        print("Unknown")
