#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, M = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(M)]

R = [False] * (N + 1)
num = [1] * (N + 1)

R[1] = True

for x, y in Q:
    R[y] = R[x] or R[y]
    num[x] -= 1
    num[y] += 1

    if num[x] <= 0:
        R[x] = False

print(R.count(True))