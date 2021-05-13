import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    n, l = na()
    a = na()

    max_point = -1
    max_idx = -1
    for i in range(1, n):
        tmp = a[i] + a[i - 1]
        if tmp >= l:
            max_point = max(max_point, tmp)
            max_idx = i - 1

    if max_point == -1:
        print("Impossible")
        exit(0)

    tmp = [i for i in range(n - 1)]

    ans = []
    x = tmp[:max_idx]
    y = tmp[max_idx + 1:]
    y.reverse()

    ans = x + y

    print("Possible")
    for ansi in ans:
        print(ansi + 1)
    print(max_idx + 1)


if __name__ == '__main__':
    main()
