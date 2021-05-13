#!/usr/bin/env python3
#AGC2 C

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n,l = LI()
a = LI()
tmp = 0
inde = 0
for i in range(1,n):
  if tmp < a[i] + a[i-1]:
    tmp = a[i]+a[i-1]
    inde = i
if tmp < l:
  print('Impossible')
  quit()
print('Possible')
for i in range(1,inde):
  print(i)
for i in range(inde+1,n)[::-1]:
  print(i)
print(inde)
