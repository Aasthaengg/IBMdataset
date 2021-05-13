from _collections import deque


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def gw():
    global input_parser
    return next(input_parser)


def gi():
    data = gw()
    return int(data)


MOD = int(1e9 + 7)

import numpy
import scipy
from collections import deque
from math import sqrt
from math import floor
# https://atcoder.jp/contests/arc081/tasks/arc081_b
# D - Coloring Dominoes
"""
need to consider the case that ticket is not enough to lower everything
"""
N = gi()
A = [0] * N

for i in range(N):
    A[i] = gi()

ans = 0
for i in range(N):
    pairs = A[i] // 2
    ans += pairs
    A[i] -= pairs * 2
    if A[i] % 2:
        if i + 1 < N and A[i + 1]:
            ans += 1
            A[i] -= 1
            A[i + 1] -= 1

print(ans)
