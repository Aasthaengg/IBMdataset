n, a = map(int, input().split())
x = list(map(int, input().split()))
max_x = max(max(x), a)
dp = [[[0] * (n * max_x + 1) for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1
for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n * max_x + 1):
            if i >= 1 and k < x[i - 1]:
                dp[i][j][k] = dp[i - 1][j][k]
            elif i >= 1 and j >= 1 and k >= x[i - 1]:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k - x[i - 1]]
            else:
                continue
ans = 0
for j in range(1, n + 1):
    ans += dp[n][j][j * a]
print(ans)