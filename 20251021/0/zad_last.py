from itertools import repeat

def repeater(seq, n):
    for i in seq:
        for j in repeat(i, n):
            yield j
