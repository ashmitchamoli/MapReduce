#!/usr/bin/env python3
"""reducer1.py"""
import sys

startNode = 1
INFINITY = 11

nodeDistances = {}
nodeNeighbors = {}

for line in sys.stdin:
    line = line.strip()

    nodeId, nodeInfo = line.split('\t', 1)

    if nodeInfo[0] == 'N':
        nodeNeighbors[nodeId] = nodeInfo[2:]
        continue

    distance = int(nodeInfo)

    if nodeId in nodeDistances:
        nodeDistances[nodeId] = min(nodeDistances[nodeId], distance)
    else:
        nodeDistances[nodeId] = distance
    
for nodeId in nodeDistances:
    print(f"{nodeId}\t{nodeDistances[nodeId]},{nodeNeighbors[nodeId]}")