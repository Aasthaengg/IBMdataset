from sys import stdin, stdout
from time import perf_counter

import sys
sys.setrecursionlimit(10**9)
mod = 10**9+7





n,l = map(int, input().split())
s = [input() for _ in range(n)]
s.sort()
result ="".join(s)
print(result)
