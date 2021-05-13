# import bisect
from collections import Counter, deque
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())
    a = [int(ipti()) for _ in range(n)]
    ans = 0

    for i in range(n):
        ans += a[i] // 2
        if a[i] % 2 == 1 and i != (n-1) and a[i+1] > 0:
            ans += 1
            a[i+1] -= 1

    print(ans)


if __name__ == '__main__':
    main()