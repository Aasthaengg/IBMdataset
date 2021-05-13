#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
import decimal
import re
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
n,m = readInts()
box = [1] * n
nya = [True] + [False]*(n-1)
for i in range(m):
    x,y = map(lambda x:int(x)-1,input().split())
    # if box[x] < 2:
    #     if nya[x] == True:
    #         if box[x]-1 == 0:
    #             nya[x] = False
    #         nya[y] = True
    #     else:
    #         nya[y] = False
    #     box[x] -= 1
    #     box[y] += 1
    # else:
    #     nya[y] = True
    #     box[x] -= 1
    #     box[y] += 1
    box[x] -= 1
    box[y] += 1
    if nya[x]:
        nya[y] = True
    if box[x] == 0:
        nya[x] = False
print(nya.count(True))
