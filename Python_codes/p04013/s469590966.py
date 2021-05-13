#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

offset = 3000

n, a = [int(item) for item in input().split()]
x = [int(item) - a for item in input().split()]

dp = [0] * 6000
dp[0 + offset] = 1

for item in x:
    if item < 0:
        for i in range(6000):
            if dp[i] == 0:
                continue 
            dp[i + item] += dp[i]
    else:
        for i in range(6000 - 1, -1, -1):
            if dp[i] == 0:
                continue 
            dp[i + item] += dp[i]
print(dp[offset] - 1)