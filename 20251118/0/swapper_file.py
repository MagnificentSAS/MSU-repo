import sys

with open(sys.argv[1], 'rb') as f:
    bytes = f.read()
    len = len(bytes) // 2

with open(sys.argv[1], 'wb') as f:
    f.write(bytes[len:] + bytes[:len])
