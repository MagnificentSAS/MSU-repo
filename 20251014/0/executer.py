str = input()
a, b = eval(input())

print(eval(str, {"x" : a, "y" : b}))
print(eval(str, {"x" : b, "y" : a}))
