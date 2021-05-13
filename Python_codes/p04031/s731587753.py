from math import *
n=int(input())
l=list(map(int,input().split()))
s=ceil(sum(l)/n)
ss=s-1
c=0
x=0
for i in range(n):
    c+=(s-l[i])**2
for i in range(n):
    x+=(ss-l[i])**2
print(min(c,x))
