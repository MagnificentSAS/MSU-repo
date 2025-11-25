match eval(input()):
    case "QWE":
        print("QWE!")
    case "A" | "B" as s:
        print("Letter", s)
    case int(n):
        print(f"INT: {int(n)}")
    case (0, *tail):
        print("Zero tuple", tail)
    case (float(n) | int(n), *tail):
        print(f"{n}-tuple", tail)
    case _:
        print("Unknown")
