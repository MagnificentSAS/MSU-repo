class Rectangle:
    rectcnt = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.__class__.rectcnt}", self.__class__.rectcnt)

    def __str__(self):
        return f"{self.__class__.rectcnt} ({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"

    def __lt__(self, other):
        y_s = self.y2 - self.y1
        x_s = self.x2 - self.x1
        y_o = other.y2 - other.y1
        x_o = other.x2 - other.x1
        S1 = x_s * y_s
        S2 = x_o * y_o
        return S1 < S2

    def __eq__(self, other):
        y_s = self.y2 - self.y1
        x_s = self.x2 - self.x1
        y_o = other.y2 - other.y1
        x_o = other.x2 - other.x1
        return y_s == y_o and x_s == x_o

    def __mul__(self, num):
        return self.__class__(self.x1 * num, self.y1 * num, self.x2 * num, self.y2 * num)

    def __rmul__(self, num):
        return self.__class__(self.x1 * num, self.y1 * num, self.x2 * num, self.y2 * num)
