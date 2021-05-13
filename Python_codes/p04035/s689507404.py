import bisect
import sys
import math
import itertools
sys.setrecursionlimit(10000)
 
# input macro
def i():
    return int(raw_input())
def ii():
    return map(int,raw_input().split(" "))
def s():
    return raw_input()
def ss():
    return raw_input().split(" ")
def slist():
    return list(raw_input())
#
 
def join(s):
    return ''.join(s)
 
#memoize macro
def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[(args)] = f(*args)
        return cache[args]
    return helper
 
nh=zip([1,0,-1,0],[0,1,0,-1])
INF = float('inf')
mod=1000000007
 
###########

n,l=ii()
a=ii()
p=-1
for j in range(n-1):
    if a[j]+a[j+1]>=l:
        p=j

if p==-1:
    print "Impossible"
else:
    print "Possible"
    x=[p+1]
    for j in range(p+2,n):
        x.append(j)
    for j in reversed(range(1,p+1)):
        x.append(j)
    x.reverse()
    for j in x:
        print j
