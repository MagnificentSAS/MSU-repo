from decimal import Decimal as dec
from fractions import Fraction as frac

def multiplier(x, y, Type):
    return Type(x) * Type(y)

print(multiplier("1.1", "1.2", float))
print(multiplier("1.1", "1.2", dec))
print(multiplier("11/10", "12/10", frac))
