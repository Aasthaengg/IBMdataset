from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = [inp() for _ in range(n)]
res = 0
for i,x in enumerate(a):
    res += x//2
    if x%2:
        if i == n-1 or a[i+1] == 0: continue
        a[i+1] -= 1
        res += 1
print(res)