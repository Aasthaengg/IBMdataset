n, a = map(int, input().split())
x = list(map(int, input().split()))

dp = [[[0] * 2501 for _ in range(51)] for _ in range(51)]
dp[0][0][0] = 1

for i in range(n):
    for j in range(n):
        for k in range(2501):
            if k + x[i] <= 2500:
                dp[i+1][j+1][k+x[i]] += dp[i][j][k]
            dp[i+1][j][k] += dp[i][j][k]


ans = 0
for j in range(1, n+1):
    ans += dp[n][j][j * a]

print(ans)