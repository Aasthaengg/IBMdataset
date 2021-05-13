n, a = map(int, input().split())
X = list(map(int, input().split()))
dp = [ [[0]*(n*a+1) for j in range(i+1)] for i in range(n+1) ]
for i in range(n+1):
  dp[i][0][0] = 1
for i in range(n):
  for j in range(i+1):
    for k in range(n*a+1):
      if X[i] > k:
        if i > j:
          dp[i+1][j+1][k] = dp[i][j+1][k]
      else:
        if i > j:
          dp[i+1][j+1][k] = dp[i][j+1][k] + dp[i][j][k-X[i]]
        else:
          dp[i+1][j+1][k] = dp[i][j][k-X[i]]
ans = 0
for i in range(1, n+1):
  ans += dp[n][i][a*i]
print(ans)