#! /usr/bin/env python3

import sys

filename = sys.argv[1]

from collections import Counter

count = 0

hexamers_5 = Counter()
hexamers_3 = Counter()

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

       hexamer_5 = seq[0:6]
       hexamer_3 = seq[-6:]
       hexamers_5[hexamer_5] += 1
       hexamers_3[hexamer_3] += 1

for hexamer, count in hexamers_5.most_common(1):
    print("The most common hexamer at 5':", hexamer, count)

for hexamer, count in hexamers_3.most_common(1):
    print("The most common hexamer at 3':", hexamer, count)

