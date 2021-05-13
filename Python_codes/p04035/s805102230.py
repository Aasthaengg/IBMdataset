import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**10
mod = 10**9 + 7


def f():
    n,l = list(map(int, input().split()))
    a = list(map(int, input().split()))
    g = 0
    for i in range(1,n):
        if a[i] + a[i-1] >= l:
            g = i
            break
    if g == 0:
        print('Impossible')
        return
    print('Possible')
    for i in range(1,g):
        print(i)
    for i in range(n-1,g-1,-1):
        print(i)

f()
