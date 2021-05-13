n, a = map(int, input().split())
x = list(map(int, input().split()))

dp = [[[0 for k in range(n+1)] for j in range(n+1)] for s in range(2501)]


dp[0][0][0] = 1
for s in range(2501):
    for j in range(1, n+1):
        for k in range(j+1):
            idx = j-1
            if x[idx] > s:
                dp[s][j][k] = dp[s][j-1][k]
            else:
                dp[s][j][k] = dp[s][j-1][k] + dp[s-x[idx]][j-1][k-1]

ans = 0
for k in range(1, n+1):
    ans += dp[k*a][n][k]

print(ans)