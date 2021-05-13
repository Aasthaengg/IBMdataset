n, a = map(int, input().split())
ns = list(map(int, input().split()))
ns = [0] + ns
ma = max(ns+[a])
dp = [[[0] * (ma * n+1) for i in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    for j in range(i+1):
        for k in range(n * ma+1):
            if i == j == k == 0:
                dp[i][j][k] = 1
            elif i > 0 and k < ns[i]:
                dp[i][j][k] = dp[i - 1][j][k]
            elif i > 0 and j >= 1 and k >= ns[i]:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k - ns[i]]
print(sum(dp[n][i][i*a] for i in range(1, n+1)))

