#!/usr/bin/env python3
"""reducer0.py"""
import sys

friends = set()
currNode = None
node = None

for line in sys.stdin:
    line = line.strip()

    node, v = map(int, line.split('\t', 1))

    if currNode == node:
        friends.add(v)
    else:
        if currNode:
            for f1 in friends:
                for f2 in friends:
                    if f1 >= f2:
                        continue                    
                    print(f"{f1} {f2}\t{currNode}")
        friends = set([v])
        currNode = node

if currNode == node:
    for f1 in friends:
        for f2 in friends:
            if f1 >= f2:
                continue
            print(f"{f1} {f2}\t{currNode}")