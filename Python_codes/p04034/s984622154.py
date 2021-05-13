#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate, product # (string,3) 3回
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
# my_round_int = lambda x:np.round((x*2 + 1)//2)
# 四捨五入
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
n,m = readInts()
red = [False] * n
red[0] = True
box = [1] * n
for i in range(m):
    x,y = map(lambda x:int(x)-1, input().split())
    box[x] -= 1
    box[y] += 1
    if red[x]:
        red[y] = True
    if box[x] == 0:
        red[x] = False
cnt = 0
for i in range(n):
    if red[i]:
        cnt += 1
print(cnt)
