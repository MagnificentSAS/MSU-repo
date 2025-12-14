import sys
from itertools import tee, islice

def slide(seq, n):
    iters = tee(seq, len(seq))

    shifted = (islice(it, k, k + n) for k, it in enumerate(iters))

    for slice in shifted:
        yield from slice

exec(sys.stdin.read())
