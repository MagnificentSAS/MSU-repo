import sys
from collections import UserString
from math import ceil

class DivStr(UserString):
    def __init__(self, seq=""):
        super().__init__(seq)

    def __floordiv__(self, n: int):
        s = self.data
        base = len(s) // n

        def gen():
            start = 0
            for i in range(n):
                part_len = base
                yield s[start:start + part_len]
                start += part_len

        return gen()

    def __mod__(self, n: int):
        s = self.data
        tail_len = len(s) % n
        if tail_len == 0:
            return self.__class__("")
        return self.__class__(s[-tail_len:])

exec(sys.stdin.read())
