from argparse import ArgumentParser, FileType
import sys

parser = ArgumentParser()
parser.add_argument('files', nargs='*', type=FileType('wt'))
args = parser.parse_args()

for line in sys.stdin:
    sys.stdout.write(line)
    for f in args.files:
        f.write(line)
