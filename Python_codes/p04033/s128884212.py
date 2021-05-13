from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

a,b = inpl()
if a>0 and b>0:
    res = 1
elif a*b<=0:
    res = 0
else:
    if abs(a-b)%2:
        res = 1
    else:
        res = -1
if res == 1:
    print('Positive')
elif res == 0:
    print('Zero')
else:
    print('Negative')