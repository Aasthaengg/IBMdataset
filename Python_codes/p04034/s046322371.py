from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, m = MAP()
x = []
for i in range(m):
    x0, x1 = MAP()
    x.append([x0-1, x1-1])

r = [0]*n
w = [1]*n
t = [1]*n
r[0] = 1
w[0] = 0

for y in x:
    t[y[0]] -= 1
    t[y[1]] += 1

    if r[y[0]] > 0 and w[y[0]] == 0:
        r[y[0]] = 0
        r[y[1]] = 1
    elif r[y[0]] == 0 and w[y[0]] > 0:
        w[y[0]] -= 1
        w[y[1]] += 1
    elif r[y[0]] > 0 and w[y[0]] > 0:
        r[y[1]] = 1
        w[y[1]] += 1
    if t[y[0]] == 0:
        r[y[0]] = w[y[0]] = 0

ans = sum(r)
print(ans)