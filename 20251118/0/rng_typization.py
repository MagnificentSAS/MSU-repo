import random
import struct

seq = [(random.random(), bytes(random.sample(range(5),3)), random.randrange(10000)) for i in range(10)]

with open('file_rng', 'bw+') as f:
    for s in seq:
        b = struct.pack('f3si', *s)
        f.write(b)

with open('file_rng', 'br') as fin:
    with open('fout_rng', 'bw+') as fout:
        size = fin.seek(0, 2)
        fin.seek(0)
        while s := fin.read(size // 10):
            w = fout.write(s)
