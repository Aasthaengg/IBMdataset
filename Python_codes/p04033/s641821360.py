from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations # (string,3) 3回
from collections import deque
from collections import defaultdict
import bisect
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

def readInts():
  return list(map(int,input().split()))
def main():
    a,b = readInts()
    judge = 0
    if a <= 0 <= b:
        pass
    elif a <= b < 0:
        if (abs(a) - abs(b) + 1)%2:
            judge = 2
        else:
            judge = 1
    else:
        judge = 1

    if judge == 0:#0がある
        print('Zero')
    elif judge == 1:#正
        print('Positive')
    else:
        print('Negative')
if __name__ == '__main__':
  main()
