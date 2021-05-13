N, A = map(int,input().split())
X = list(map(int,input().split()))
dp = [[[0 for k in range(50 * N + 1)] for j in range(N + 1)] for i in range(N + 1)]
dp[0][0][0] = 1
for i in range(1,N+1):
    for j in range(i+1):
        for k in range(50 * N + 1):
            dp[i][j][k] += dp[i-1][j][k]
            if j != 0 and k - X[i-1] >= 0:
                dp[i][j][k] += dp[i-1][j-1][k - X[i-1]]
ans = 0
for i in range(1, N+1):
    ans += dp[N][i][A * i]
print(ans)