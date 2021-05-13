from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
A = [inp() for i in range(n)]
rem = 0
res = 0
for i,a in enumerate(A):
    res += (a+rem)//2
    if a != 0:
        rem = (a+rem)%2
    else:
        rem = 0
print(res)