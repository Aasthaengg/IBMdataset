from sys import stdin, stdout
from time import perf_counter

import sys
sys.setrecursionlimit(10**9)
mod = 10**9+7


l =sorted([int(item) for item in input().split()])
print("YES" if l == [5,5,7] else "NO")