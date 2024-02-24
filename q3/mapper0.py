#!/usr/bin/env python3
"""mapper0.py"""
import sys

startNode = 1
INFINITY = 11

for line in sys.stdin:
    line = line.strip()

    nodeId, neighborList = line.split("\t", 1)

    if int(nodeId) == startNode:
        print(f"{nodeId}\t0,{neighborList}")
    else:
        print(f"{nodeId}\t{INFINITY},{neighborList}")