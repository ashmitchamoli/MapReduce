#!/usr/bin/env python3
"""reducer1.py"""
import sys

currPair = None
# mutualFriends = {}
pair = None
mutualFriends = set()

for line in sys.stdin:
    line = line.strip()

    # print(line)
    pair, value = line.split('\t', 1)

    if currPair == pair:
        mutualFriends.add(value)
    else:
        if currPair:
            print(f"{currPair}\t", end='')
            for f in sorted(mutualFriends):
                print(f"{f}", end=' ')
            print()
        mutualFriends = set([value])
        currPair = pair

if currPair == pair:
    print(f"{currPair}\t", end='')
    for f in sorted(mutualFriends):
        print(f"{f}", end=' ')
    print()