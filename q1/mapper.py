#!/usr/bin/env python3
"""mapper.py"""
import sys

for line in sys.stdin:
    line = line.strip()

    docID, text = line.split('\t', 1)

    words = text.split()
    for word in words:
        print(f"{word}\t{docID}")