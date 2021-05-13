from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()
a.sort()
res = 0
for i in range(2*n)[::2]:
    res += a[i]
print(res)
