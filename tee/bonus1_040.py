import sys

files = [
    open(name, mode='wt')
    for name in sys.argv[1:]
]

for line in sys.stdin:
    sys.stdout.write(line)
    for f in files:
        f.write(line)
