import sys

f = open(sys.argv[1], mode='wt') if len(sys.argv) > 1 else None

for line in sys.stdin:
    print(line, end='')
    if f:
        print(line, end='', file=f)
