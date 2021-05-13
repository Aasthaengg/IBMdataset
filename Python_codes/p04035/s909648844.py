import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,l=map(int,input().split())
a=list(map(int,input().split()))
I,P="Impossible","Possible"

for i in range(n-1):
    if a[i]+a[i+1]>=l:
        print(P)
        for j in range(i):
            print(j+1)
        for j in range(i+1,n)[::-1]:
            print(j)
        break
else:
    print(I)