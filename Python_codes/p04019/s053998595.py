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
    s = input()
    N = s.count('N')
    W = s.count('W')
    S = s.count('S')
    E = s.count('E')
    if N:
        if S:
            pass
        else:
            print('No')
            exit()
    if S:
        if N:
            pass
        else:
            print('No')
            exit()
    if W:
        if E:
            pass
        else:
            print('No')
            exit()
    if E:
        if W:
            pass
        else:
            print('No')
            exit()
    print('Yes')
if __name__ == '__main__':
  main()
