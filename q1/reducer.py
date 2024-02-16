#!/usr/bin/env python3
"""reducer.py"""
import sys

invertedIndex = {}

for line in sys.stdin:
    line = line.strip()

    word, docID = line.split('\t', 1)

    if word in invertedIndex:
        invertedIndex[word].add(docID)
    else:
        invertedIndex[word] = set([docID])

for word in invertedIndex:
    print(f"{word}", end='\t')
    for docID in invertedIndex[word]:
        print(f"{docID}", end=' ')
    print()

# ! combine both the loops later