n, a = map(int, input().split())
X = list(map(int, input().split()))

# dp[i][j][k] i枚までj枚えらんで合計k
# 答えはdp[n][1..n][a..ak]
dp = [[[0] * 2700 for _ in range(52)]
      for __ in range(52)]

dp[0][0][0] = 1
for i in range(0, n):
    for j in range(0, n + 1):
        for k in range(n * max(X) + 1):
            dp[i + 1][j][k] += dp[i][j][k]  # 選ぶ
            dp[i + 1][j + 1][k + X[i]] += dp[i][j][k]  # 選ばない

ans = 0
for i in range(1, n+1):
    for j in range(a, 2501):
        if i * a == j:
            ans += dp[n][i][j]
print(ans)
