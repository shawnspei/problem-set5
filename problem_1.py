#! /usr/bin/env python3
import sys

filename = sys.argv[1]

from collections import Counter

counts = Counter()

for line in open(filename):
    if line.startswith('#'): continue
    fields = line.split('\t')
    chrom = fields[0]
    counts[chrom] += 1

for chrom, count in counts.items():
    print(chrom, count, sep = '\t')

sortme = [(v,k) for k,v in counts.items()]




