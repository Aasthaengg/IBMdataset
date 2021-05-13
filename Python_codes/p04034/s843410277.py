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
sys.setrecursionlimit(500000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m=map(int,input().split())
xy=[list(map(int,input().split())) for i in range(m)]

lst=[1]*n
anslst=[0]*n
anslst[0]=1

for x,y in xy:
    x,y=x-1,y-1
    if anslst[x]==1:
        anslst[y]=1
    lst[x]-=1
    lst[y]+=1
    if lst[x]==0:
        anslst[x]=0

print(sum(anslst))