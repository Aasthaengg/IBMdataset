from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
a = [0]*n
for i in range(n):
    a[i] = INT()

ans = 0
for i in range(n-1):
    ans += a[i]//2
    a[i] %= 2
    if a[i] == 1 and a[i+1] >= 1:
        ans += 1
        a[i] -= 1
        a[i+1] -= 1
ans += a[n-1]//2
print(ans)