# -*- coding: utf-8 -*-
import sys
import math
import os
import itertools
import string
import heapq
import _collections
from collections import Counter
from collections import defaultdict
from collections import deque
from functools import lru_cache
import bisect
import re
import queue
import copy
import decimal


class Scanner():
    @staticmethod
    def int():
        return int(sys.stdin.readline().rstrip())

    @staticmethod
    def string():
        return sys.stdin.readline().rstrip()

    @staticmethod
    def map_int():
        return [int(x) for x in Scanner.string().split()]

    @staticmethod
    def string_list(n):
        return [Scanner.string() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [Scanner.int() for i in range(n)]


def solve():
    N = Scanner.int()
    A = Scanner.int_cols_list(N)
    ans = 0
    for i in range(N - 1):
        ans += A[i] // 2
        A[i] %= 2
        t = min(A[i], A[i + 1])
        ans += t
        A[i] -= t
        A[i + 1] -= t
    ans += A[-1] // 2
    print(ans)


def main():
    # sys.setrecursionlimit(1000000)
    # sys.stdin = open("sample.txt")
    solve()


if __name__ == "__main__":
    main()
