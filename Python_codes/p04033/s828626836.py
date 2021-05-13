#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

A, B = map(int, readline().split())

if A <= 0 and B >= 0:
    print("Zero")
elif A > 0:
    print("Positive")
else:
    print("Positive") if (B - A + 1) % 2 == 0 else print("Negative")
