from argparse import ArgumentParser
from pathlib import Path
import sys

parser = ArgumentParser()
parser.add_argument('files', nargs='*', type=Path)
parser.add_argument(
    '-a',
    '--append',
    dest='mode',
    action='store_const',
    const='ab',
    default='wb',
)
args = parser.parse_args()

files = []
for path in args.files:
    try:
        files.append(open(path, mode=args.mode))
    except OSError as e:
        parser.error(f"Can't open {path}: {e}")

for line in sys.stdin.buffer:
    sys.stdout.buffer.write(line)
    for f in files:
        f.write(line)
