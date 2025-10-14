import timeit

f = input()
t = timeit.Timer(stmt=f)
t.autorange()

