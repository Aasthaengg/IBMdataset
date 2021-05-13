N, A = map(int, input().split())
X = list(map(int, input().split()))
dp = [[0]*2501 for _ in range(N+1)] # dp[n][k] := カードn枚で合計kにする選び方の数
dp[0][0] = 1

for i, x in enumerate(X):
  for n in range(i+1, 0, -1):
    for k in range(x, 2501):
      dp[n][k] += dp[n-1][k-x]

ans = 0
for n in range(1, N+1):
  ans += dp[n][A*n]
print(ans)