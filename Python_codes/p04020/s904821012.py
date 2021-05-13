import sys

# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue
import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    ans = 0
    cnt = 0
    for _ in range(n):
        ai = ni()
        if ai == 0:
            ans += cnt // 2
            cnt = 0
        else:
            cnt += ai
    ans += cnt // 2

    print(ans)


if __name__ == '__main__':
    main()
