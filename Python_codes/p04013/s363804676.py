n, a = map(int, input().split())
l = list(map(int, input().split()))

t = 50*n+1
dp = [[0]*t for _ in range(n+1)]

for i in range(n):
  x = l[i]
  for j in reversed(range(n+1)):
    for k in range(t):
      if dp[j][k] != 0:
        dp[j+1][k+x] += dp[j][k]
  dp[0][x] += 1

ans = 0
for i in range(n):
  ans += dp[i][a*(i+1)]

print(ans)