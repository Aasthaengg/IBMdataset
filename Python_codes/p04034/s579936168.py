import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees#, log2, log
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
from decimal import Decimal
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
from decimal import *

N, M = MAP()
xy = [LIST() for _ in range(M)]

check = [0]*N
check[0] = 1
cnt = [1]*N

for x, y in xy:
	if check[x-1]:
		check[y-1] = 1
	cnt[x-1] -= 1
	cnt[y-1] += 1
	if cnt[x-1] == 0:
		check[x-1] = 0

print(sum(check))
