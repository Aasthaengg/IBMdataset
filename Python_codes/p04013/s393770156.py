#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect, fractions
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**8)
inf = float('inf')
ans = count = 0

def counting(A):
    memo=[0]*2501
    memo[0]=1
    n=len(A)
    for ai in A:
        for i in range(2500,0,-1):
            if i-ai<0:continue
            memo[i]+=memo[i-ai]
    return memo


    

n,X=map(int,input().split())
A,B=[],[]
lis=list(map(int,input().split()))
for li in lis:
    li-=X
    if li<0:
        B.append(-li)
    elif li==0:
        count+=1
    else:
        A.append(li)
count=2**count
A.sort();B.sort()
A=counting(A)
B=counting(B)
for i in range(1,len(A)):
    ans+=A[i]*B[i]*count
ans+=count-1

print(ans)