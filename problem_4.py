import sys
filename = sys.argv[1]

from collections import Counter
from pysam import AlignmentFile
from pysam import AlignedSegment


strands = Counter()
mismatches = Counter()
counts = 0

bamfile = AlignmentFile(filename)

for record in bamfile:
    strand = record.flag
    strands[strand] += 1
    nm = record.get_tag("NM")
    mismatches[nm] += 1

for strand, count in strands.items():
    if strand == 16:
        print("Total number of alignments on the positive strand:", count)
    else:
        print("Total number of alignments on the negative strand:", count)

for nm, count in mismatches.items():
    if nm == 0:
        print("Total number of alignments with no mismatches:", count)
    else:
        counts += count
print("Total number of alignments with more than zero mismathces:", counts)





