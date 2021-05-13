import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


N, L = list(map(int, sys.stdin.buffer.readline().split()))
A = list(map(int, sys.stdin.buffer.readline().split()))

A = np.array(A, dtype=int)

s = A[1:] + A[:-1]

if s.max() >= L:
    print('Possible')
    last = s.argmax()
    ans = list(range(N - 1))
    for i in range(last):
        print(i + 1)
    for i in reversed(range(last + 1, N - 1)):
        print(i + 1)
    print(last + 1)
else:
    print('Impossible')
