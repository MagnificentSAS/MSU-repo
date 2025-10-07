from math import *

W, H = eval(input())
A, B = eval(input())

def scale(a, b, A, B, x):
    return (x-a) * (B - A) / (b - a) + A


screen = [['.'] * W for _ in range(H)]

for line in range(0, W):
    x = scale(0, W - 1, A, B, line)
    y = sin(x)
    k = round(scale(-1,1,0,H-1,y))
    screen[H - k - 1][line] = '*'

print('\n'.join([''.join(screen[i]) for i in range(H)]))


