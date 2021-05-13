import sys, math
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

S = set(input())
if S == {'N', 'S'} or S == {'W', 'E'} or S == {'W', 'E', 'N', 'S'}:
    print('Yes')
else:
    print('No')