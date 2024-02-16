#!/usr/bin/env python3
"""reducer1.py"""
import sys

mutualFriends = {}

for line in sys:
    line = line.strip()

    key, value = line.split('\t', 1)

    if key in mutualFriends:
        mutualFriends[key].add(value)
    else:
        mutualFriends[key] = set([value])
    
for key in mutualFriends:
    print(f"{key}", end='\t')
    for value in mutualFriends[key]:
        print(f"{value}", end=' ')
    print()