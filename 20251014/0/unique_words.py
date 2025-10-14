str = input()

print(' '.join({i : 0 for i in str.split()}.keys()))
