A = '-'
B = '-'
C = '-'
n = int(input())
if n % 8 == 0:
    C = '+'

if n % 25 == 0:
    if n % 2 == 0:
        A = '+'
    else:
        B = '+'

print('A', A, 'B', B, 'C', C)
