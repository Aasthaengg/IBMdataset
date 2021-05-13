n, a = map(int, input().split())
x = list(map(int, input().split()))
s = sum(x)
dp = [[0] * (s * n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][x[i - 1]] = 1
    for j in range(1, s + 1):
        dp[i][j] += dp[i - 1][j]
    for j in range(s + 1, s * n + 1):
        dp[i][j] = dp[i - 1][max(0, j - s - x[i - 1])] + dp[i - 1][j]
ans = 0
for i in range(1, n + 1):
    if i * a > s:
        print(ans)
        exit()
    ans += dp[n][i * a + (i - 1) * s]
print(ans)