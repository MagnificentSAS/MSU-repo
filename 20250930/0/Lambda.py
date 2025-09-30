args = eval(input())
print(sorted(args, key = lambda x: x * x % 100))
