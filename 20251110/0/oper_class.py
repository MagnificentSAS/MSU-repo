class A:
    def __init__(self, v):
        self.val = v

    def __add__(self, other):
        return self.__class__(self.val + self.other)

    def __str__(self):
        return f"<{self.val}>"

class B(A):
    def __str__(self):
        return f">{self.val}<"
