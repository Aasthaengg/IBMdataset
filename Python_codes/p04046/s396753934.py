#!/usr/bin/env python3
#ABC42 D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7

h,w,a,b = map(int,input().split())

fact = [1]*(200000+1)
for i in range(1,200000+1):
    fact[i] = fact[i-1]*(i) % mod

def comb(n,r):
    return fact[n] * pow(fact[r],mod-2,mod) * pow(fact[n-r],mod-2,mod) % mod
ans = 0
for i in range(b,w):
    x = comb(h-a-1+i,i)*comb(a-1+w-i-1,a-1) % mod
    ans += x
    ans %= mod
print(ans)
