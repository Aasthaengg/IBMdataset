from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
res = [False] * n
res[0] = True
cnt = [1] * n
for i in range(m):
    a,b = inpl()
    a,b = a-1,b-1
    cnt[a] -= 1; cnt[b] += 1
    if res[a]:
        res[b] = True
    if cnt[a] == 0:
        res[a] = False
print(sum(res))