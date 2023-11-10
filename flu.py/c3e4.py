# Using defaultdict is a useful mechanism to get the empty element added
import sys
import re
import collections


print(f"Total arguments {len(sys.argv)}")
print(f"The list is {sys.argv}")

WORD_RE = re.compile(r'\w+')
word_index = collections.defaultdict(list)

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        # The match is a word match and it prints individual word as returned by the \w
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # print(f"Matched the word {word} at {location}")
            # Get the list of occurances for the word "word"
            # The defaultdict now handles the addition of a new list
            # In case the missing wod it appends a empty list in place
            word_index[word].append(location)
# print the words in sorted way

for word in sorted(word_index, key=str.upper):
    print(word,word_index[word])
