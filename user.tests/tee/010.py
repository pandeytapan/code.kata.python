import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1], mode='wt')
else:
    f = None

for line in sys.stdin:
    sys.stdout.write(line)
    if f:
        f.write(line)
