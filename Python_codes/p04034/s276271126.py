import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics

sys.setrecursionlimit(10000001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===
def main():
    n, m = ns()

    table_TF = [False for _ in range(n)]
    table_TF[0] = True

    table_cnt = [1 for _ in range(n)]

    for _ in range(m):
        x, y = ns()
        x -= 1
        y -= 1

        table_cnt[x] -= 1
        table_cnt[y] += 1
        if table_TF[x]:
            table_TF[y] = True
        if table_cnt[x] == 0:
            table_TF[x] = False

    ans = 0
    for tf in table_TF:
        if tf:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
