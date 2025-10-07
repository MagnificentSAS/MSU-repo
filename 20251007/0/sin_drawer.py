from math import *

W, H = eval(input())
A, B = eval(input())

def scale(a, b, A, B, x):
    return x * (B - A) / (b - a) + A


for line in range(0, H):
    x = scale(0, H - 1, A, B, line)
    y = sin(x)
    k = round((y + 1) * (W - 1) / 2)
    print(" "*k, "*")
