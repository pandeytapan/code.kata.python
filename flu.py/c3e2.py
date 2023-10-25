import sys
import re

print(f"Total arguments {len(sys.argv)}")
print(f"The list is {sys.argv}")
WORD_RE = re.compile(r'\w+')

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        # The match is a word match and it prints individual word as returned by the \w
        for MATCH in WORD_RE.finditer(line):
            print(MATCH)
