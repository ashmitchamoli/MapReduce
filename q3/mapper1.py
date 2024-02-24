#!/usr/bin/env python3
"""mapper1.py"""
import sys

startNode = 1
INFINITY = 11

for line in sys.stdin:
    line = line.strip()

    nodeId, nodeInfo = line.split('\t', 1)

    distance, neighborList = nodeInfo.split(',', 1)

    distance = int(distance)
    nodeId = int(nodeId)
    if distance < INFINITY:
        for neighbor in neighborList.split():
            print(f"{neighbor}\t{distance+1}")

    print(f"{nodeId}\t{distance}")          # print your own distance from start node
    print(f"{nodeId}\tN {neighborList}")    # pass on the graph structure forward