ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

n = ni()
A = []
ans = 0
tmp=0
for i in range(n):
    a = ni()
    if a==0:
        ans+=tmp//2
        tmp=0
    else:
        tmp+=a
ans+=tmp//2
print(ans)
