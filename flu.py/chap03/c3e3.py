import sys
import re

print(f"Total arguments {len(sys.argv)}")
print(f"The list is {sys.argv}")

WORD_RE = re.compile(r'\w+')
word_index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        # The match is a word match and it prints individual word as returned by the \w
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # print(f"Matched the word {word} at {location}")
            # Get the list of occurances for the word "word"
            # The line below replaces the dict.get() and following the append() afterwards
            # Its good to use dict.get(key) instead of dict[key] and better to use setdefault()
            # in case we know that the key has chances of being missing
            word_index.setdefault(word,[]).append(location)
# print the words in sorted way

for word in sorted(word_index, key=str.upper):
    print(word,word_index[word])
