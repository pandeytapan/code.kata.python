from argparse import ArgumentParser, FileType
import sys

parser = ArgumentParser()
parser.add_argument('files', nargs='*', type=FileType('ab'))
parser.add_argument('-a', '--append', action='store_true')
args = parser.parse_args()

if not args.append:
    args.files = [open(f.name, mode='wb') for f in args.files]

for line in sys.stdin.buffer:
    sys.stdout.buffer.write(line)
    for f in args.files:
        f.write(line)
