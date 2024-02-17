#!/usr/bin/env python3
"""reducer1.py"""
import sys

mutualFriends = {}

for line in sys.stdin:
    line = line.strip()

    # print(line)
    key, value = line.split('\t', 1)

    if key in mutualFriends:
        mutualFriends[key].add(value)
    else:
        mutualFriends[key] = set([value])

for key in mutualFriends:
    print(f"{key}", end='\t')
    for value in sorted(list(mutualFriends[key])):
        print(f"{value}", end=' ')
    print()

# ! combine both the loops later