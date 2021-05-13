N, A = map(int, input().split())
X = list(map(int, input().split()))
sum_X = sum(X)
dp = [[[0]*(sum_X+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(N):
  for j in range(N):
    for k in range(sum_X):
      if dp[i][j][k] == 0: continue
      # not used
      dp[i+1][j][k] += dp[i][j][k]
      # used
      dp[i+1][j+1][k+X[i]] += dp[i][j][k]
ans = 0
for k in range(1, N+1):
  if k*A <= sum_X:
    ans += dp[N][k][k*A]
print(ans)  