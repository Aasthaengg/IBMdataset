#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

N, *A = map(int, read().split())

cnt = 0
acc = 0
for a in A:
    if a != 0:
        acc += a
    else:
        cnt += acc // 2
        acc = 0
cnt += acc // 2

print(cnt)
