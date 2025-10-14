from word_count import f as f1
from word_count2 import f as f2
import timeit

str = input()

t1 = timeit.Timer("f1(str)", globals=globals())
print('f1: ', t1.autorange())
t2 = timeit.Timer("f2(str)", globals=globals())
print("f2: ", t2.autorange())
