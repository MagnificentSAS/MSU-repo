from math import *

def Calc(s, t, u):
    f1 = eval('lambda x:' + s)
    f2 = eval('lambda x:' + t)
    f3 = eval('lambda x, y:' + u)
    def g(x):
        return f3(f1(x), f2(x))
    return g

s, t, u = eval(input())
i = eval(input())
print(Calc(s, t, u)(i))
