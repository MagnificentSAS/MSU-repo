s = input()
pairs = set()

for i in range(len(s) - 1):
    c1, c2 = s[i], s[i+1]
    if c1.isalpha() and c2.isalpha():
        pair = c1.lower() + c2.lower()
        pairs.add(pair)

print(len(pairs))
