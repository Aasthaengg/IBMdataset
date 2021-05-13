N, A = map(int, input().split())
X = list(map(int, input().split()))
n = N * 50
dp = [[[0]*(n+1) for j in range(N+1)] for i in range(N+1)]
dp[0][0][0] = 1

for i, a in enumerate(X, 1):
  for j in range(N+1):
    for s in range(n+1):
      dp[i][j][s] = dp[i-1][j][s]
      if a <= s:
        dp[i][j][s] += dp[i-1][j-1][s-a]

ans = 0
for m in range(1, N+1):
  ans += dp[-1][m][A*m]

print(ans)