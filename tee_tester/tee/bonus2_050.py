from argparse import ArgumentParser, FileType
import sys

parser = ArgumentParser()
parser.add_argument('files', nargs='*', type=FileType('wb'))
args = parser.parse_args()

for line in sys.stdin.buffer:
    sys.stdout.buffer.write(line)
    for f in args.files:
        f.write(line)
