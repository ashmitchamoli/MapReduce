#!/usr/bin/env python3
"""mapper2.py"""
import sys

startNode = 1
INFINITY = 11

for line in sys.stdin:
    line = line.strip()

    nodeId, nodeInfo = line.split('\t', 1)

    distance = None
    if nodeInfo[1] == ',':
        distance = int(nodeInfo[0])
    else:
        distance = int(nodeInfo[0:2])
    nodeId = int(nodeId)
    if distance < INFINITY:
        print(f"{nodeId}\t{distance}")
