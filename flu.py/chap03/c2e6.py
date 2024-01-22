# Looking at the usage of the bisect and the bisect_left function
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8 , 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}   {2}{0:<2d}'

def hay_search(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle, position, offset))


def grade(score): 
    breakpoint=[60,70,80,90]
    grades = "FDCBA"
    pos = bisect.bisect(breakpoint, score)
    return grades[pos]

if __name__ == '__main__':
    bisect_fn = bisect.bisect

    print('DEMO: ', bisect_fn.__name__)
    print('Haystack ->', ' '.join('%2d' % n for n in HAYSTACK))

    hay_search(bisect_fn)
    
    marks = 39
    print(f"{marks} will get grade {grade(marks)}")

    marks = 61
    print(f"{marks} will get grade {grade(marks)}") 
    
    marks = 94
    print(f"{marks} will get grade {grade(marks)}")
    
