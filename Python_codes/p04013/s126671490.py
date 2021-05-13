n, a = map(int, input().split())
x = list(map(int, input().split()))
dp = [[[0] * 2501 for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1

for i in range(n):
    for j in range(i + 1):
        for k in range(2451):
            dp[i + 1][j][k] += dp[i][j][k]
            dp[i + 1][j + 1][k + x[i]] += dp[i][j][k]

ans = 0
for j in range(1, n + 1):
    ans += dp[n][j][j * a]

print(ans)