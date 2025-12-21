import sys

buf = sys.stdin.buffer.read()

N = buf[0]
tail = buf[1:]
tail_len = len(tail)

if N == 0:
    res = buf
else:
    parts = []
    for i in range(N):
        start = round(i * tail_len / N)
        end = round((i + 1) * tail_len / N)
        part = tail[start:end]
        parts.append(part)

    parts.sort()

    res = bytes([N]) + b"".join(parts)

sys.stdout.buffer.write(res)