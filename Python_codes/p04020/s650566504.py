#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
#from itertools import combinations # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict
#import bisect
#
#    d = m - k[i] - k[j]
#    if kk[bisect.bisect_right(kk,d) - 1] == d:
#
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#

import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())

n = I()
A = [I() for _ in range(n)]
ans = 0
# for i in range(n):
#     cnt += A[i]//2
#     A[i] -= (A[i]//2) * 2
# for i in range(n-1):
#     if A[i] >= 1 and A[i+1] >= 1:
#         cnt += 1
#         A[i] -= 1
#         A[i+1] -= 1
i = 0
SUM = 0
while i < n:
    if A[i] == 0:
        ans += SUM//2
        SUM = 0
    else:
        SUM += A[i]
    i += 1
ans += SUM//2
print(ans)
