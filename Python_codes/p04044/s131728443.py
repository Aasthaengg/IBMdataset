import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    n, l = map(int, input().split())
    s = [input() for _ in range(n)]
    for i in range(l):
        s.sort()
    print("".join(s))
    return 0

if __name__ == "__main__":
    solve()