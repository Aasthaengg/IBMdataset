# -*- coding: utf-8 -*-
import sys 
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, A = map(int, readline().split())
X = list(map(int,readline().split()))
Y = [x-A for x in X]
dp = {0:1}

for y in Y:
    tmp = list(dp.items())
    for k,v in tmp:
        dp[k+y] = dp.get(k+y,0) + v
print(dp[0]-1) 