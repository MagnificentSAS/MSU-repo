match int(input()):
    case 1:
        print("ОДИН")
    case 2:
        print("DWA")
    case 3:
        print("TRI")
    case var if var % 2 == 0:
        print(var, "is ЧЕТНОЕ")
    case n:
        print(n, "is MNOgO")
