import sys

with open(sys.argv[1], 'r') as f:
    strs = f.readlines()

with open(sys.argv[1], 'w') as f:
    print(*sorted(strs), file=f)
