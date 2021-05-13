import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
def gcd(*numbers): reduce(math.gcd, numbers)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
count = 0
ans = 0

N, M = I()
a = []
c = [1]*N
red = [0]*N
red[0] = 1

for i in range(M):
    x = l()
    a.append(x)
    c[x[0]-1] -= 1
    c[x[1]-1] += 1
    if red[x[0]-1]:
        red[x[1]-1] = 1
    if not c[x[0]-1]:
        red[x[0]-1] = 0


print(sum(red))
