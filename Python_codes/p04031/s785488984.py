import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9+7
MAX = 10**18
n = int(input())
a = list(map(int,input().split()))
ans = MAX
for i in range(-100,101):
    cost = 0
    for j in range(n):
        cost += (i-a[j])**2
    ans = min(ans,cost)
print(ans)