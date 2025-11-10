def div(a, b, eps):
    try:
        if abs(b) < eps:
            raise ZeroDivisionError
        else:
            return a / b
    except ZeroDivisionError:
        print("b < eps")
