from math import *

W, H = eval(input())
A, B = eval(input())

for line in range(0, H):
    x = line * (B - A) / (H - 1) + A
    y = sin(x)
    k = round((y + 1) * (W - 1) / 2)
    print(" "*k, "*")
