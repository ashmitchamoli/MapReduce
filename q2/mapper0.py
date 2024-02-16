#!/usr/bin/env python3
"""mapper0.py"""
import sys

for line in sys.stdin:
    line = line.strip()
    u, v = line.split()

    print(f"{u}\t{v}")
    print(f"{v}\t{u}")