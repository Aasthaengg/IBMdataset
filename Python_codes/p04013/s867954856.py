N, A = map(int, input().split())
X = list(map(int, input().split()))

dp = [[[0]*(2501) for i in range(51)] for j in range(51)]
dp[0][0][0] = 1
for i in range(N):
    value = X[i]
    for j in range(i+2):
        for k in range(2501):
            if i >= j:
                dp[i+1][j][k] += dp[i][j][k]
            if j >= 1 and k >= value:
                dp[i+1][j][k] += dp[i][j-1][k-value]

ans = sum(dp[N][x][A*x] for x in range(1,N+1))

print(ans)

