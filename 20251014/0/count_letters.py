str = input()

a = set()
b = set()
for l in str:
    if l in "aeyuio":
        a.add(l)
    if l in "qwrtpsdfghjklzxcvbnm":
        b.add(l)

print(len(a), len(b))
