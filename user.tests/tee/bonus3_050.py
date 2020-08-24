from argparse import ArgumentParser
import sys

parser = ArgumentParser()
parser.add_argument('files', nargs='*')
parser.add_argument(
    '-a',
    '--append',
    dest='mode',
    action='store_const',
    const='ab',
    default='wb',
)
args = parser.parse_args()

files = [
    open(filename, mode=args.mode)
    for filename in args.files
]

for line in sys.stdin.buffer:
    sys.stdout.buffer.write(line)
    for f in files:
        f.write(line)
