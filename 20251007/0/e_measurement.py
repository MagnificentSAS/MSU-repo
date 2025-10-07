from decimal import getcontext
from decimal import Decimal as dec

def e_count(N, one):
    e = one
    curr = one
    for i in range(1, N + 1):
        curr /= i;
        e += curr

    return e

print(e_count(100, dec("1")))
getcontext().prec = 100
print(e_count(100, dec("1")))
print(e_count(100, 1.0))
