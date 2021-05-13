#!/usr/bin/env python3
n, a = map(int, input().split())
x = list(map(int, input().split()))
s = sum(x)
dp = [[[0] * (s+1) for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 1
for i in range(1, n+1):
    xi = x[i-1]
    for j in range(s+1):
        for k in range(i):
            dp[i][k][j] = dp[i-1][k][j]
    for j in range(xi, s+1):
        for k in range(1, i+1):
            dp[i][k][j] += dp[i-1][k-1][j-xi]

ans = 0
for i in range(1, n+1):
    if i*a > s:
        break
    ans += dp[n][i][i*a]
print(ans)