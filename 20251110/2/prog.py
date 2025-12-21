import math

class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass


def calculate_triangle_square(inp):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inp)
    except Exception:
        raise InvalidInput()

    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        x3 = float(x3)
        y3 = float(y3)
    except (ValueError, TypeError):
        raise BadTriangle()

    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    if a + b <= c or a + c <= b or b + c <= a:
        raise BadTriangle()

    area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

    if area < 1e-10:
        raise BadTriangle()

    return area

while True:
    try:
        inp = input()
        area = calculate_triangle_square(inp)

    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    except Exception:
        break
    else:
        print(f"{area:.2f}")


