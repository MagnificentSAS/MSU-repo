import timeit

def letter_counter(str):
    a = set()
    b = set()
    for l in str:
        if l in "aeyuio":
            a.add(l)
        if l in "qwrtpsdfghjklzxcvbnm":
            b.add(l)

    return len(a), len(b)

str = input()
# print(*letter_counter(str))
t = timeit.Timer("letter_counter(str)", globals=globals())
print(t.autorange())
