#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from itertools import combinations # (string,3) 3回
#from collections import deque
#import collections.defaultdict
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

def readInts():
  return list(map(int,input().split()))
def main():
    n,m = readInts()
    # 数が入っているのと、
    # 箱の中が0かどうかを判別するものを定義する
    # 全部まず1個入ってる
    # 赤は最初だけ!!!!!!!!
    nums = [1] * n
    In = [False] * n
    In[0] = True
    for i in range(m):
        a,b = map(lambda x:int(x) - 1, input().split())
        nums[a] -=1
        nums[b] +=1
        if In[a]:
            In[b] = True
        if nums[a] == 0:
            In[a] = False
    cnt = 0
    #print(In)
    for i in range(n):
        if In[i]:
            cnt += 1
    print(cnt)
if __name__ == '__main__':
  main()
