N, A = map(int, input().split())
X = list(map(int, input().split()))
dp = [[[0] * 3001 for i in range(51)] for j in range(51)]

dp[0][0][0] = 1

for i in range(N):
  for j in range(N):
    for k in range(0, 2501):
      dp[i+1][j][k] += dp[i][j][k]
      dp[i+1][j+1][k+X[i]] += dp[i][j][k]

ans = 0
for n in range(1, N+1):
  ans += dp[N][n][n*A]

print(ans)