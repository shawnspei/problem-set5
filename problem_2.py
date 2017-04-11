#! /usr/bin/env python3

import sys

filename = sys.argv[1]

from collections import Counter

count = 0
bases = Counter()

for line in open(filename):
    line = line.rstrip()

    if count == 0:
       count += 1

    elif count == 1:
       seq = line
       count += 1

    elif count == 2:
       count += 1

    elif count == 3:
       count = 0

       for base in seq:
           bases[base] += 1

for base, count in bases.items():
    print(base, count)



