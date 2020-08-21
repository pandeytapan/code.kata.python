from contextlib import nullcontext
import sys

with open(sys.argv[1], mode='wt') if len(sys.argv) > 1 else nullcontext() as f:
    for line in sys.stdin:
        sys.stdout.write(line)
        if f:
            f.write(line)
