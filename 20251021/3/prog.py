from itertools import product
n=int(input())
print(*filter(lambda s: sum(s[i:i+3]=='TOR' for i in range(n-2))==2, map(''.join, product('ORT', repeat=n))), sep =', ')
