#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
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

n, a = LI()
x = LI()

# dp[i][j][k] := i番目まで見たときj個使用してkを作る場合の数
dp = [[[0] * (2500+1) for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 1
for i in range(n+1):
    xi = x[i-1]
    for j in range(2500+1):
        for k in range(i):
            dp[i][k][j] = dp[i-1][k][j]
    for j in range(xi, 2500+1):
        for k in range(1, i+1):
            dp[i][k][j] += dp[i-1][k-1][j-xi]
ans = 0
for i in range(1, n+1):
    ans += dp[-1][i][i*a]
print(ans)