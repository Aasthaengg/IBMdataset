# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, m = [int(x) for x in input().split()]
    g = defaultdict(list)
    cnt = [1] * (n + 1)
    w = [0] * (n + 1)
    w[1] = 1
    for _ in range(m):
        a, b = [int(x) for x in input().split()]
        g[a].append(b)
        cnt[a] -= 1
        cnt[b] += 1
        if w[a]:
            if cnt[a] == 0:
                w[a] = 0
            w[b] = 1
    
    ans = 0
    for i in range(1, n+1):
        if cnt[i] and w[i]:
            ans += 1
    print(ans)
    

        
    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

R s
S p
P r

"""
